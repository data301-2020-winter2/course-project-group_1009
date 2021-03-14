import pandas as pd
import re as regex
import matplotlib.pyplot as plt
import seaborn as sns


def prep_data(sourcePath,destPath):
    #load
    df = pd.read_csv(sourcePath)
    
    #process
    #dictionary by Alessandro. Thank you.
    dict = {'Class': {'e':'edible', 'p': 'poisonous'},
            'Cap Shape': {'b': 'bell', 'c': 'conical', 'x': 'convex', 'f': 'flat', 'k': 'knobbed', 's': 'sunken'},
            'Cap Surface': {'f': 'fibrous', 'g': 'grooves', 'y' : 'scaly', 's': 'smooth'},
            'Cap Color': {'n': 'brown', 'b':'buff','c':'cinnamon','g':'gray','r':'green','p':'pink','u':'purple','e': 'red','w':'white','y':'yellow'},
            'Bruises': {'t': True, 'f': False},
            'Odor': {'a': 'almond', 'l':'anise','c':'creosote','y':'fishy','f':'foul','m':'musty','n':'none','p':'pungent','s':'spicy'},
            'Gill Attachment': {'a':'attached', 'd':'descending','f':'free','n':'notched'},
            'Gill Spacing': {'c':'close','w':'crwoded','d':'distant'},
            'Gill Size': {'b':'broad','n':'narrow'},
            'Gill Color': {'k': 'black', 'n':'brown','b':'buff','h':'chocolate','g':'gray','r':'green','o':'orange','p':'pink','u':'purple','e':'red','w':'white','y':'yellow'},
            'Stalk Shape': {'e':'enlarging','t':'tapering'},
            'Stalk Root': {'b':'bulbous','c':'club','u':'cup','e':'equal','z':'rhizomorphs','r':'rooted','?':'unknown'},
            'Stalk Surface Above Ring': {'f':'fibrous','y':'scaly','k':'silky','s':'smooth'},
            'Stalk Surface Below Ring': {'f':'fibrous','y':'scaly','k':'silky','s':'smooth'},
            'Stalk Color Above Ring': {'n':'brown','b':'buff','c':'cinnamon','g':'gray','o':'orange','p':'pink','e':'red','w':'white','y':'yellow'},
            'Stalk Color Below Ring': {'n':'brown','b':'buff','c':'cinnamon','g':'gray','o':'orange','p':'pink','e':'red','w':'white','y':'yellow'},
            'Veil Type': {'p':'partial','u':'universal'},
            'Veil Color': {'n':'brown','o':'orange','w':'white','y':'yellow'},
            'Ring Number': {'n':0,'o':1,'t':2},
            'Ring Type': {'c':'cobwebby','e':'evanescent','f':'flaring','l':'large','n':'none','p':'pendant','s':'sheathing','z':'zone'},
            'Spore Print Color': {'k':'black','n':'brown','b':'buff','h':'chocolate','r':'green','o':'orange','u':'purlple','w':'white','y':'yellow'},
            'Population': {'a':'abundant','c':'clustered','n':'numerous','s':'scattered','v':'several','y':'solitary'},
            'Habitat': {'g':'grasses','l':'leaves','m':'meadows','p':'paths','u':'urban','w':'waste','d':'woods'}}
    df=(df
     .dropna() #not actually needed, but included for robustness
     .rename(columns=lambda x: regex.sub(r'-',r' ',x))
     .rename(columns=lambda x: regex.sub(r'([a-z])([a-z]*)',lambda match: '{}{}'.format(match.group(1).upper(),match.group(2)),x))
     .replace(dict)
     .assign(Edible=df['class'])
     .replace({'Edible':{'e':True, 'p':False}})
    )

    #save
    df.to_csv(destPath)
    
    #return
    return df

def plotEdibility(df):
    length = len(df.columns[1:])
    axes = [None]*length
    h = plt.figure(figsize=(10*3,10*int(length/3+1)))
    for i in range(1, length):
        #print('col {}'.format(df.columns[i]))
        axes[i] = h.add_subplot(int(length/3+1),3,i)
        sns.countplot(data=df, x=df.columns[i], hue="Edible", hue_order=[True,False], ax=axes[i])
    #return df

def show_edibility_ratio(df):
    ratioDict = {}

    length = len(df.columns[1:])
    axes = [None]*length
    h = plt.figure(figsize=(10*3,10*int(length/3+1)))
    for i in range(1, length):
        col = df.columns[i]
        rqData = pd.DataFrame(df[col].value_counts())
        rqData.reset_index(inplace = True)

        rqData = rqData.merge(pd.DataFrame(df[col].loc[df['Edible'] != True].value_counts()).reset_index().rename(columns = {col:'Not Edible'}), how='outer')
        rqData = rqData.merge(pd.DataFrame(df[col].loc[df['Edible']].value_counts()).reset_index().rename(columns = {col:'Edible'}), how='outer')
        rqData['Edibility'] = rqData['Edible'] / (rqData['Not Edible']+rqData['Edible'])
        #print(rqData)
        ratioDict.update({col:rqData})
        axes[i] = h.add_subplot(int(length/3+1),3,i)
        sns.barplot(data=rqData, x='index', y='Edibility')
    return ratioDict