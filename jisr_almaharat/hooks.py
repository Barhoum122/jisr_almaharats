app_name = "jisr_almaharat"
app_title = "jisr-almaharat"
app_publisher = "admin"
app_description = "site for training and employment"
app_email = "amaralazi1000@gmail.com"
app_license = "mit"
from jisr_almaharat.route import routes

# Apps
# ------------------

# required_apps = []

###################### Start Fixtures for testing #################
fixtures = [ 
#add role  
    {"doctype": "Role", "filters": [["name", "in", ["Organization Role", "User Role"]]]},
    {"doctype": "Custom DocPerm", "filters": [["role", "in", ["Organization Role", "User Role"]]]},
#add Workflow
    {"doctype": "Workflow", "filters": [["name", "in", ["Approval Organization", "Approval Application"]]]},
    {"doctype": "Workflow State"},
    {"doctype": "Workflow Action Master"}


]
#######################        end Fixtures       #################


#######################  Start Custom Login       #################
# import frappe
# from frappe.auth import LoginManager

# def custom_login(login_manager):
#     # الحصول على بيانات المستخدم من نموذج تسجيل الدخول
#     email = frappe.form_dict.get('email')  # البريد الإلكتروني المدخل
#     password = frappe.form_dict.get('password')  # كلمة المرور المدخلة

#     # البحث في الـ DocType المخصص (Organization)
#     organization = frappe.get_all(
#         "Organization",  # اسم الـ DocType المخصص
#         filters={"email": email},
#         fields=["name", "password"]
#     )

#     if organization and organization[0].password == password:
#         # إذا تم التحقق من المستخدم، قم بتسجيل الدخول
#         frappe.local.login_manager.user = organization[0].name
#         frappe.local.login_manager.post_login()
#     else:
#         # إذا فشل التحقق، قم برمي خطأ
#         frappe.throw("Invalid email or password")

# # ربط الوظيفة بـ "login" hook
# frappe.login = custom_login

#######################  End Custom Login         #################

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "jisr_almaharat",
# 		"logo": "/assets/jisr_almaharat/logo.png",
# 		"title": "jisr-almaharat",
# 		"route": "/jisr_almaharat",
# 		"has_permission": "jisr_almaharat.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jisr_almaharat/css/jisr_almaharat.css"
# app_include_js = "/assets/jisr_almaharat/js/jisr_almaharat.js"

# include js, css files in header of web template
# web_include_css = "/assets/jisr_almaharat/css/jisr_almaharat.css"
# web_include_js = "/assets/jisr_almaharat/js/jisr_almaharat.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "jisr_almaharat/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "jisr_almaharat/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }
############## Here line to git file routes
website_route_rules = routes
############## Here line to git file routes
# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "jisr_almaharat.utils.jinja_methods",
# 	"filters": "jisr_almaharat.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "jisr_almaharat.install.before_install"
# after_install = "jisr_almaharat.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "jisr_almaharat.uninstall.before_uninstall"
# after_uninstall = "jisr_almaharat.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "jisr_almaharat.utils.before_app_install"
# after_app_install = "jisr_almaharat.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "jisr_almaharat.utils.before_app_uninstall"
# after_app_uninstall = "jisr_almaharat.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jisr_almaharat.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"jisr_almaharat.tasks.all"
# 	],
# 	"daily": [
# 		"jisr_almaharat.tasks.daily"
# 	],
# 	"hourly": [
# 		"jisr_almaharat.tasks.hourly"
# 	],
# 	"weekly": [
# 		"jisr_almaharat.tasks.weekly"
# 	],
# 	"monthly": [
# 		"jisr_almaharat.tasks.monthly"
# 	],
# }



scheduler_events = {
 
	# "daily": [
	# 	"jisr_almaharat.tasks.daily"
	# ],jisr_almaharat/jisr_almaharat/programming_module/doctype/job/job.py"
	"hourly": [
		"jisr_almaharat.jisr_almaharat.programming_module.task.update_status"
	],
 
 
}
# Testing
# -------

# before_tests = "jisr_almaharat.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "jisr_almaharat.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "jisr_almaharat.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["jisr_almaharat.utils.before_request"]
# after_request = ["jisr_almaharat.utils.after_request"]

# Job Events
# ----------
# before_job = ["jisr_almaharat.utils.before_job"]
# after_job = ["jisr_almaharat.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"jisr_almaharat.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

