def generateTicket(input_text):
    if "server" in input_text.lower():
        return {
            "issue": "server down",
            "urgency": "high",
            "action": "assign to infra team"
        }
    else:
        return {
            "issue": input_text,
            "urgency": "normal",
            "action": "assign to infra team"
        }

print(generateTicket("Server down!!! pls fix ASAP"))
