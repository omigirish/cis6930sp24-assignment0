import urllib.request
import os

def fetchincidents(url, headers={}):
    '''The function fetchincidents(url) takes a URL string and uses the Python urllib.request library to grab one incident pdf for the Norman Police Report Webpage.'''
    
    # Set headers
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"     
    
    # File path for storing file name
    fileName = "./resources/downloads/"+ url.split("/")[-1]                     
    
    # If file is not already download the file
    if not os.path.exists(fileName):
        # print(f"Downloading {url.split('/')[-1]}......")
        urllib.request.urlretrieve(url,fileName)
    else:
        # print(f"File already downloaded at ./{fileName}")
        pass
    
    return fileName
                                                                  