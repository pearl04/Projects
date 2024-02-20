#Day2
#1.drop duplicate rows
#2.replace missing values with 0
#3.Example: Standardize date format. 
#Automatically parse dates without specifying a format

import pandas as pd
df=pd.read_csv('messy_data.csv')
def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)
    df['date'] = pd.to_datetime(
        df['date'],errors='coerce')
    return df

cleaned_df = clean_data(df)
print(cleaned_df)
