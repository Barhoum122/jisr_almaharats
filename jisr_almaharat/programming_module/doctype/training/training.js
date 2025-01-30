// Copyright (c) 2024, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Training", {
	refresh(frm) {
        // to set the posting value
        frm.set_value('training_post_date', frappe.datetime.get_today());
	},
});
