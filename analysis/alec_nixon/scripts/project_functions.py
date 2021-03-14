import pandas as pd
import re as regex


def prep_data(sourcePath,destPath):
    #load
    df = pd.read_csv(sourcePath)
    
    #process
    df=(df
     .dropna() #not actually needed, but included for robustness
     .rename(columns=lambda x: regex.sub(r'-',r' ',x))
     .rename(columns=lambda x: regex.sub(r'([a-z])([a-z]*)',lambda match: '{}{}'.format(match.group(1).upper(),match.group(2)),x))
     .assign(Edible=df['class'])
     .replace({'Edible':{'e':True, 'p':False}})
    )

    #save
    df.to_csv(destPath)
    
    #return
    return df