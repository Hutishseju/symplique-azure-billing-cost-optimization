resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'archivestorageacct'
  location: resourceGroup().location
  sku: {
    name: 'Standard_GRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Cool'
  }
}