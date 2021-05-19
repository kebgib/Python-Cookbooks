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
