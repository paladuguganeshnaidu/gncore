"""Small stdlib transaction probe, not a PostgreSQL concurrency benchmark."""
import json
import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.execute("CREATE TABLE claims (tenant TEXT, key TEXT, status TEXT, PRIMARY KEY (tenant, key))")
    connection.commit()
    connection.execute("BEGIN")
    connection.execute("INSERT INTO claims VALUES ('a', 'request-1', 'IN_PROGRESS')")
    connection.execute("UPDATE claims SET status = 'FAILED' WHERE tenant = 'a' AND key = 'request-1'")
    before = connection.execute("SELECT status FROM claims").fetchall()
    connection.rollback()
    after = connection.execute("SELECT status FROM claims").fetchall()
    assert before == [("FAILED",)] and after == []
print(json.dumps({"engine": "SQLite stdlib", "scope": "Transaction rollback only; no PostgreSQL lock or concurrency execution", "before_rollback": before, "after_rollback": after, "failed_state_survives_rollback": False, "passed": True}, indent=2))
