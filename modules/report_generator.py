def generate_crm_report(crm_summary, followups):
    followup_text = "\n".join(followups)

    report = f"""AI CRM Assistant Report

CRM Summary
===========

Total Customers: {crm_summary['total_customers']}
New Customers: {crm_summary['new_customers']}
No Reply Customers: {crm_summary['no_reply_customers']}
Replied Customers: {crm_summary['replied_customers']}
High Priority Customers: {crm_summary['high_priority_customers']}

Follow-up Tasks
===============

{followup_text}
"""

    return report