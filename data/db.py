import sqlite3

import pandas as pd

from config import SCHEME_DICT_QUERY, SQLITE_DB_ENDPOINT


def get_scheme_dict():
    conn = sqlite3.connect(SQLITE_DB_ENDPOINT)
    return pd.read_sql_query(SCHEME_DICT_QUERY, con=conn).set_index('SCHEME').to_dict()['HEAD']
