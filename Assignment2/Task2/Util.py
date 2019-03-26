import numpy as np
import pandas as pd

def ReadTrainData(fileName='./data/train.tsv', asNumpy=True):
    df = pd.read_csv(fileName, sep='\t', header=0)
    df.dropna(axis='index', how='any')

    df_features = df.drop(['Sentiment'], axis=1)
    df_targets = df.drop(['PhraseId', 'SentenceId', 'Phrase'], axis=1)

    if(asNumpy):
        return df_features.values, np.transpose(df_targets.values)[0]
    else:
        return df_features, df_targets

def ReadTestData(fileName='./data/test.tsv', asNumpy=True):
    df_features = pd.read_csv(fileName, sep='\t', header=0)
    df_features.dropna(axis='index', how='any')

    if(asNumpy):
        return df_features.values
    else:
        return df_features