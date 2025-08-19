# txn-pipeline-sentinel

This is a demo project that shows how to test:
- API ingestion (sending transactions and checking responses)
- BigQuery validations (data integrity checks)

It uses:
- **pytest** → testing framework
- **requests** → to call APIs
- **google-cloud-bigquery** → to validate data in BigQuery
- **pytest-html** → to generate test reports

## Run tests locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
