
def lambda_handler(event, context):
    """
    This function is a basic AWS Lambda handler that returns a simple JSON response.

    Args:
        event (dict): The event dictionary passed to the Lambda function.
        context (object): The context object passed to the Lambda function.

    Returns:
        dict: A dictionary containing the HTTP status code (200) and a JSON body with the message "Hello from CIDC Lambda".
    """
    return {
        'statusCode': 200,  # Indicate successful execution
        'body': json.dumps("Hello from CIDC updated Lambda")  # Serialize the message as JSON
    }

