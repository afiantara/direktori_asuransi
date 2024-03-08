import pandas as pd
from direktori_asuransi import *
if __name__=="__main__":
    conn = init()
    df = get_directory_data(conn)
    max,min= get_min_max_periode(df)
    print(max,min)
    df_entity = get_entity_name(df)
    print(df_entity)