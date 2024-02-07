from pypdf import PdfReader
from assignment0.Incident import IncidentReport
import re 

exclude_strings = ["Date / Time Incident Number Location Nature Incident ORI", "Daily Incident Summary (Public)"]

def insertIncident(line):       
    '''Inserts an incident into an IncidentReport object based on the provided line.
    
    Args:
        line (str): The line containing information about the incident.
        
    Returns:
        IncidentReport or None: An IncidentReport object representing the incident if successful, otherwise None.
    '''
    
    if line not in exclude_strings:

        i,j= (0,0)

        match = re.search(IncidentReport.rexpressions["date_time"], line)
        if match:
            date_time = match.group().strip()

        match = re.search(IncidentReport.rexpressions["incident_number"], line)
        if match:
            incident_number = match.group().strip()
            i=match.end()

        match = re.search(IncidentReport.rexpressions["ori"], line)
        if match:
            ori = match.group().strip()
            j=match.start()

        match = re.match(IncidentReport.rexpressions["location"], line[i:j])

        try:
            if i+1==j:
                incident = IncidentReport(date_time,incident_number,"","",ori)
                
            else:
                if match:
                    location = match.group(1).strip() if match.group(1).strip() else ""
                    nature = match.group(2).strip() if match.group(2).strip() else ""


                    keyword = location.split(" ")[-1]
                    if keyword in ["MVA", "COP", "DDACTS", "911","EMS","RAMPMVA"]:
                        if not keyword == "RAMPMVA":
                            nature = keyword + " " + nature
                            location = ' '.join(location.split()[:-1])
                        else:
                            nature = "MVA " + nature
                            location = ' '.join(location.split()[:-1]) + " RAMP"
                        
                    k=0
                    for c in nature:
                        if not (ord(c) >= 65 and ord(c)<=90):
                            break
                        k+=1

                    if ord(nature[k])!=32 and k!=0:
                        location = location + nature[:k-1]
                        nature = nature[k-1:]

                incident = IncidentReport(date_time,incident_number,location,nature,ori)
                
        except UnboundLocalError as e:
            return None

        return incident

def extractincidents(file):

    try:
        reader = PdfReader(file)

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return []

    incidents=list()
    for page in reader.pages:
        page_text = page.extract_text()
        page_text=page_text.replace("NORMAN POLICE DEPARTMENT", "")
        page_text = page_text.replace('Date / Time Incident Number Location Nature Incident ORI', '') 
        page_text = page_text.replace('Daily Incident Summary (Public)', '')

        page_text = page_text.replace("\n"," ")
        # page_text=page_text.replace("NORMAN POLICE DEPARTMENT\n", "")
        lines = re.findall(r'(\d{1,2}/\d{1,2}/\d{4}.*?)(?=\d{1,2}/\d{1,2}/\d{4}|$)',page_text)
                           
        for line in lines:
            i = insertIncident(line.strip())
            if i:
                incidents.append(i)

    return incidents