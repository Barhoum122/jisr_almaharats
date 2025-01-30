frappe.ready(function () {


	// frappe.web_form.set_value('book_name', applicand_detail.book_name);
	setTimeout(function () {
		frappe.web_form.set_value('application_name', "{{detail.jop_title }}");
		frappe.web_form.set_value('applicant_name', "{{ frappe.get_fullname() }}");
		frappe.web_form.set_value('kind', '{{Job_kind}}');
	}, 100);


	// 	fetchJobDetails("kjkj");

	// 	// const job_id = urlParams.get('job_id');
	// 	function fetchJobDetails(jobId) {
	// 		const urlParams = new URLSearchParams(window.location.search);
	// 		alert('sssssssssssssss', urlParams)
	// 		frappe.call({
	// 			// method: 'jis r_almaharat.api.get_context',
	// 			// method: 'jisr_almaharat.web_form.get_context',
	// 			method: 'jisr_almaharat.programming_module.web_form.application.application.get_context',
	// 			args: {
	// 				// job_id: jobId
	// 			},
	// 			callback: function (response) {
	// 				if (response.message.status === "success") {
	// 					const data = response.message.data;
	// 					// console.log(data.au_name)
	// 					frappe.web_form.set_value('application_name', data.jop_title);
	// 					// frappe.web_form.set_value('au_name', data.jop_title);
	// 					console.log("Data has been set in the Web Form fields.");
	// 				} else {
	// 					console.error('Error:', response.message.message);
	// 				}
	// 			},
	// 			error: function (error) {
	// 				console.error('Error fetching job details:', error);
	// 			}
	// 		});
	// 	}



})



// const urlParams = new URLSearchParams(window.location.search);
// 	const job_id ='f8a0ab7763'
// 	console.log(job_id)
// 	if (job_id) {
// 		frappe.call({
// method: 'jisr_almaharat/programming_module/web_form/form_book/form_book.get_context',
// 			// method: 'jisr_almaharat/programming_module.get_context',
// 			method: 'jisr_almaharat.api.get_context',

// 			args: {
// 				job_id: job_id
// 			},
// 			callback: function (r) {
// 				console.log(r.message.book_name)
// 				if (r.message) {
// 					// frappe.web_form.set_value('book_name', r.message.book_name);
// 					frappe.web_form.set_value('book_name', r.message.book_name);

// 					frappe.web_form.set_value('au_name', r.message.au_name);
// 					frappe.msgprint(__('تم تعبئة الحقول بنجاح!'));
// 				}
// 			}
// 		});
// 	} else {
// 		frappe.msgprint(__('لم يتم العثور على ID الوظيفة.'));
// 	}

// frappe.web_form.ready(function () {

// });





