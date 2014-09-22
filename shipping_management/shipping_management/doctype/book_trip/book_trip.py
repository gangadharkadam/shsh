# Copyright (c) 2013, New Indictranstech Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.email_lib import sendmail
from frappe.utils import flt ,cint, cstr

class BookTrip(Document):
	def fill_trip_info(self):
		trip_info = self.get_trip_info()
		self.calc_price(trip_info)
		self.fill_chld(trip_info)

	def get_trip_info(self):
		return frappe.db.sql("""select start_date,end_date,trip_id,ship_name,container,(capacity-booked_container) as available_capacity from 
			(
			SELECT
			    t.start_date,
			    t.end_date,
			    t.name as trip_id,
			    s.name as ship_name,
			    c.container,
			    c.capacity,
			    coalesce((select  sum(booked_container) from `tabShip Container Log` where trip_id=t.name and container=c.container),0) as booked_container    
			FROM
			    tabTrip t,
			    tabShip s,
			    `tabCargo Details` c
			WHERE
			t.ship_id=s.name
			and s.name=c.parent
			)foo
			where
			start_date>=coalesce(date('%(from_date)s'),now()) and end_date<=coalesce(date('%(to_date)s'),now()) and container='%(container)s' and (capacity-booked_container)>=%(qty)s
			and exists(select true from `tabSub Routes` where parent=foo.trip_id and location='%(source)s')
			and exists(select true from `tabSub Routes` where parent=foo.trip_id and location='%(dest)s')
		"""%{'from_date':self.from_date, 'to_date': self.to_date,
		'container': self.container, 'qty': self.qty, 'source':self.source, 'dest':self.destination}, as_dict=1)
	
	def calc_price(self, trip_info):
		for trip in trip_info:
			self.get_amt(trip)

		frappe.errprint(trip_info)

	def get_amt(self, trip):
		amt = frappe.db.sql(""" select s.name,(dr.rate-sr.rate)*coalesce((select conversion_rate from `tabExchange Details` ed where spl.currency=ed.to_currency and ed.from_currency='%(s_currency)s'),1) as final_rate
			from tabShip s,`tabShipping Price List` spl,
			`tabSub Route` sr,`tabSub Route` dr where spl.shipping_company = s.company  and sr.parent = spl.name 
			and dr.parent = spl.name and dr.location = '%(dest)s' 
			and sr.location='%(source)s' and spl.container = '%(container)s' and s.name = '%(ship_id)s'
			"""%{'ship_id':trip.ship_name, 'container':trip.container,'source':self.source, 'dest':self.destination, 's_currency':self.currency},as_list=1, debug=1)

		if amt:
			trip['amt'] = amt[0][1]

	def fill_chld(self, trip_info):
		self.set('trip_info', [])

		for d in trip_info:
			nl = self.append('trip_info', {})
			nl.trip_id =d.trip_id
			nl.from_date = d.start_date
			nl.to_date = d.end_date
			nl.ship_id = d.ship_name
			nl.container = self.container
			nl.qty = self.qty
			nl.rate = d.amt
			nl.amount = cstr(flt(nl.qty) * flt(d.amt))

	def fil_selected_trip(self):
		self.set('selected_trip', [])
		for d in self.get('trip_info'):
			if cint(d.select) == 1:
				nl = self.append('selected_trip', {})
				nl.trip_id =d.trip_id
				nl.ship_id = d.ship_id
				nl.container = d.container
				nl.qty = d.qty
				nl.rate = d.rate
				nl.amount = d.amount

	def make_log_entry(self):
		so_no = self.make_log()
		self.make_so(so_no)
		return True


	def make_log(self):
		so =frappe.new_doc('Shipping Sales Order')
		so.field = 'test'
		so.save(ignore_permissions=True)

		for d in self.get('selected_trip'):
			ml = frappe.new_doc('Ship Container Log')
			ml.trip_id = d.trip_id
			ml.ship_id = d.ship_id
			ml.container = d.container
			ml.booked_container = d.qty
			ml.order_no = so.name
			ml.save()

		return so.name

	def make_so(self, order_no):
		child_table = self.getchild_table()

		body= "<html><body><table wisth='100%''><tr><td>Customer Name</td><td>"+self.customer_name+"</td><td>Contact </td><td>"+self.email_id+"</td></tr><tr><td>From Date</td><td>"+self.from_date+"</td><td>To Date </td><td>"+self.to_date+"</td></tr><tr><td>Currency</td><td>"+self.currency+"</td><td>Order No </td><td>"+order_no+"</td></tr></table><table style='100%'>"+child_table+"</table></body></html>"
		sendmail(self.email_id,subject='Sales Order',msg=body)
		frappe.msgprint("Send Successfully")
		return True
		

	def getchild_table(self):
		body = '<tr><td style="border: 1pt solid #777;border-collapse: collapse;">SR</td><td style="border: 1pt solid #777;border-collapse: collapse;">Trip Id</td><td style="border: 1pt solid #777;border-collapse: collapse;">Ship Id</td><td style="border: 1pt solid #777;border-collapse: collapse;">Container</td><td style="border: 1pt solid #777;border-collapse: collapse;">Qty</td><td style="border: 1pt solid #777;border-collapse: collapse;">Rate</td><td style="border: 1pt solid #777;border-collapse: collapse;">Amount</td><tr>'
		for d in self.get('selected_trip'):
			body +=""" <tr><td style="border: 1pt solid #777;border-collapse: collapse;">%s</td><td style="border: 1pt solid #777;border-collapse: collapse;">%s</td>
			<td style="border: 1pt solid #777;border-collapse: collapse;">%s</td>
			<td style="border: 1pt solid #777;border-collapse: collapse;">%s</td>
			<td style="border: 1pt solid #777;border-collapse: collapse;">%s</td>
			<td style="border: 1pt solid #777;border-collapse: collapse;">%s</td><td style="border: 1pt solid #777;border-collapse: collapse;">%s</td></tr>
			"""%(cstr(d.idx), d.trip_id, d.ship_id, d.container, cstr(d.qty), cstr(d.rate), cstr(d.amount))

		return body

	def toggle_selection(self, index):
		for d in self.get('trip_info'):
			if cint(d.idx) == cint(index):
				d.select = 1
			else:
				d.select = 0
		return True
