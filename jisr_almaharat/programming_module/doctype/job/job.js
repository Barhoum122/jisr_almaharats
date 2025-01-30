// Copyright (c) 2024, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Job", {
	refresh(frm) {
        frm.set_value('posting_date', frappe.datetime.get_today());
	},
    // onload(frm){
    //     frm.set_value('posting_date', frappe.datetime.get_today());
        
    // }
});
