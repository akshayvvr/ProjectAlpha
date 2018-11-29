import json
import datetime


def handler(event, context):
    name=input("Enter your name: ")
    data = {
        'output': 'Hello World',
        'name': f'Hello, {name}',
        'timestamp': datetime.datetime.utcnow().isoformat()
        
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
