import pytest
from assignment0.fetchincidents import fetch_incidents


def test_fetch_incidents_valid_url():
    url = "https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-03_daily_incident_summary.pdf"  
    file_object = fetch_incidents(url)
    assert file_object is not None
    assert file_object.readable()  # Check if the file object is readable

def test_fetch_incidents_invalid_url():
    url = "https://example.com/invalid_incident.pdf"  
    with pytest.raises(Exception):
        fetch_incidents(url)



