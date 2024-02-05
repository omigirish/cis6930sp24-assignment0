import sqlite3
import pytest
from assignment0.db import createdb,populatedb,disconnectdb, status
from assignment0.Incident import IncidentReport
import os


@pytest.fixture(scope="session")
def test_db():
    db = createdb()
    yield db
    disconnectdb(db)

def test_createdb(): 
    db = createdb()
    assert isinstance(db, sqlite3.Connection)
    disconnectdb(db)

def test_populatedb(test_db):
    incidents = [
        IncidentReport("2022-01-01 12:00", "12345", "Location1", "Nature1", "ORI1"),
        IncidentReport("2022-01-02 15:30", "67890", "Location2", "Nature2", "ORI2"),
    ]
    populatedb(test_db, incidents)

    curr = test_db.cursor()
    data =  curr.execute("""
                SELECT COUNT(*)
                FROM incidents
                """).fetchone()  # Fetch the result from the cursor
    count = data[0]

    assert count == 2

    curr.close()


def test_status(test_db, capsys):
    # Populate the database with test data
    incidents = [
        IncidentReport("2022-01-01 12:00", "12345", "Location1", "Nature1", "ORI1"),
        IncidentReport("2022-01-02 15:30", "67890", "Location2", "Nature2", "ORI2"),
        IncidentReport("2022-01-03 08:45", "54321", "Location3", "Nature1", "ORI1"),
    ]
    populatedb(test_db, incidents)

    # Call the status function and capture the printed output
    status(test_db)
    captured = capsys.readouterr()

    # Add assertions to check if the expected output matches the captured output
    assert "Nature1|3" in captured.out
    assert "Nature2|2" in captured.out

@pytest.fixture(scope="session", autouse=True)
def cleanup_after_tests():
    yield
    # Remove the database file if it exists
    db_file_path = "./resources/normanpd.db"
    if os.path.exists(db_file_path):
        os.remove(db_file_path)


