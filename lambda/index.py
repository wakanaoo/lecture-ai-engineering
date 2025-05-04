# lambda/index.py
import json
import urllib.request

# あなたの FastAPI サーバのエンドポイントに書き換えてください
FASTAPI_URL = "https://fd2e-34-87-136-98.ngrok-free.app/predict"

def lambda_handler(event, context):
    try:
        # リクエストボディを取得
        body = json.loads(event['body'])
        message = body.get('message', '')
        
        # FastAPI に送信するデータを整形
        payload = json.dumps({"text": message}).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        
        # リクエストを作成して送信
        req = urllib.request.Request(FASTAPI_URL, data=payload, headers=headers)
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode("utf-8")
            result = json.loads(response_body)
        
        # FastAPI からの応答を構成
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({
                "success": True,
                "response": result.get("response", "")
            })
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
