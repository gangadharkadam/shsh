# Copyright (c) 2013, New Indictranstech Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	columns = get_column()
	data = get_data(filters)
	return columns, data

def get_column():
	columns =["Trip:Link/Trip:120", "Start Date::80", "End Date::80", "Ship Name::80", "Company::80","Container::80", "Available Quantity","Booked Quantity"]
	return columns

def get_data(filters):
	return frappe.db.sql("""select trip_id,start_date,end_date,ship_name, company,container,(capacity-booked_container) as available_capacity, booked_container from 
(
SELECT
    t.start_date,
    t.end_date,
    t.name as trip_id,
    s.name as ship_name,
    s.company,
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
start_date>=coalesce(date('%(from_date)s'),now()) and end_date<=coalesce(date('%(to_date)s'),now()) %(cond)s 
"""%{'from_date': filters.get("from_date"), 'to_date': filters.get("to_date"), 'cond': make_cond(filters)}, as_list=1, debug=1)

def make_cond(filters):
	cond = []
	if filters.get('container'):
		cond.append("container='%s'"%filters.get('container'))

	if filters.get('company'):
		cond.append("company='%s'"%filters.get('company'))	

	if cond:
		return ' and ' + ' and '.join(cond)	
	else:
		return ''

