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

    raw_df['Scheme & Detail Head'] = raw_df['Scheme & Detail Head'].map(lambda x: str(x)[-2:]).map(dict)

    raw_df['Spending'] = round(100*(raw_df['Actual Exp'] / raw_df['Grant Received']),2)
    df = raw_df[raw_df['Scheme & Detail Head'].notnull()]
    df = df[df['Spending'] < 40]

    return df.groupby('Scheme & Detail Head', as_index=False).sum()

# def to_inr(amount):
#     amount.astype(str)