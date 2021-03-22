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
            'Habitat': {'g':'grasses','l':'leaves','m':'meadows','p':'paths','u':'urban','w':'waste','d':'woods'}})

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
# Use the venn2 function
#venn2(subsets = (10, 5, 2), set_labels = ('Group A', 'Group B'))
#plt.show()
##analysis and cleaning
