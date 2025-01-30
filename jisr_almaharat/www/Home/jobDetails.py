import frappe # type: ignore
def get_context(context):
    try:
       context.detail = frappe.get_doc("Job",frappe.form_dict.docname)
      #  print(f"\n\n\n\n\n\n{context.detail}\n\n\n\n\n")
    except Exception as e:   
       frappe.local.flags.redirect_location ='/404'
       raise frappe.Redirect       
    return context
