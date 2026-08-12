import os
from datetime import datetime, timezone
 
from supabase import create_client
 
 
supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_KEY"]
)
 
 
result = supabase.table("bus_observations").insert({
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "atco_code": "TEST",
    "stop_name": "Test",
    "raw_data": {
        "hello": "world"
    }
}).execute()
 
 
print(result.data)
