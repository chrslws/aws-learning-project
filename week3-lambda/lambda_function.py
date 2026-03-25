def lambda_handler(event, context):
    name = event.get("name", "stranger")

    return {
        "statusCode": 200,
        "body": f"Hello {name}, your Lambda function works!!"
    }