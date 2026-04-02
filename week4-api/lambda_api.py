def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}
    name = params.get("name", "stranger")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": f"Hello {name}, your API works!"
    }