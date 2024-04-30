import os
import time
import requests
import json
import timeago
from datetime import datetime
from vessel_types import vessel_types
from vessel_flags import vessel_flags

API_KEY = os.environ.get('AISHUB_API_KEY')
if not API_KEY:
    raise Exception("No API key found, set AISHUB_API_KEY environment variable")

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']
if not SLACK_WEBHOOK_URL:
    raise Exception("No Slack webhook URL found, set SLACK_WEBHOOK_URL environment variable")

BOUNDING_BOX = (51.425531, -0.382048, 51.529024, 0.039552)

KNOWN_VESSELS_FILE = 'thames-london.json'

TIMEOUT = 60*60*24*30*3 # three months, to avoid vessels that just come out once every week or two

try:
    with open(KNOWN_VESSELS_FILE, 'r') as file:
        known_vessels = json.load(file)
except:
    known_vessels = {}

def get_last_seen(vessel_id):
    return known_vessels.get(vessel_id, None)

def update_last_seen(vessel_id):
    now = datetime.utcnow().isoformat()
    known_vessels[vessel_id] = now

def get_vessels_in_area():
    url = f"https://data.aishub.net/ws.php?username={API_KEY}&format=1&output=json&latmin={BOUNDING_BOX[0]}&lonmin={BOUNDING_BOX[1]}&latmax={BOUNDING_BOX[2]}&lonmax={BOUNDING_BOX[3]}"
    response = requests.get(url)

    if response.status_code == 200:
        parsed_response = response.json()
        if parsed_response[0]["ERROR"]:  
            raise Exception(f"Error getting vessels: {parsed_response[0]['ERROR_MESSAGE']}")
        else: 
            return parsed_response[1]
    else:
        return []

current_time = time.time()

current_vessels = get_vessels_in_area()
new_or_returning_vessels = []

for vessel in current_vessels:
    mmsi = str(vessel['MMSI'])
    last_seen = get_last_seen(mmsi)
    
    vessel['last_seen'] = last_seen

    print(f"Vessel {vessel['MMSI']} last seen {vessel['last_seen']}")

    # If the vessel hasn't been seen before or if it was seen a long time ago
    if not last_seen or (current_time - time.mktime(datetime.strptime(last_seen, "%Y-%m-%dT%H:%M:%S.%f").timetuple())) > TIMEOUT:
        print(f"New or timed out vessel. Full data: {vessel}")
        new_or_returning_vessels.append(vessel)

    update_last_seen(mmsi)

with open(KNOWN_VESSELS_FILE, 'w') as file:
    json.dump(known_vessels, file, sort_keys=True, indent=2)

# temporary slack channel for testing, normal channel is baked in the webhook
# channel = '#test-vessel-tracker'

if new_or_returning_vessels:
    message = 'New vessels in the area:\n'

    for vessel in new_or_returning_vessels:
        message += f"<https://www.vesselfinder.com/?mmsi={vessel['MMSI']}|{vessel['MMSI']} - {vessel.get('NAME', '(No name)')}> "
        type = vessel.get('TYPE', None)
        
        vessel_mid = int(str(vessel['MMSI'])[:3])

        if vessel_mid in vessel_flags.keys():
            message += f" {vessel_flags[vessel_mid]} "

        if type in vessel_types.keys():
            message += f"({vessel_types[type]}) "

        if vessel["IMO"]:
            message += f"(IMO: {vessel['IMO']}) "

        if vessel["DEST"]:
            message += f"(Destination: {vessel['DEST']}) "

        if vessel['last_seen']:
            message += f"Last seen {timeago.format(datetime.fromisoformat(vessel['last_seen']), current_time)}\n"
        else:
            message += "Never seen before\n"

    # Prepare the payload
    payload = {
#        'channel': channel,
        'text': message,
    }

    # Send a POST request to the webhook URL
    response = requests.post(
        SLACK_WEBHOOK_URL,
        headers={'Content-Type': 'application/json'},
        data=json.dumps(payload),
    )

    # Check for errors
    if response.status_code != 200:
        raise ValueError(
            f'Request to slack returned an error {response.status_code}, '
            f'the response is:\n{response.text}'
    )
