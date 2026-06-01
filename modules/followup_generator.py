def generate_followups(customers):
    followups = []

    for customer in customers:
        company = customer["company"]
        status = customer["status"]
        priority = customer["priority"]

        if status == "no_reply":
            message = (
                f"Follow up with {company}. "
                f"No response received yet. "
                f"Priority: {priority}."
            )

            followups.append(message)

    return followups