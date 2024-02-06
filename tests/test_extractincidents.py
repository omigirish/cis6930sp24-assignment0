
from assignment0.extractincidents import extractincidents, insertIncident
from assignment0.Incident import IncidentReport
from assignment0.fetchincidents import fetch_incidents

def test_insertIncident_valid_line():
    line = "1/3/2024 8:21 2024-00000490 650 N INTERSTATE DR Alarm OK0140200"
    incident = insertIncident(line)
    assert isinstance(incident, IncidentReport)

def test_insertIncident_valid_line2():
    line = "1/20/2024 6:42 2024-00004434W STATE HWY 9 HWY / I35 NB ON RAMP 108A RAMPMotorist Assist OK0140200"
    incident = insertIncident(line)
    assert isinstance(incident, IncidentReport)

def test_insertIncident_invalid_line():
    line = "1/3/2024 8:21 2024-00000490"
    incident = insertIncident(line)
    assert incident is None

def test_extractincidents_valid_file():
    file = fetch_incidents("https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-03_daily_incident_summary.pdf")
    incidents = extractincidents(file)
    assert isinstance(incidents, list)
    assert all(isinstance(incident, IncidentReport) for incident in incidents)

def test_extractincidents_invalid_file():
    file = "invalid_test_file.pdf"  
    incidents = extractincidents(file)
    assert incidents == []

