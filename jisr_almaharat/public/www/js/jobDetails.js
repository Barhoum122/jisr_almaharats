// document.querySelector("#apply-botton").addEventListener('click', (e) => {
//     let d = new frappe.ui.Dialog({
//         title: 'Enter details',
//         fields: [
//             {
//                 label: 'First Name',
//                 fieldname: 'book_name',
//                 fieldtype: 'Data',
//                 default: 'nn',


//             },


//             {
//                 label: 'Au Name',
//                 fieldname: 'au_name',
//                 fieldtype: 'Data'
//             },
//         ],
//         size: 'small', // small, large, extra-large
//         primary_action_label: 'Submit',
//         primary_action(values) {
//             console.log(values);

//             fetch('/api/method/jisr_almaharat.api.new_book', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-Frappe-CSRF-Token': frappe.csrf_token
//                 },
//                 body: JSON.stringify(values)
//             })
//                 .then(response => {
//                     // if (!response.ok) {
//                     //     throw new Error('Network response was not ok');
//                     // }
//                     return response.json();
//                 })
//                 .then(data => {
//                     if (data.message) {
//                         frappe.msgprint(__("Success: {0}", [data.message]));
//                     } else {
//                         frappe.msgprint({
//                             title: '<span style="color: red;">Error</span>',
//                             indicator: 'red',
//                             message: __("Data submit failed: {0}", [data.message])
//                         });
//                     }
//                 })
//                 .catch(error => {
//                     console.error('Error:', error);
//                     frappe.msgprint({
//                         title: '<span style="color: red;">Error</span>',
//                         indicator: 'red',
//                         message: __("An error occurred: {0}", [error.message])
//                     });
//                 });

//             d.hide();
//         }
//     });

//     d.show();
//     console.log("clicked");
// });

document.querySelector("#apply-botton").addEventListener('click', (e) => {

// get request from html to python file 
    function fetchJobDetails(jobId) {
        alert('sssssssssssssss')
        frappe.call({
            // method: 'jis r_almaharat.api.get_context',
            // method: 'jisr_almaharat.web_form.get_context',
            method: 'jisr_almaharat.programming_module.web_form.application.application.get_context',
            args: {
                job_id: jobId
            },
            callback: function (response) {
                if (response.message.status === "success") {
                    const data = response.message.data;
                    console.log(data.au_name)
                    frappe.web_form.set_value('application_name', data.jop_title);
                    // frappe.web_form.set_value('au_name', data.jop_title);
                    console.log("Data has been set in the Web Form fields.");
                } else {
                    console.error('Error:', response.message.message);
                }
            },
            error: function (error) {
                console.error('Error fetching job details:', error);
            }
        });
    }



});

