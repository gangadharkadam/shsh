cur_frm.cscript.onload = function(doc,cdt,cdn){
  if(doc.__islocal){
  	ft=['Basic Fare','Surcharge and Taxes','Total Payable']
  	f=[100000,50000,150000]
     for (i=0;i<=2;i++){
      var acc = frappe.model.add_child(doc, "Booking Details1", "table_7");
      acc.fare_type=ft[i];
      acc.fare=f[i]
      }
    doc.amount=150000;    
  }
}

cur_frm.cscript.login = function(doc, cdt, cdn){
		// frappe.model.open_mapped_doc({
		// 	method: "erpnext.selling.doctype.lead.lead.make_customer2",
		// 	frm: cur_frm
		// })
		window.open('/files/bank_payment1.html','open_window','menubar, toolbar, location, directories, status, scrollbars, resizable,dependent, width=640, height=480, left=0, top=0')
		// window.open('/files/bank_payment.html','_self')
}