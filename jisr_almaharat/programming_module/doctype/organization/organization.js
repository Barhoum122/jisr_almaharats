// Copyright (c) 2024, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Organization", {
	// refresh(frm) {
    //     frappe.msgprint("hello ammar");

	// },

    
    validate: function(frm){
        
        // to ensur the name only letters
        const nameField = frm.doc.organization_name; 
        const isValid = /^[A-Za-z\s]+$/.test(nameField);

        if (!isValid) {
            frappe.throw(__('Name should contain only letters and spaces.'));
        }


       
            // the email validation
                if (frm.doc.email && ! frappe.utils.validate_type(frm.doc.email,'email')){
                    frappe.throw('invalid email address');
                }
        
    }

         

    
});
