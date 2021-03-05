  
import json
import requests

def lambda_handler(event, context):
  print('Loading function')
  return {
      'statusCode': 200,
      'body': "{}".format(
          "Lambda function built and deployed by TeamCity & Octopus"
      )
  }
