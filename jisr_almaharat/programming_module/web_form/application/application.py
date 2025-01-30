import frappe # type: ignore
# @frappe.whitelist(allow_guest=True)
def get_context(context):
	try:	
			# this line to get Jobkind context from url
			context.Job_kind =frappe.form_dict.get("Jobkind")
			if context.Job_kind in ['Job','Training']:
				context.Job_kind
			# this line to get name context from url
				context.detail = frappe.get_doc("Job",frappe.form_dict.docname)
			# print(f"\n\n\n\n\n\n{context.Job_kind}\n\n\n\n\n")
				return context
			else:
			# if the data in url not found or false go to page 404 
				frappe.local.flags.redirect_location ='/404'
				raise frappe.Redirect  

	except Exception as e:
					frappe.local.flags.redirect_location ='/404'
					raise frappe.Redirect  
	                

				