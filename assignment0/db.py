import sqlite3
import os
def createdb():

    '''
    Creates a new SQLite database file and a table for storing incident data if the file does not exist.
    
    Returns:
        sqlite3.Connection: A connection object to the newly created database.

    '''

    if os.path.exists("./resources/normanpd.db"):
        os.remove("./resources/normanpd.db")

    conn = sqlite3.connect("./resources/normanpd.db")
    curr = conn.cursor()
    curr.execute("""
                CREATE TABLE IF NOT EXISTS incidents (
                incident_time TEXT,
                incident_number TEXT,
                incident_location TEXT,
                nature TEXT,
                incident_ori TEXT
                );
                """);
    conn.commit()
    curr.close()

    return conn

def populatedb(db, incidents):

    '''
    Populates the SQLite database with incident data.
    
    Args:
        db (sqlite3.Connection): A connection object to the SQLite database.
        incidents (list): A list of IncidentReport objects to be inserted into the database.
    
    '''

    curr = db.cursor()
    data_to_insert = [(incident.date_time, incident.incident_number, incident.location, incident.nature, incident.ori)
                  for incident in incidents]

    curr.executemany("""
                INSERT INTO incidents (incident_time, incident_number, incident_location, nature, incident_ori)
                VALUES (?, ?, ?, ?, ?);
                 """,data_to_insert)
    db.commit()
    curr.close()

def status(db):

    '''
    
    Prints a summary of incident data grouped by nature and sorted by count.
    
    Args:
        db (sqlite3.Connection): A connection object to the SQLite database.

    '''

    curr = db.cursor()
    data =  curr.execute("""
                SELECT nature, COUNT(*)
                FROM incidents
                GROUP BY nature
                ORDER BY COUNT(*) DESC, nature ASC;
                """)
    
    for (nature, count) in data:
        print(f"{nature}|{count}")       

    curr.close()

def disconnectdb(conn):
    '''
    Closes the connection to the SQLite database.
    
    Args:
        conn (sqlite3.Connection): A connection object to the SQLite database.
        
    '''

    conn.close()