import urllib.request

import urllib.request
from io import BytesIO

def fetch_incidents(url, headers={}):
    '''Fetches an incident PDF from a specified URL using the Python urllib.request library.
    
    Args:
        url (str): The URL string of the incident PDF to fetch.
        headers (dict, optional): Additional HTTP headers to include in the request. Defaults to an empty dictionary.
        
    Returns:
        BytesIO: A BytesIO object containing the contents of the fetched incident PDF.
        
    Raises:
        urllib.error.HTTPError: If an HTTP error occurs while fetching the PDF.
        
    Example:
        pdf_bytes = fetch_incidents("https://example.com/incident.pdf")
    '''
    
    # Set headers
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"     
    
    try:
        # Open the URL and return the file object
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as response:
            # Read the content of the response into BytesIO
            file_object = BytesIO(response.read())

    except urllib.error.HTTPError as e:
        print(f"Failed to download file: {e}")

    return file_object                                                     