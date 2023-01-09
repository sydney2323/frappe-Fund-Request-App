// Copyright (c) 2022, sydney and contributors
// For license information, please see license.txt

frappe.ui.form.on('request', {
	refresh: function(frm) {
		if (frappe.user_roles[0] == 'staff') {
			frm.toggle_enable("feedback",false)
		   frm.toggle_enable("status",false)
		  
		   if (frm.doc.status == 'Approved') {
			frm.disable_save();
			frm.toggle_enable("amount",false)
			frm.toggle_enable("reason",false)
			frm.toggle_enable("project",false)
			frm.toggle_enable("category",false)
			}

			if (frm.doc.status == 'Rejected') {
				frm.toggle_enable("status",false)
				}
		}

		// if (frappe.user_roles[0] == 'finance') {
		// 	if (frm.doc.status == 'Rejected') {
		// 		frm.toggle_enable('feedback', true)
		//  }
		// }

		// cur_frm.cscript.custom_status = function(doc) {
		// 	cur_frm.toggle_display("feedback", doc.status=="Pending");
	//    }

	
	}
	   
});
