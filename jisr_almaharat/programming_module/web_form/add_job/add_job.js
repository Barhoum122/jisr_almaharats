frappe.ready(function() {  
    // bind events here 
	//Organization Site add value to it
	$('input[data-fieldname="organization"]').on('change', function() {
		var organization = $('input[data-fieldname="organization"]').val();
		frappe.db.get_value("Organization", organization, "site", function(value) {
			$('input[data-fieldname="site"]').val(value.message.site);
		});
	});
 
});