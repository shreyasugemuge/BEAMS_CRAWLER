import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate

from util import db


def get_raw_table_with_id(id, html_str):
    soup = BeautifulSoup(html_str, 'lxml')
    return soup.find('table', id='table2', recursive=True)


def to_dataframe(raw_table):
    return pd.read_html(raw_table,header=0)[0]


def view_df(df):
    return tabulate(df, headers='keys', tablefmt='psql')


def process_dataframe(raw_df):
    dict = db.get_scheme_dict()
    # map last two characters with particular heads
    raw_df['Scheme & Detail Head'] = raw_df['Scheme & Detail Head'].map(lambda x: str(x)[-2:]).map(dict)

    # remove heads that are not needed and return
    return raw_df[raw_df['Scheme & Detail Head'].notnull()].groupby('Scheme & Detail Head', as_index=False).sum()