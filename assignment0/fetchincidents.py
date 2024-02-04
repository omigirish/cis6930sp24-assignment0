import urllib.request
import os

import urllib.request
from io import BytesIO

def fetch_incidents(url, headers={}):
    '''The function fetch_incidents(url) takes a URL string and uses the Python urllib.request library
    to grab one incident pdf for the Norman Police Report Webpage.
    '''
    
    # Set headers
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"     
    
    # Open the URL and return the file object
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as response:
        # Read the content of the response into BytesIO
        file_object = BytesIO(response.read())
    
    return file_object

                                                                  