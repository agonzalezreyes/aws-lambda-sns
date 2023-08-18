import json
import boto3

def lambda_handler(event, context):
    first_name = event['first_name']
    last_name = event['last_name']

    client = boto3.client('sns')
    snsArn = '[SNS-ARN-HERE]'
    message = "This is a test notification from AWS Lambda + SNS."
    
    response = client.publish(
        TargetArn=snsArn,
        Message=message,
        Subject='Test Notification for ' + first_name + ' ' + last_name,
    )
    # print(response)
    return response