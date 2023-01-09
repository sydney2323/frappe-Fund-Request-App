# Copyright (c) 2022, sydney and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class monthly_category_project_budget(Document):
    def before_save(self):
       self.amount_copy = self.amount
       exists = frappe.db.exists(
           "monthly_category_project_budget",
           {
               "project": self.project,
               "category": self.category,
               "monthly": self.monthly
               },
           )
       if exists:
           frappe.throw(f'{self.project} and {self.category} for {self.monthly} month already exist')
	     
       existsB = frappe.db.exists(
            "monthly_budget",
           {
               "month_name": self.monthly,
               "budget_amount":("<",self.amount)
               },
           )
       if existsB:
           frappe.throw("Amount is greater than monthly budget")
       else:
           amount = frappe.db.get_value('monthly_budget', self.monthly, 'budget_amount')
           amount = amount - self.amount
           frappe.db.set_value('monthly_budget', self.monthly, 'budget_amount', amount)
           
     
     
