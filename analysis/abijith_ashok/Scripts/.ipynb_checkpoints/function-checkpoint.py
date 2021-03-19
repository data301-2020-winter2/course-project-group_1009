import pandas as pd
   
def load_process(path):
    data = pd.read_csv(path)
    ##analysis and cleaning
    return data