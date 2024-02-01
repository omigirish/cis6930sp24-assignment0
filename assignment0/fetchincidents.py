import urllib

defaulturl = "https://www.normanok.gov/sites/default/files/documents/""2024-01/2024-01-01_daily_incident_summary.pdf"

def fetchincidents(url=defaulturl, headers={}):
    '''The function fetchincidents(url) takes a URL string and uses the Python urllib.request library to grab one incident pdf for the Norman Police Report Webpage.'''
    
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          
    
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()                                                                    