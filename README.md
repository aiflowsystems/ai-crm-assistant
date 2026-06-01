# AI CRM Assistant

An AI-powered CRM assistant that analyzes customer data, tracks lead status, generates follow-up tasks, and creates centralized CRM reports.

Designed to help freelancers, sales teams, and small businesses manage customer relationships, follow-up workflows, and lead status tracking more efficiently.

---

## Features

### Customer Management

- Read customer data from CSV files
- Track customer status
- Monitor last contact timing
- Organize customers by priority

### CRM Analysis

- Count total customers
- Identify new customers
- Track no-reply customers
- Track replied customers
- Count high-priority customers

### Follow-up Generation

- Generate follow-up tasks for no-reply customers
- Include customer priority in follow-up reminders
- Support simple CRM follow-up workflows

### CRM Reporting

- Generate centralized CRM reports
- Summarize customer status
- List follow-up tasks
- Save reports automatically in the outputs folder

---

## Technologies Used

- Python
- CSV Processing
- JSON Configuration
- File Handling
- Pathlib
- Modular Programming
- CRM Automation
- Business Process Automation

---

## Project Structure

```text
ai-crm-assistant/

├── main.py
├── config.json
├── customers.csv
├── README.md
├── .gitignore
│
├── modules/
│   ├── customer_analyzer.py
│   ├── followup_generator.py
│   └── report_generator.py
│
└── outputs/
    └── crm_report.txt
```

---

## Workflow

1. Load configuration from `config.json`
2. Read customer data from `customers.csv`
3. Analyze customer status and priority
4. Generate follow-up tasks for no-reply customers
5. Create a centralized CRM report
6. Save the report inside the outputs folder

---

## Example Customer Input

```csv
customer_id,company,status,last_contact_days,priority
1,Acme Corp,new,0,high
2,TechFlow,no_reply,14,medium
3,DataWorks,replied,3,high
4,StartupX,no_reply,7,low
5,Global Systems,new,0,medium
```

---

## Example Console Output

```text
AI CRM Assistant
================

Customers loaded: 5
Acme Corp - new
TechFlow - no_reply
DataWorks - replied
StartupX - no_reply
Global Systems - new

CRM Summary
-----------
Total Customers: 5
New Customers: 2
No Reply Customers: 2
Replied Customers: 1
High Priority Customers: 2

FOLLOW-UP TASKS
---------------
Follow up with TechFlow. No response received yet. Priority: medium.
Follow up with StartupX. No response received yet. Priority: low.

CRM report generated: outputs\crm_report.txt
```

---

## Business Value

Customer relationship management often involves repetitive tracking, follow-ups, and reporting.

This project demonstrates how automation can simplify CRM workflows by analyzing customer data, identifying follow-up opportunities, and generating structured reports automatically.

---

## Future Improvements

- AI-generated personalized follow-up messages
- Lead scoring integration
- Customer segmentation
- CRM dashboard interface
- Email follow-up automation
- Contact history tracking
- Sales pipeline reporting
- Multi-file customer imports
- OpenAI-powered customer insights

---

## Author

Adam Zaki

AI Automation Developer

GitHub:
https://github.com/aiflowsystems

Portfolio:
https://aiflowsystems.github.io/portfolio/