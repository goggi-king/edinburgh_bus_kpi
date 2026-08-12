import os
from datetime import datetime, timezone
 
from supabase import create_client
 
 
print("Starting Supabase test...")
 
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
 
if not url:
    raise Exception("SUPABASE_URL is missing")
 
if not key:
    raise Exception("SUPABASE_KEY is missing")
 
print("Supabase URL found")
print("Supabase key found")
 
supabase = create_client(url, key)
 
print("Connected to Supabase")
 
data = {
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "atco_code": "TEST",
    "stop_name": "Test",
    "raw_data": {
        "hello": "world"
    }
}
 
print("Attempting to insert test record...")
 
result = (
    supabase
    .table("bus_observations")
    .insert(data)
    .execute()
)
 
print("SUCCESS!")
print(result.data)
