import frappe # type: ignore
from frappe.model.document import Document # type: ignore
def get_context(context):
    try:
       context.applicant = frappe.get_doc("Job","JOP-ID-00005")
       print(f"\n\n\n\n\n\n{context.applicant}\n\n\n\n\n")
    except Exception as e:   
       frappe.local.flags.redirect_location ='/404'
       raise frappe.Redirect       
    return context