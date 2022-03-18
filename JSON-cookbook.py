"""
These are simple templates for JSON ingestion and file manipulation
Use these to speed data analysis and routine updating of intelligence data
"""

import json
import os
from datetime import datetime

class daytime:      # Custom date and time class for simple console or file usage
    now = datetime.now()
    day = f"{now:%d}"
    month = f"{now:%m}"
    year = f"{now:%y}"
    hour = f"{now:%I}"
    minute = f"{now:%M}"
    second = f"{now:%S}"
    filedate = f"{month}-{day}-{year}"
    filetime = f"{hour}.{minute}"
    realdate = f"{month}/{day}/{year}"
    realtime = f"{hour}:{minute}:{second}"

        
"""
Folder and path operations
"""
# Saving a folder? 
try:
    os.mkdir(f'Results-{daytime.filedate}')   # Make dir
    os.chdir(f'Results-{daytime.filedate}')   # Change to dir
except FileExistsError:
    os.chdir(f'Results-{daytime.filedate}')   # If dir already exists, change to it
# Notifying user of file location is nice 
print(f"[+] Results will be saved in:")
print(f"[+] {os.getcwd()}")


"""
Read/write JSON to a file w/ datetime data within the filename
Using keyword 'with' to open files within a single context for ingestion
"""
# open() kwarg 'w' for write file permissions
with open(f'Scan_Results-{daytime.filedate}-{daytime.filetime}.json', 'w') as json_file:
    # dump contents of my_jason to the file specified above
    json.dump(my_json, json_file, indent=2)

# open() a saved json file and json.load() the contents in to a Dict() type object
with open('my_saved_json_file.json') as json_file:
    json_object = json.load(json_file)

    
    
    
"""
Handling nested JSON with data that cannot be serialized

ex. AWS SDK boto3 returns JSON objects with datetime.datetime objects as values
these objects cannot be serialized to JSON format and will throw an error.

Use the datetimeHandler function and pass it in to json.dumps(data, default=datetimeHandler)
"""
def datetimeHandler(json_object):
    """
    Pass in to json.dumps in order to parse datetime objects to
    isoformat strings -> json.dumps(my_data, default=datetimeHandler, indent=2)
    
    If specified, default should be a function that gets called for objects
    that can’t otherwise be serialized. It should return a JSON encodable
    version of the object or raise a TypeError. If not specified, TypeError is raised.
    """
    # https://docs.python.org/3/library/json.html#json.dump
    if isinstance(json_object, datetime.datetime):
        return json_object.isoformat()
    
    raise TypeError(f"[!] datetimeHandler() exception - unknown data type")

my_json = json.dumps(my_data, default=datetimeHandler, indent=2)
