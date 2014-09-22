cur_frm.cscript.route = function(doc, cdt, cdn){
	get_server_fields('get_routes','','',doc, cdt, cdn,1, function(){
		refresh_field('sub_routes')
	})
}

cur_frm.cscript.validate = function(doc, cdt, cdn){
	refresh_field('sub_routes')
}