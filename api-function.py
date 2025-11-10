    # lambda_function.py
import json
import requests # Example dependency

def lambda_handler(event, context):
        try:
            response = requests.get('https://regres.in/api/users?page=2')
            return {
                'statusCode': response.status_code,
                'body': response.text[:500]
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error: {str(e)}')
            }
