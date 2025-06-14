def get_billing_record(record_id):
    record = cosmos_db.get(record_id)
    if record:
        return record
    else:
        blob_path = f"billing/archive/{record_id}.json"
        return azure_blob.download(blob_path)