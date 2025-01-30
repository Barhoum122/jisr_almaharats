# Copyright (c) 2024, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import getdate

class Job(WebsiteGenerator):
	def on_update(self):
		# التحقق من وجود الحقول المطلوبة
		if self.aplication_deadline and self.status:

			# الحصول على تاريخ اليوم
			today = getdate()

			# الحصول على تاريخ Aplication Deadline
			deadline = getdate(self.aplication_deadline)
			frappe.msgprint("hello")
			# مقارنة التواريخ
			if today == deadline:
				frappe.msgprint("hell00000o")

			
				# إذا كان تاريخ اليوم يساوي Aplication Deadline
				frappe.db.set_value("Job", self.jop_title, "status", "Closed")
				frappe.msgprint("Job status is now Closed.")

	# def validate(self):
	# 	# to commar if aplication deadline smaler than pasting date
	# 	if self.aplication_deadline < self.posting_date:
	# 		frappe.throw("Aplication Deadline Can't be smaller than Poating Date")
		
		
