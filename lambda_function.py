  
import json
import requests
import awswrangler

def lambda_handler(event, context):
  print('Loading function')
  return {
      'statusCode': 200,
      'body': "{}".format(
          response.text
      )
  }
