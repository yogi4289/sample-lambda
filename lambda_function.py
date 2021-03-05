  
import json
import requests

def lambda_handler(event, context):
  print('Loading function')
  return {
      'statusCode': 200,
      'body': "{}".format(
          response.text
      )
  }
