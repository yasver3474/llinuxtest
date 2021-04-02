# import json
# import boto3
# sqs = boto3.client('sqs')
# def lambda_handler(event, context):
#     # TODO implement
#     print(event)
#     try:
#         sqs.delete_message(
#         QueueUrl = 'https://sqs.us-east-2.amazonaws.com/763998929332/lambda-test-queue',
#         ReceiptHandle = event['Records'][0]['receiptHandle']
#         )
#     except Exception as error:
#         print(error)
#     else:
#         print("Execution complete, message deleted")

#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }






# {'Records': [{'messageId': '96357365-ba3f-40a9-8bf7-750b4a339e9d', 'receiptHandle': 'AQEBsZ5iaY4dyfMWcbBy1UaIGQ+1lKKYFjP/Ko70kybEjVODkkSDzNaclk5F+Ys6uyuJzapL9AU9Pnkb7vI7RZVhYi7vz7JEHI3eFyIzJ4vvBEZC8Bv/oXXt3mBi8Bz+T2b99L8PHXf85npqht+WlA2+qV69fKWOWiADCGWVxCEsyUwqHntUcIBcT/vXquxbPiN/GOMDeojTJFsfSwK/A6cJJrUTanylfjd7mmsgmYZypNNhUBgm8IC15UPeT1dbs2N6x0B3qQYAwja0XNfd2AmV++48btkYxlQH0yBzapg9SPkdbQH4xYyXjh2+C9vO3jOvbXEaKQmdskOsxxvXloV2Pb8J4c+cGbVSz/kgcsWXBca0HiVx7vRnxhyKHWGZUvNmOg0+ckoByMoCMWMnBPQeOQ==', 'body': 'This is a test message for our lambda function', 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1614342533808', 'SenderId': 'AIDA3DYPCQG2NKR365DCW', 'ApproximateFirstReceiveTimestamp': '1614342533813'}, 'messageAttributes': {}, 'md5OfMessageAttributes': None, 'md5OfBody': '67aff1f37c174ce45c379ecec54231d3', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-2:763998929332:lambda-test-queue', 'awsRegion': 'us-east-2'}]}




def test():
    return 1,0,1


a,b,c = test()
print(a,b,c)