import json
import logging

from flask import Response

from pointy.database.common import connect

logger = logging.getLogger(__name__)


def build_db():
    conn = connect()
    execute_query(conn, "CREATE SCHEMA points")
    execute_query(conn, "CREATE SCHEMA dbo")
    execute_query(conn, "CREATE TABLE dbo.teams (id varchar(20) NOT NULL, PRIMARY KEY (id))")
    conn.close()
    return Response(json.dumps({"status": "success"}), 200)


def execute_query(conn, query):
    with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
