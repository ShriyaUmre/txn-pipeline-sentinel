import requests
import time
from conftest import make_txn_payload


def test_api_ingest_and_ack(api_base):
    """Send a transaction and check API responds correctly."""
    payload = make_txn_payload(199.99)
    resp = requests.post(f"{api_base}/v1/transactions", json=payload, timeout=5)

    # API should accept the transaction
    assert resp.status_code in (200, 201, 202)

    # API should echo or return transaction_id
    body = resp.json()
    assert "transaction_id" in body
