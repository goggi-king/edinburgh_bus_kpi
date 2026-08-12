import os
import requests
import json
import csv
from datetime import datetime, timezone
 
 
# ============================================================
# API SETTINGS
# ============================================================
 
api_key = os.environ["BUS_API_KEY"]
 
headers = {
    "Ocp-Apim-Subscription-Key": api_key
}
 
 
# ============================================================
# STOP
# ============================================================
 
atco = "6200206875"
 
 
# ============================================================
# API REQUEST
# ============================================================
 
url = (
    "https://apim-public.trapezegroupazure.co.uk/"
    "edinburgh-cec-openapi/generic/v1.1/"
    "stops/StopEvents"
)
 
params = {
    "atcoCode": atco
}
 
 
response = requests.get(
    url,
    headers=headers,
    params=params,
    timeout=30
)
 
 
print("ATCO:", atco)
print("Status:", response.status_code)
 
 
# ============================================================
# SAVE OBSERVATION
# ============================================================
 
if response.status_code == 200:
 
    data = response.json()
 
    observed_at = datetime.now(timezone.utc).isoformat()
 
    row = {
        "observed_at": observed_at,
        "atco_code": atco,
        "stop_name": data.get("name"),
        "number_of_events": len(data.get("events", [])),
        "raw_data": json.dumps(data)
    }
 
    with open("bus_observations.csv", "a", newline="") as file:
 
        writer = csv.DictWriter(
            file,
            fieldnames=row.keys()
        )
 
        if file.tell() == 0:
            writer.writeheader()
 
        writer.writerow(row)
 
    print("Observation saved")
 
else:
 
    print("API request failed")
    print(response.text)
 
