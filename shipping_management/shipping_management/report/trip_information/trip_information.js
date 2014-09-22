// Copyright (c) 2013, New Indictranstech Pvt Ltd and contributors
// For license information, please see license.txt

frappe.query_reports["Trip Information"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("Date"),
			"fieldtype": "Date",
			"default": get_today()
		},
		{
			"fieldname":"to_date",
			"label": __("Date"),
			"fieldtype": "Date",
			"default": get_today()
		},
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Shipping Company"
		},
		{
			"fieldname":"container",
			"label": __("Container Type"),
			"fieldtype": "Link",
			"options": "Container"
		}
	]
}
