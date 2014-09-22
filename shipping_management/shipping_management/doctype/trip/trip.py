# Copyright (c) 2013, New Indictranstech Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from shipping_management.shipping_management.doctype.shipping_price_list.shipping_price_list import get_route_details

class Trip(Document):
	def validate(self):
		self.get_routes()

	def get_routes(self):
		sub_route = get_route_details(self)
		self.set('sub_routes', [])

		for d in sub_route:
			nl = self.append('sub_routes', {})
			nl.location = d[0]
		
