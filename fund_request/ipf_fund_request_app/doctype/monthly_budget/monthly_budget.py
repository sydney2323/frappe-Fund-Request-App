# Copyright (c) 2022, sydney and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class monthly_budget(Document):

	def autoname(self):
		self.name = self.month_name
	def before_save(self):
			self.budget_amount_copy = self.budget_amount
			check_month_name_exists = frappe.db.exists(
				"monthly_budget",
				{
					"month_name": self.month_name
				},
			)
			if check_month_name_exists:
				frappe.throw("Budget for this Month is available")