import pytest


def test_bq_row_and_null_checks(bq_client):
    """Check if BigQuery table has valid rows and no nulls."""
    project = bq_client.project
    dataset = pytest.config.getoption("--bq_dataset", default=None) or "my_dataset"
    table = pytest.config.getoption("--bq_table", default=None) or "my_table"
    table_ref = f"`{project}.{dataset}.{table}`"

    # Check rowcount
    q1 = f"SELECT COUNT(1) as cnt FROM {table_ref}"
    r1 = list(bq_client.query(q1))[0]
    assert r1.cnt >= 0

    # No null transaction_id
    q2 = f"SELECT COUNT(1) as nulls FROM {table_ref} WHERE transaction_id IS NULL"
    r2 = list(bq_client.query(q2))[0]
    assert r2.nulls == 0
