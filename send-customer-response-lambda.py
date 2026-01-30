import boto3
import json

ses = boto3.client("ses", region_name="eu-north-1")

SENDER_EMAIL = "mynameislalit456@gmail.com"  # 🔧 SES verified email

def lambda_handler(event, context):
    print("FULL EVENT RECEIVED:")
    print(json.dumps(event, indent=2))

    # Customer email
    email = event.get("email")

    # Handle Step Functions nested structure safely
    auto_response = (
        event.get("autoResponse", {})
             .get("autoResponse", {})
             .get("customerResponse")
    )

    ticket_id = event.get("storeResult", {}).get("ticket_id", "NA")

    if not email:
        raise ValueError("Missing customer email")

    if not auto_response:
        raise ValueError("Missing autoResponse.customerResponse")

    subject = f"We received your support request (Ticket {ticket_id})"

    body_text = f"""
Hello,

{auto_response}

Ticket ID: {ticket_id}

This is an automated acknowledgment. Our support team will follow up if required.

Regards,
Support Team
"""

    ses.send_email(
        Source=SENDER_EMAIL,
        Destination={
            "ToAddresses": [email]
        },
        Message={
            "Subject": {"Data": subject},
            "Body": {
                "Text": {"Data": body_text}
            }
        }
    )

    return {
        "customerEmailStatus": "SENT",
        "sentTo": email,
        "ticket_id": ticket_id
    }
