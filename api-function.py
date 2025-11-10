    # lambda_function.py
    import json
    import requests # Example dependency

    def lambda_handler(event, context):
        try:
            response = requests.get('https://regres.in/api/users?page=2')
            data = response.json()
            return {
                'statusCode': 200,
                'body': json.dumps(data)
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error: {str(e)}')
            }
