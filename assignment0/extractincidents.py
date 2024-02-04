from pypdf import PdfReader
from Incident import IncidentReport
import re 

exclude_strings = ["Date / Time Incident Number Location Nature Incident ORI", "Daily Incident Summary (Public)"]

def insertIncident(line):       
    if line not in exclude_strings:

        x = line.find("NORMAN POLICE DEPARTMENT")

        if x>0:
            line= line[:x]

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

        if match:
            location = match.group(1).strip()
            nature = match.group(2).strip()

        try: 
            incident = IncidentReport(date_time,incident_number,location,nature,ori)
            with open("output.csv","a") as of:
                of.write(f"{date_time},{incident_number},{location},{nature},{ori}\n")
            
        
        except UnboundLocalError as e:
            with open("output.csv","a") as of:
                of.write(f"{line}\n")
            return None

        return incident

def extractincidents(file):
    with open("output.csv","a") as of:
        of.write(f"date_time,incident_number,location,location,ori\n")
    reader = PdfReader(file)
    incidents=list()
    for page in reader.pages:
        page_text = page.extract_text() 
        for line in page_text.split("\n"):
            i = insertIncident(line)
            if i:
                incidents.append(i)
    return incidents




