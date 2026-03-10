import pandas as pd

def preprocess(df, region_df):
    

    # filter only Summer Olympics
    df = df[df['Season'] == 'Summer']

    # merge with region dataset
    df = df.merge(region_df, on='NOC', how='left')

    # remove duplicates
    df.drop_duplicates(inplace=True)

    # one-hot encoding for medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

    return df