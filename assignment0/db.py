import sqlite3
import os
def createdb():
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
    conn.close()