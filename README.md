# cis6930sp24-assignment0
CIS 6930 - Data Engineering Assignement 0 : Extract Data about incidents from NormanPD

Name: Girish Vinayak Salunke

## Assignment Description
The assignment involves developing a data engineering solution to extract incident data from the Norman Police Department website. The process includes downloading incident reports, extracting relevant information from PDF files, and storing the data in a SQLite database.

## How to install
Install pip and the then install pipenv
```
pip install pipenv
```

## How to run
Switch to the project directory in terminal and run the following command:
``` bash
pipenv run python assignment0/main.py --incidents <pdf_url>
```

Example Command:
``` bash
pipenv run python assignment0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-25_daily_incident_summary.pdf
```

## Running Test Cases
```bash

https://github.com/omigirish/cis6930sp24-assignment0/assets/56110537/b36bd60a-069c-461e-94dd-47d16953c274


pipenv run pytest
```

## Project Demo

https://github.com/omigirish/cis6930sp24-assignment0/assets/56110537/76647291-ba5c-413e-8d30-5233824f4899

## Project Directory Structure
```bash
.
├── COLLABORATORS.md
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── assignment0
│   ├── Incident.py
│   ├── db.py
│   ├── extractincidents.py
│   ├── fetchincidents.py
│   └── main.py
├── docs
├── resources
│   ├── downloads
│   └── normanpd.db
├── setup.cfg
├── setup.py
└── tests
    ├── test_Incident.py
    ├── test_db.py
    ├── test_extractincidents.py
    └── test_fetchincidents.py
```

## Functions
#### main.py 
Calling the main function should download data insert it into a database and print a summary of the incidents.

### fetchincidents.py

```
def fetch_incidents(url, headers={}):

    Fetches an incident PDF from a specified URL using the Python urllib.request library.

    Args:
        url (str): The URL string of the incident PDF to fetch.
        headers (dict, optional): Additional HTTP headers to include in the request. Defaults to an empty dictionary.
        
    Returns:
        BytesIO: A BytesIO object containing the contents of the fetched incident PDF.
        
    Raises:
        urllib.error.HTTPError: If an HTTP error occurs while fetching the PDF.
        
    Example:
        pdf_bytes = fetch_incidents("https://example.com/incident.pdf")

```

### extractincidents.py
```
def insertIncident(line):

    Inserts an incident into an IncidentReport object based on the provided line.
    
    Args:
        line (str): The line containing information about the incident.
        
    Returns:
        IncidentReport or None: An IncidentReport object representing the incident if successful, otherwise None.
 ```
 ```   
def extractincidents(file):

    Extracts incidents from a PDF file and returns a list of IncidentReport objects.
    
    Args:
        file (str): The path to the PDF file containing incident reports.
        
    Returns:
        list: A list of IncidentReport objects representing the extracted incidents.
```

### db.py
```
def createdb():

    Creates a new SQLite database file and a table for storing incident data if the file does not exist.
    
    Returns:
        sqlite3.Connection: A connection object to the newly created database.
```
```
def populatedb(db, incidents):

    Populates the SQLite database with incident data.
    
    Args:
        db (sqlite3.Connection): A connection object to the SQLite database.
        incidents (list): A list of IncidentReport objects to be inserted into the database.  
```

```
def status(db):

    Prints a summary of incident data grouped by nature and sorted by count.
    
    Args:
        db (sqlite3.Connection): A connection object to the SQLite database.    
```
```
def disconnectdb(conn):

    Closes the connection to the SQLite database.
    
    Args:
        conn (sqlite3.Connection): A connection object to the SQLite database.
    
```

## Database Development

In this project, database development is pivotal in managing incident data effectively. Utilizing SQL queries, we establish a SQLite database specifically designed for incident reports. The createdb() function employs SQL to craft the database schema, defining a table structure to encompass key incident attributes such as date/time, incident number, location, nature, and Originating Agency Identifier (ORI). These SQL statements ensure the data's structured organization, aligning with project requirements.

```sql

CREATE TABLE IF NOT EXISTS 
incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT
    );

```

Subsequently, the populatedb() function leverages SQL INSERT statements to populate the database with incident data extracted from PDF files. By utilizing SQL's robust capabilities, multiple records are efficiently inserted into the database, facilitating seamless data storage and retrieval. This process enables the project to centralize a significant volume of incident data, laying the foundation for accessible retrieval and analysis.

```sql

INSERT INTO incidents (incident_time, incident_number, incident_location, nature, incident_ori)
    VALUES (?, ?, ?, ?, ?);

```

Moreover, the status() function demonstrates the project's SQL querying capabilities, providing insightful summaries such as incident counts grouped by nature. By harnessing SQL's power, developers can extract valuable insights from the database, enabling informed decision-making and analysis.

```sql

SELECT nature, COUNT(*)
    FROM incidents
    GROUP BY nature
    ORDER BY COUNT(*) DESC, nature ASC;

```

SQLite emerges as the database engine of choice for this project due to its lightweight nature and self-contained design. It offers simplicity without compromising robustness, making it an optimal solution for managing incident data without the complexities associated with server-based database systems. Ultimately, through the integration of SQL queries and SQLite, database development empowers developers to construct efficient and scalable solutions for incident reporting and analysis


## Bugs and Assumptions

### Assumptions

1. The format of the pdf files is the same, No changes are done in the formatting of the pdf on any of the pages. 

2. The sequence of the columns in the table is also the same.

3. All characters in the Location column are alphanumeric (including puncuation marks like ,;"'-) and all alphabets in location column are capital.

4. ORIs have a fixed format.

5. Date format is fixed (mm/dd/yyyy hh:mm)

6. Besides the words ["MVA", "COP", "DDACTS", "911","EMS","RAMPMVA"], all other string in nature column start with a capital letter followed by only lower case characters.

### Bugs
1. The program might give incorrect answers if the nature column contains a word in which all characters are capitalized. 

2. The program might give error if pdfs have non standard formatting. One such case migth occur when the location column has very long multi line address. (Although the program is tested and works fine for 2 line addresses).

3. If an address ends in 911, then the string 911 is stripped from the address column and added to the nature column.
