# Copyright (c) 2013, New Indictranstech Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MakePayment(Document):
		
	def payment(self):
		frappe.msgprint("Thank you for payment");

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

		
		
	

