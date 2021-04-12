import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
   
def load_processed(srcpath, despath):
    ##Thank You Alessandro for this dictionary.
    data = pd.read_csv(srcpath)
    data=data.dropna().rename(columns={key: key.replace('-',' ').title() for key in data.columns}).replace({'Class': {'e':'edible', 'p': 'poisonous'},
            'Cap Shape': {'b': 'bell', 'c': 'conical', 'x': 'convex', 'f': 'flat', 'k': 'knobbed', 's': 'sunken'},
            'Cap Surface': {'f': 'fibrous', 'g': 'grooves', 'y' : 'scaly', 's': 'smooth'},
            'Cap Color': {'n': 'brown', 'b':'buff','c':'cinnamon','g':'gray','r':'green','p':'pink','u':'purple','e': 'red','w':'white','y':'yellow'},
            'Bruises': {'t': True, 'f': False},
            'Odor': {'a': 'almond', 'l':'anise','c':'creosote','y':'fishy','f':'foul','m':'musty','n':'none','p':'pungent','s':'spicy'},
            'Gill Attachment': {'a':'attached', 'd':'descending','f':'free','n':'notched'},
            'Gill Spacing': {'c':'close','w':'crowded','d':'distant'},
            'Gill Size': {'b':'broad','n':'narrow'},
            'Gill Color': {'k': 'black', 'n':'brown','b':'buff','h':'chocolate','g':'gray','r':'green','o':'orange','p':'pink','u':'purple','e':'red','w':'white','y':'yellow'},
            'Stalk Shape': {'e':'enlarging','t':'tapering'},
            'Stalk Root': {'b':'bulbous','c':'club','u':'cup','e':'equal','z':'rhizomorphs','r':'rooted','?':np.nan},
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
            'Habitat': {'g':'grasses','l':'leaves','m':'meadows','p':'paths','u':'urban','w':'waste','d':'woods'}}) .assign(Edible=data['class']).replace({'Edible':{'e':True, 'p':False}}).sort_values(by='Class').reset_index().drop('index',axis=1)
    return data

#    dict = {'Class': {'e':'edible', 'p': 'poisonous'},
#           'Cap Shape': {'b': 'bell', 'c': 'conical', 'x': 'convex', 'f': 'flat', 'k': 'knobbed', 's': 'sunken'},
#            'Cap Surface': {'f': 'fibrous', 'g': 'grooves', 'y' : 'scaly', 's': 'smooth'},
#           'Cap Color': {'n': 'brown', 'b':'buff','c':'cinnamon','g':'gray','r':'green','p':'pink','u':'purple','e': 'red','w':'white','y':'yellow'},
#            'Bruises': {'t': True, 'f': False},
#           'Odor': {'a': 'almond', 'l':'anise','c':'creosote','y':'fishy','f':'foul','m':'musty','n':'none','p':'pungent','s':'spicy'},
#            'Gill Attachment': {'a':'attached', 'd':'descending','f':'free','n':'notched'},
#            'Gill Spacing': {'c':'close','w':'crwoded','d':'distant'},
#            'Gill Size': {'b':'broad','n':'narrow'},
#            'Gill Color': {'k': 'black', 'n':'brown','b':'buff','h':'chocolate','g':'gray','r':'green','o':'orange','p':'pink','u':'purple','e':'red','w':'white','y':'yellow'},
#            'Stalk Shape': {'e':'enlarging','t':'tapering'},
#            'Stalk Root': {'b':'bulbous','c':'club','u':'cup','e':'equal','z':'rhizomorphs','r':'rooted','?':'unknown'},
#            'Stalk Surface Above Ring': {'f':'fibrous','y':'scaly','k':'silky','s':'smooth'},
#            'Stalk Surface Below Ring': {'f':'fibrous','y':'scaly','k':'silky','s':'smooth'},
#            'Stalk Color Above Ring': {'n':'brown','b':'buff','c':'cinnamon','g':'gray','o':'orange','p':'pink','e':'red','w':'white','y':'yellow'},
#            'Stalk Color Below Ring': {'n':'brown','b':'buff','c':'cinnamon','g':'gray','o':'orange','p':'pink','e':'red','w':'white','y':'yellow'},
#            'Veil Type': {'p':'partial','u':'universal'},
#            'Veil Color': {'n':'brown','o':'orange','w':'white','y':'yellow'},
#            'Ring Number': {'n':0,'o':1,'t':2},
#            'Ring Type': {'c':'cobwebby','e':'evanescent','f':'flaring','l':'large','n':'none','p':'pendant','s':'sheathing','z':'zone'},
#            'Spore Print Color': {'k':'black','n':'brown','b':'buff','h':'chocolate','r':'green','o':'orange','u':'purlple','w':'white','y':'yellow'},
#           'Population': {'a':'abundant','c':'clustered','n':'numerous','s':'scattered','v':'several','y':'solitary'},
#            'Habitat': {'g':'grasses','l':'leaves','m':'meadows','p':'paths','u':'urban','w':'waste','d':'woods'}}
    # library
    data.to_csv(despath)
    return data
def describe_features(data):
    # give stats about the all data
    print('\033[1m'+"Statistic description of dataset:"+'\033[0m')
    print(data.describe(include='all'))
    #give details about the missing data
    print('\033[1m'+"Missing/Unknown entry details:"+'\033[0m')
    print(data.isna().sum())
    #gives the count of unique values in each column
    print('\033[1m'+"Count of unique values in Each Column:"+'\033[0m')
    print(data.nunique(axis=0))
    #gives the first ten columns
    print('\033[1m'+"The First ten rows:"+'\033[0m')
    print(data.head(10))
    return

    
    
def vennD(colname, colval, colname1, colval1, edibility, data ):
    df1=data[(data[colname]==colval)  & (data['Class']==edibility)]
    df2=data[(data[colname]==colval) & (data[colname1]==colval1) & (data['Class']==edibility)]
    df3=data[(data[colname1]==colval1) & (data['Class']==edibility)]
    return venn2(subsets = (len(df1)-len(df2), len(df3)-len(df2), len(df2)), set_labels = (colval+" "+colname, colval1+" "+colname1) )

## function made my Ale Pisa and Alec Nixon
def show_edibility_ratio(df):
    ratioDict = {}

    length = len(df.columns[1:])
    #axes = [None]*length
    #h = plt.figure(figsize=(10*3,10*int(length/3+1)))
    for i in range(1, length):
        col = df.columns[i]
        rqData = pd.DataFrame(df[col].value_counts())
        rqData.reset_index(inplace = True)

        rqData = rqData.merge(pd.DataFrame(df[col].loc[df['Edible'] != True].value_counts()).reset_index().rename(columns = {col:'Not Edible'}), how='outer')
        rqData = rqData.merge(pd.DataFrame(df[col].loc[df['Edible']].value_counts()).reset_index().rename(columns = {col:'Edible'}), how='outer')
        rqData['Edibility'] = rqData['Edible'].fillna(0) / (rqData['Not Edible'].fillna(0) + rqData['Edible'].fillna(0))
        #print(rqData)
        ratioDict.update({col:rqData})
        #axes[i] = h.add_subplot(int(length/3+1),3,i)
        #sns.barplot(data=rqData, x='index', y='Edibility')
    return ratioDict
def sort_by_influence(ratioDict, keepCoeff=False):
    ratios = pd.DataFrame(columns=['Feature','Edibility'])
    for ratio in ratioDict.values():
        for index, row in ratio.iterrows():
            #nr={'Feature':'{} {}'.format(row['index'],ratio.columns[1]),'Edibility':row['Edibility']}
            nr={'Feature':'{} {}'.format(regex.sub(r'([a-z])([a-z]*)',lambda match: '{}{}'.format(match.group(1).upper(),match.group(2)),str(row['index'])),ratio.columns[1]),'Edibility':row['Edibility']}
            #print(nr)
            ratios = ratios.append(nr, ignore_index=True)
    ratios['coeff'] = abs(ratios['Edibility']-0.5)+0.5
    ratios.sort_values(by=['coeff'],ascending=False).reset_index(drop=True,inplace=True)
    if not keepCoeff:
        ratios.drop(['coeff'],axis=1,inplace=True)
    return ratios

# Use the venn2 function
#venn2(subsets = (10, 5, 2), set_labels = ('Group A', 'Group B'))
#plt.show()
##analysis and cleaning
