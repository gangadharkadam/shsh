# Copyright (c) 2013, New Indictranstech Pvt Ltd and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Service')

class TestService(unittest.TestCase):
	pass
