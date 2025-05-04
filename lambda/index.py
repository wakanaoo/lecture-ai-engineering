import json
import urllib.request

def lambda_handler(event, context):
    # ここに、あなたが Colab で立てた FastAPI の URL を貼り付けてください
    url = "https://e5bc-34-143-186-188.ngrok-free.app/predict"  # ← ここを正しいURLに修正

    try:
        # Lambda に送られてきた JSON から本文を取り出す
        body = json.loads(event['body'])
        message = body['message']  # JSONのキーは 'message' を想定

        input_data = {"text": message}
        req = urllib.request.Request(
            url,
            data=json.dumps(input_data).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        
        with urllib.request.urlopen(req) as res:
            response_body = res.read().decode("utf-8")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": response_body
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }
