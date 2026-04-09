import json
from datetime import timedelta

json_file = open('/home/devasc/labs/devnet-src/parsing/myfile.json', 'r')

ourjson = json.load(json_file)

json_file.close()

print(f"Token: {ourjson['access_token']}")

time_remaining = timedelta(seconds=ourjson['expires_in'])
print(f"Tiempo restante: {time_remaining}")
