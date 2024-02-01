# -*- coding: utf-8 -*-
# Example main.py
import argparse

import assignment0

def main(url):
    ''' Calling the main function should download data insert it into a database and print a summary of the incidents.'''
    # Download data
    incident_data = assignment0.fetchincidents(url)

    # Extract data
    incidents = assignment0.extractincidents(incident_data)
	
    # Create new database
    db = assignment0.createdb()
	
    # Insert data
    assignment0.populatedb(db, incidents)
	
    # Print incident counts
    assignment0.status(db)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)