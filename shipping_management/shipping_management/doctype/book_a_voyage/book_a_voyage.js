cur_frm.cscript.select = function(doc, cdt, cdn){
	var d =locals[cdt][cdn]	
	get_server_fields('toggle_selection',d.idx,'',doc, cdt, cdn, 1, function(){
		refresh_field('trip_info')
	})
}
cur_frm.cscript.add_trip = function(doc, cdt, cdn){
		frappe.model.open_mapped_doc({
			method: "shipping_management.shipping_management.doctype.book_a_voyage.book_a_voyage.make_customer",
			frm: cur_frm
		})
}

