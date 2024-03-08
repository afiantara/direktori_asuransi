import pandas as pd
import numpy as np
from db import *

db_name = './Data_Kantor_Selain_KP.db'

entity_desc=['Asuransi Jiwa','Asuransi Umum','Asuransi Wajib','Asuransi Umum Syariah','Asuransi Jiwa Syariah']
office_types=['Kantor Pemasaran','Kantor Selain Kantor Cabang','Kantor Cabang','Unit Syariah','Kantor Selain Kantor Cabang Unit Syariah','Kantor Pusat Unit Syariah','Kantor Cabang Syariah','Kantor Selain Kantor Cabang Syariah']

global conn

def init():
    conn = create_connection(db_name)
    return conn

def get_min_max_periode(df):
    return df['report_date'].min(),df['report_date'].max()

def get_directory_data(conn):
    query='select * from Data_Kantor_Selain_KP'
    df = get_data(query,conn)
    return df

def get_entity_name(df):
    keys=['report_date','EntityName']
    df = df.groupby(keys).count()
    return df