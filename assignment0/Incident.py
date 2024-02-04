class IncidentReport:

    rexpressions={
                "date_time": r'\b(?:1[0-2]|0?[1-9])\/(?:3[01]|[12][0-9]|0?[1-9])\/\d{4} (?:2[0-3]|[01]?[0-9]):(?:[0-5]?[0-9])\b',
                "ori": "|"
                .join([
                    r'[A-Z]{2}[0-9A-Z]{7}$',  # Standard ORI pattern
                    r'\b\d{5}\b$',  # Numeric-only codes, e.g., '14005'
                    r'\b[A-Z]{7}\b$'  # Letter-only codes, e.g., 'EMSSTAT'
                ]),
                "incident_number": r'\d{4}-\d{8}',
                # "location": r"^([\d\sA-Z\/'-,<>.;]+|(?:\d+\.\d+;\-\d+\.\d+))\s(.+)$",
                # "location": r"^([\d\sA-Z\/'-<>.;]+|(?:\d+\.\d+;\-\d+\.\d+))\s(.+)$"
                "location": r"^([\d\sA-Z\/',-<>.;]+|(?:\d+\.\d+;\-\d+\.\d+))\s(.+)$"

            }
    
    def __init__(self, date_time, incident_number, location, nature, ori):
        """
        Initializes a new instance of the IncidentReport class.

        :param date_time: The date and time of the incident.
        :param incident_number: The unique number assigned to the incident.
        :param location: The location where the incident occurred.
        :param nature: The nature of the incident.
        :param ori: The Originating Agency Identifier.
        """
        self.date_time = date_time
        self.incident_number = incident_number
        self.location = location
        self.nature = nature
        self.ori = ori
    

    def __str__(self):
        """
        Returns a string representation of the IncidentReport instance.
        """
        return f"Incident Report:\nDate/Time: {self.date_time}\nIncident Number: {self.incident_number}\nLocation: {self.location}\nNature: {self.nature}\nORI: {self.ori}"
