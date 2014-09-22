# Copyright (c) 2013, New Indictranstech Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ShippingPriceList(Document):
	def validate(self):
		pl = frappe.db.sql("""select name from `tabShipping Price List`
			where shipping_company = '%s' and currency = '%s' and container = '%s' 
				and route = '%s'"""%(self.shipping_company, self.currency, self.route, self.container))
		if pl:
			if pl[0][0] != self.name:
				frappe.msgprint("Price List already exist", raise_exception=1)

	def fill_sub_route_details(self):
		sub_route = get_route_details(self)

		self.set('sub_route_details', [])

		for d in sub_route:
			nl = self.append('sub_route_details', {})
			nl.location = d[0]
			
def get_route_details(self):
	sub_route = frappe.db.sql("""select location from `tabSub Routes` where parent = '%s' """%self.route,as_list=1)
	source = frappe.db.get_value('Route', self.route, 'source_route')
	dest = frappe.db.get_value('Route', self.route, 'target_route')
	sub_route.insert(0,[source])
	sub_route.insert(len(sub_route),[dest])
	return sub_route