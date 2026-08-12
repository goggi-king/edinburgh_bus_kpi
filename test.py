import os
from datetime import datetime, timezone
 
from supabase import create_client
 
print("Starting Supabase test...")
 
url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
 
supabase = create_client(url, key)
 
print("Connected to Supabase")
 
result = supabase.table("bus_observations").insert({
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "atco_code": "TEST",
    "stop_name": "Test",
    "raw_data": {
        "hello": "world"
    }
}).execute()
 
print("SUCCESS!")
print(result.data)
