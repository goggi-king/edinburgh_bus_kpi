mport requests
import json
from datetime import datetime, timezone
 
 
# ============================================================
# API SETTINGS
# ============================================================
 
api_key = "0d7efb41a48249cb844296ecc3f3c714"
 
headers = {
    "Ocp-Apim-Subscription-Key": api_key
}
 
 
# ============================================================
# STOP WE ARE COLLECTING
# ============================================================
 
atco = "6200206875"
 
 
# ============================================================
# GET REAL-TIME BUS DATA
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
# SAVE RESPONSE
# ============================================================
 
if response.status_code == 200:
 
    data = response.json()
 
    print("API request successful")
    print("Stop:", data.get("name"))
    print("Number of events:", len(data.get("events", [])))
 
    timestamp = datetime.now(timezone.utc).isoformat()
 
    output = {
        "observed_at": timestamp,
        "atco_code": atco,
        "data": data
    }
 
    with open("bus_data.json", "w") as file:
        json.dump(output, file, indent=2)
 
    print("Data saved to bus_data.json")
 
else:
 
    print("API request failed")
    print(response.text)
