import azure.functions as func
import json, datetime
from azure.storage.blob import BlobServiceClient
from azure.cosmos import CosmosClient

def main(mytimer: func.TimerRequest) -> None:
    cosmos = CosmosClient(url, key) # add the url and Key here
    container = cosmos.get_database_client('billing').get_container_client('records')

    blob_service = BlobServiceClient.from_connection_string(blob_conn_str) # blob connection string to be placed here
    container_client = blob_service.get_container_client('archived-billing')

    cutoff = (datetime.datetime.utcnow() - datetime.timedelta(days=90)).isoformat()
    records = container.query_items(
        query="SELECT * FROM records r WHERE r.date < @cutoff",
        parameters=[{"name": "@cutoff", "value": cutoff}],
        enable_cross_partition_query=True
    )

    for record in records:
        blob_name = f"billing/archive/{record['id']}.json"
        container_client.upload_blob(blob_name, json.dumps(record))
        container.delete_item(record, partition_key=record['partitionKey'])