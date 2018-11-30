def handle(inp: str) -> str:
    """handle a request to the function
    Args:
        inp (str): request body
    """
    output_string = 'Hi there, you said: ' + inp
    return output_string
