import sqlite3

import pandas as pd


def get_scheme_dict():
    conn = sqlite3.connect('data.db')
    return pd.read_sql_query("SELECT * FROM SCHEME_HEAD", con=conn).set_index('SCHEME').to_dict()['HEAD']
