import requests

def is_valid_m3u8(link: str, timeout: int = 5, secure: bool = False) -> bool:
    """
    Validates if the given link is a valid m3u8 URL.
    
    Args:
        link (str): The URL to validate.
        timeout (int): Timeout for the request in seconds. Default is 5.
        secure (bool): Ensures the URL is HTTPS if set to True. Default is False.
        
    Returns:
        bool: True if the link is a valid m3u8 file; otherwise, False.
    """
    
    # Check if link is non-empty and starts with "http" (either http or https)
    if not link or not link.startswith("http"):
        return False

    # Ensure link is HTTPS if the secure parameter is set
    if secure and not link.startswith("https"):
        return False

    try:
        # Make a request to the link with the specified timeout
        response = requests.get(link, timeout=timeout)
        response.raise_for_status()  # Raise an error for unsuccessful status codes
        
        # Check if the response text starts with the m3u8 header identifier
        return response.text.startswith("#EXTM3U")
        
    except requests.exceptions.RequestException as e:
        # Log the exception and return False if any request-related error occurs
        print(f"Request exception Error: {e}")
        return False
