# A little handler script for analyzed data. If the data is deemed invalid it is deleted from disk
import sys
import json
import os

if len(sys.argv) < 2:
    print("Usage: python test.py JSONFILE")
    sys.exit(1)



json_file = sys.argv[1]

with open(json_file, 'r') as f:

    data = json.load(f)

    if data.get("product") is None:

        print("Off to the trash.")
        os.remove(json_file)
        os.remove(json_file.split("-analysis")[0])
        
    else:
        print("The AI has deemed you worthy.")


