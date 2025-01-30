// Copyright (c) 2024, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Application", {
	// refresh(frm) {

	// },
    
    // to change the link application_name to another doctype by change the kind value
    kind: function (frm) {
        // Check the value of the "kind" field
        if (frm.doc.kind === 'Training') {
            // Set the application_name field to link to Training
            frm.set_df_property('application_name', 'options', 'Training');
        } else {
            // Default: Link application_name to Job
            frm.set_df_property('application_name', 'options', 'Job');
        }
    }
});
