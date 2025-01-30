// Copyright (c) 2024, admin and contributors
// For license information, please see license.txt

// frappe.ui.form.on("User1", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("User1", {
    	refresh(frm) {
    
    	},/*this code for password confirm */
        validate: function(frm){
        // the email validation
            if (frm.doc.email && ! frappe.utils.validate_type(frm.doc.email,'email')){
                frappe.throw('invalid email address');
            }
        //passwords 
            var password = frm.doc.password;
            var confirm_password = frm.doc.confirm_password;
            if(password !== confirm_password){
                frappe.throw('Passwords do not match!');
                //frappe.validate =false;
            }

        }
     });
    