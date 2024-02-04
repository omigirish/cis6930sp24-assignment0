# -*- coding: utf-8 -*-
# Example main.py
import argparse

from assignment0 import *
from assignment0.db import createdb,populatedb,disconnectdb, status
from assignment0.extractincidents import extractincidents
from assignment0.fetchincidents import fetch_incidents


def main(url):
    """
    Calling the main function should download data insert it into a database and print a summary of the incidents.
    """
    # Download data
    incident_data = fetch_incidents(url)

    # Extract data
    incidents = extractincidents(incident_data)
	
    # Create new database
    db = createdb()
	
    # Insert data
    populatedb(db, incidents)
	
    # Print incident counts
    status(db)

    # Close the connection
    disconnectdb(db)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)