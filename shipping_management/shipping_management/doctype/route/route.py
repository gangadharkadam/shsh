# Copyright (c) 2013, New Indictranstech Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Route(Document):
	def validate(self):
		for d in self.get('sub_route'):
			if d.location == self.source_route or d.location == self.target_route:
				frappe.throw(_("No need to add Source or Target location under sub routes at row {0}").format(d.idx))

			if self.source_route == self.target_route:
				frappe.throw(_("Source and Target must not be equal"))

