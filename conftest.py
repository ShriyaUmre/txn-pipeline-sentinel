import os
import uuid
import time
import pytest
import requests
from google.cloud import bigquery

# API base URL (from environment variable or default)
API_BASE = os.getenv("API_BASE", "http://localhost:5000")

# BigQuery settings (from environment variables)
BQ_PROJECT = os.getenv("BQ_PROJECT")
BQ_DATASET = os.getenv("BQ_DATASET")
BQ_TABLE = os.getenv("BQ_TABLE")


@pytest.fixture(scope="session")
def api_base():
    """Provide the base URL for the API."""
    return API_BASE


@pytest.fixture(scope="session")
def bq_client():
    """Return a BigQuery client if project is set, otherwise skip."""
    if not BQ_PROJECT:
        pytest.skip("BQ_PROJECT not set, skipping BigQuery tests")
    return bigquery.Client(project=BQ_PROJECT)


def make_txn_payload(amount=10.0):
    """Helper to create a fake transaction payload."""
    return {
        "transaction_id": str(uuid.uuid4()),
        "amount": amount,
        "currency": "INR",
        "timestamp": int(time.time()),
        "metadata": {"source": "txn-pipeline-sentinel"}
    }
