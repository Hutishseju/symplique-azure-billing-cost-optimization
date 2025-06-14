# symplique-azure-billing-cost-optimization
Symplique Solutions azure-billing-cost-optimization Assignment

# Azure Billing Cost Optimization

## Objective
Optimize Azure Cosmos DB storage costs by archiving older billing records while maintaining access and existing API behavior.

## Architecture
Refer to `/architecture/diagram.png`

## Tech Stack
- Azure Cosmos DB
- Azure Blob Storage
- Azure Functions (Python)
- Bicep (Infra as Code)

## Folder Structure
azure-billing-cost-optimization/
├── README.md
├── architecture/
│   └── diagram.png
├── pseudocode/
│   ├── data_archival_logic.md
│   └── data_access_proxy.md
├── scripts/
│   ├── archive_to_blob_function.py
│   └── read_from_blob_function.py
├── infra/
│   └── bicep_or_terraform_modules/
│       ├── cosmos_db.bicep
│       ├── blob_storage.bicep
│       └── function_app.bicep
└── .gitignore

## How to Deploy
1. Clone Repo
2. Deploy infrastructure using Bicep
3. Deploy Azure Functions
4. Validate data archival process

## Key Benefits
- Storage cost reduction
- Zero downtime
- No API changes

## License
MIT