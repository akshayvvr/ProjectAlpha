import json
import datetime
import requests
r = requests.post("https://l82nn2ozrk.execute-api.us-west-2.amazonaws.com/Prod/", data={'name': 'Akshay'})
print(r)

def handler(event, context):
    try:
        print(event)
        print(event['requestContext']['identity']['userArn'])
        caller_name=event['requestContext']['identity']['userArn']
        split_name=caller_name.split("/")
        greet_name=split_name[-1]
    except:
        print("ARN not found")
        print(event)
        greet_name='User'
    
    data = {
        'output': 'Hello World',
        'name': greet_name,
        'timestamp': datetime.datetime.utcnow().isoformat()
        
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

