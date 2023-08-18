# Example AWS Lambda function + SNS

## Setup

1. Clone this repo
2. Create a Amazon Simple Notification Service (SNS) topic
3. Copy that topic's ARN into `notification/app.py` for line `snsArn = '[SNS-ARN]'`
4. Verify the email address from step 2
4. Run `sam build`
5. Test locally with `sam local invoke -e events/event.json`
6. Run `sam deploy --guided`

Notes:
- Make sure you have the AWS CLI installed and configured
- Make sure the Lambda IAM role has the AWS managed policy AmazonSNSFullAccess