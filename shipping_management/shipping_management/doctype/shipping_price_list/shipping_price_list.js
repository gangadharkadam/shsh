cur_frm.add_fetch('shipping_company', 'currency', 'currency')
cur_frm.cscript.route = function(doc, dt, dn){
	return $c('runserverobj', args={'method':'fill_sub_route_details', 'docs':doc}, function(r,rt) {
			cur_frm.refresh();
	});
}