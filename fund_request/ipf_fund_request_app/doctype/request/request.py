# Copyright (c) 2022, sydney and contributors
# For license information, please see license.txt

# import frappe
from ast import If
from frappe.model.document import Document
import frappe
import datetime
import calendar


class request(Document):
    def before_save(self):
        if frappe.get_roles(frappe.session.user)[0] == 'staff':
            self.user = frappe.session.user
            self.status = 'Pending'

    def on_trash(self):
        if self.status == 'Approved':
            frappe.throw("You request can not be deleted")

    def on_change(self):
        if frappe.get_roles(frappe.session.user)[0] == 'finance':
          
          medate = datetime.datetime.strptime(self.date, '%Y-%m-%d')
          requestMonth = calendar.month_abbr[medate.month]
          
          if self.status == 'Approved':
            
            exists = frappe.db.exists(
              "monthly_category_project_budget",
              {
                "project": self.project,
                "category": self.category,
                "monthly": requestMonth
                },
              )
            if exists:
              amount = frappe.db.get_value('monthly_category_project_budget', requestMonth, 'amount')
              amount = amount - self.amount
              frappe.db.set_value('monthly_budget', self.monthly, 'budget_amount', amount)
            else:
              frappe.throw(f'{self.project} and {self.category} for {requestMonth} month Does Not exist')
