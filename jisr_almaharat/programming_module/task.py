# Copyright (c) 2024, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import getdate,get_datetime


def update_status():
 	job = frappe.get_all("Job", fields=["name", "status", "aplication_deadline"])
	now_date = get_datetime(now())	#
	if self.aplication_deadline and self.status:

		
		#  Aplication Deadline
		deadline = getdate(self.aplication_deadline)
		frappe.msgprint("hello")
		#
		if now_date == deadline:
			frappe.msgprint("hell00000o")

		
			# Aplication Deadline
			frappe.db.set_value("Job", self.jop_title, "status", "Closed")
			frappe.msgprint("Job status is now Closed.")

# def validate(self):
# 	# to commar if aplication deadline smaler than pasting date
# 	if self.aplication_deadline < self.posting_date:
# 		frappe.throw("Aplication Deadline Can't be smaller than Poating Date")
	
	
