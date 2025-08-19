import json
from conftest import make_txn_payload

if __name__ == "__main__":
    txn = make_txn_payload(123.45)
    print(json.dumps(txn, indent=2))
