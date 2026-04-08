import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
table = dynamodb.Table('messages')

def lambda_handler(event, context):

    params = event.get("queryStringParameters") or {}
    action = params.get("action")

    if action == "add":
        text = params.get("text", "empty")

        item = {
            "id": str(uuid.uuid4()),
            "text": text
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/plain"},
            "body": f"Stored message: {text}"
        }

    elif action == "get":
        response = table.scan()

        messages = [item["text"] for item in response.get("Items", [])]

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(messages)
        }

    else:
        return {
            "statusCode": 200,
            "body": "Use ?action=add&text=... or ?action=get"
        }