def handle(req: str) -> str:
    """handle a request to the function
    Args:
        req (str): request body
    """
    output_string = 'Hi there, you said: ' + req
    return output_string
