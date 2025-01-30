# Copyright (c) 2024, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

#import the email valion
from frappe.utils import validate_email_address 
from frappe import throw


class Organization(Document):
	def validate_email(doc,method):
		if doc.email and not validate_email_address (doc.email):
			throw("Invail email address.")
	

	

