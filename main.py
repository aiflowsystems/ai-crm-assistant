import csv
import json
from pathlib import Path
from modules.customer_analyzer import analyze_customers
from modules.followup_generator import generate_followups
from modules.report_generator import generate_crm_report

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

output_folder = config["output_folder"]

Path(output_folder).mkdir(exist_ok=True)

customers = []

with open("customers.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customers.append(row)

crm_summary = analyze_customers(customers)
followups = generate_followups(customers)
crm_report = generate_crm_report(crm_summary, followups)

print("AI CRM Assistant")
print("================")
print()

print(f"Customers loaded: {len(customers)}")

for customer in customers:
    print(customer["company"], "-", customer["status"])

print()
print("CRM Summary")
print("-----------")
print(f"Total Customers: {crm_summary['total_customers']}")
print(f"New Customers: {crm_summary['new_customers']}")
print(f"No Reply Customers: {crm_summary['no_reply_customers']}")
print(f"Replied Customers: {crm_summary['replied_customers']}")
print(f"High Priority Customers: {crm_summary['high_priority_customers']}")

print()
print("FOLLOW-UP TASKS")
print("---------------")

for task in followups:
    print(task)

report_file = Path(output_folder) / config["crm_report_file"]

with open(report_file, "w", encoding="utf-8") as file:
    file.write(crm_report)

print()
print(f"CRM report generated: {report_file}")
