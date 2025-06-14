# Archive records older than 3 months
from datetime import datetime, timedelta
cutoff_date = datetime.utcnow() - timedelta(days=90)

for record in cosmos_db.query("SELECT * FROM billing WHERE date < @cutoff", {"@cutoff": cutoff_date}):
    blob_path = f"billing/archive/{record['id']}.json"
    azure_blob.upload(blob_path, json.dumps(record))
    cosmos_db.delete(record['id'])