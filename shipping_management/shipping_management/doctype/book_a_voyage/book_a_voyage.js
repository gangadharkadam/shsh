cur_frm.cscript.select = function(doc, cdt, cdn){
	var d =locals[cdt][cdn]
	
	get_server_fields('toggle_selection',d.idx,'',doc, cdt, cdn, 1, function(){
		refresh_fields('trip_info')
	})
}

cur_frm.cscript.final_trip = function(doc, cdt, cdn){
	get_server_fields('make_log_entry','','',doc, cdt, cdn,1, function(){
		window.location.reload()
	})
}