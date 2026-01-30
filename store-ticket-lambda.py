import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = "support-tickets"   # 🔧 change if needed
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    ticket_id = str(uuid.uuid4())

    item = {
        "ticket_id": ticket_id,
        "email": event["email"],
        "feedback": event["feedback"],
        "summary": event["analysisResult"]["summary"],
        "sentiment": event["analysisResult"]["sentiment"],
        "urgency": event["analysisResult"]["urgency"],
        "created_at": datetime.utcnow().isoformat()
    }

    table.put_item(Item=item)

    event["storeResult"] = {
        "ticket_id": ticket_id
    }

    return event
