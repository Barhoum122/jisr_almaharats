import frappe # type: ignore
def get_context(context):
    context.Full_time=frappe.get_all("Job",
    fields=["name","jop_title","aplication_deadline","organization_name","jop_type","jop_location"])
    # context.Full_time=frappe.db.sql(""" SELECT jop_title FROM tabJob """ ),
    # for job in context.Full_time:
    #  print("\n\n\n",job['jop_title'],"\n\n\n\n")
    return context
 
