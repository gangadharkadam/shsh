cur_frm.cscript.select = function(doc, cdt, cdn){
	var d =locals[cdt][cdn]	
	get_server_fields('toggle_selection',d.idx,'',doc, cdt, cdn, 1, function(){
		refresh_field('trip_info')
	})
}
cur_frm.cscript.add_trip = function(doc, cdt, cdn){
		frappe.model.open_mapped_doc({
			method: "erpnext.selling.doctype.lead.lead.make_customer1",
			frm: cur_frm
		})
}

