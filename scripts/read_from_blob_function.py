from azure.storage.blob import BlobServiceClient
import json

def get_archived_billing_record(record_id):
    blob_service = BlobServiceClient.from_connection_string(blob_conn_str) # blob connection string to be placed here
    blob_client = blob_service.get_blob_client(container='archived-billing', blob=f"billing/archive/{record_id}.json")
    data = blob_client.download_blob().readall()
    return json.loads(data)