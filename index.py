import json
import datetime


def handler(event, context):
    try:
        print(event['requestContext']['identity']['userArn'])
        caller_name=event['requestContext']['identity']['userArn']
        split_name=caller_name.split("/")
        greet_name=split_name[-1]
    except:
        print(event)
        greet_name='User'
    greet= 'Hello, '+ greet_name
    data = {
        'output': 'Hello World',
        'name': greet_name,
        'timestamp': datetime.datetime.utcnow().isoformat()
        
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

