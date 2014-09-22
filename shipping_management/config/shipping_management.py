from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Book Trip",
					"description": _("book trip"),
					"label": _("")
				},
				{
					"type": "doctype",
					"name": "Exchange Details",
					"description": _("Exchange Details"),
					"label": _("")
				},
				

			]
		},
		{
			"label": _("Masters"),
			"icon": "icon-file",
			"items": [
				{
					"type": "doctype",
					"name": "Ship",
					"description": _("Ship"),
					"label": _("")
				},
				{
					"type": "doctype",
					"name": "Location",
					"description": _("Location"),
					"label": _("")
				},
				{
					"type": "doctype",
					"name": "Container",
					"description": _("Container"),
					"label": _("")
				},
				{
					"type": "doctype",
					"name": "Trip",
					"description": _("Trip"),
					"label": _("")
				},
				{
					"type": "doctype",
					"name": "Route",
					"description": _("Route"),
					"label": _("")
				},
				{
					"type": "doctype",
					"name": "Shipping Company",
					"description": _("Shipping Address"),
					"label": _("")
				},
				{
					"type": "doctype",
					"name": "Shipping Price List",
					"description": _("Shipping Price List"),
					"label": _("")
				},
		

			   ]
		    },
		    {
			"label": _("Main Reports"),
			"icon": "icon-table",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Ledger",
					"doctype": "Item",
				},
				
			]
		},
		
		
	]
