import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate

import config as C
from data import db


def get_raw_table_with_id(id, html_str):
    soup = BeautifulSoup(html_str, 'lxml')
    return soup.find('table', id='table2', recursive=True)


def to_dataframe(raw_table):
    return pd.read_html(raw_table, header=0)[0]


def view_df(df):
    return tabulate(df, headers='keys', tablefmt='psql')


def process_dataframe(raw_df):
    print("Processing Data")
    dict = db.get_scheme_dict()
    raw_df['Scheme & Detail Head'] = raw_df[raw_df['Scheme & Detail Head'].str.contains(C.SCHEME_HEADER)]
    raw_df['Scheme & Detail Head'] = raw_df['Scheme & Detail Head'].map(lambda x: str(x)[-2:]).map(dict)
    raw_df['Spending'] = round(100 * (raw_df['Actual Exp'] / raw_df['Grant Received']), 2)
    df = raw_df[raw_df['Scheme & Detail Head'].notnull()]
    df = df[df['Spending'] < C.THRES[3]]

    return df.groupby('Scheme & Detail Head', as_index=False).sum()


def split_df(df, thres):
    dfa = df[df['Spending'] < C.THRES[thres]]
    if (thres > 0):
        dfa = dfa[dfa['Spending'] > C.THRES[thres - 1]]
    return dfa
