def analyze_customers(customers):
    total_customers = len(customers)
    new_customers = 0
    no_reply_customers = 0
    replied_customers = 0
    high_priority_customers = 0

    for customer in customers:
        status = customer["status"]
        priority = customer["priority"]

        if status == "new":
            new_customers += 1
        elif status == "no_reply":
            no_reply_customers += 1
        elif status == "replied":
            replied_customers += 1

        if priority == "high":
            high_priority_customers += 1

    return {
        "total_customers": total_customers,
        "new_customers": new_customers,
        "no_reply_customers": no_reply_customers,
        "replied_customers": replied_customers,
        "high_priority_customers": high_priority_customers
    }