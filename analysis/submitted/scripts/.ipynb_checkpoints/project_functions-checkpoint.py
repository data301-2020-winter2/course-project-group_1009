import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def load_and_process_data(directory):
    df = pd.read_csv(directory) # I can't chain this one because I access df right here
    df = (df.rename(columns = {key: key.replace('-',' ').title() for key in df.columns}) # <---- 
        .replace({'Class': {'e':'edible', 'p': 'poisonous'},
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
        .assign(Edible=df['class']).replace({'Edible':{'e':True, 'p':False}}).sort_values(by='Class').reset_index().drop('index',axis=1))
    return df


def show_cap_related_features(df, ratioDict):
    #sns.set_palette('Set1')
    sns.set_palette("Paired")

    fig = plt.figure(figsize=(20,12))
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)
    ax3 = fig.add_subplot(233)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)
    ax6 = fig.add_subplot(236)
    sns.countplot(data=df, x='Cap Shape', hue="Class", ax=ax1, order=ratioDict['Cap Shape']['index'])
    sns.countplot(data=df, x='Cap Surface', hue="Class", ax=ax2, order=ratioDict['Cap Surface']['index'])
    sns.countplot(data=df, x='Cap Color', hue="Class", ax=ax3, order=ratioDict['Cap Color']['index'])
#    sns.barplot(data=ratioDict['Cap Shape'], x='index', y='Edibility', ax = ax4, order=ratioDict['Cap Shape']['index'])
#    sns.barplot(data=ratioDict['Cap Surface'], x='index', y='Edibility', ax = ax5, order=ratioDict['Cap Surface']['index'])
    #sns.set_palette('Set1')
#    sns.barplot(data=ratioDict['Cap Color'], x='index', y='Edibility', ax = ax6, order=ratioDict['Cap Color']['index'])
    
    sns.barplot(data=ratioDict['Cap Shape'], x='index', y='Edibility', ax = ax4, order=ratioDict['Cap Shape']['index']).set(xlabel='Cap Shape')
    sns.barplot(data=ratioDict['Cap Surface'], x='index', y='Edibility', ax = ax5, order=ratioDict['Cap Surface']['index']).set(xlabel='Cap Surface')
    #sns.set_palette('Set1')
    sns.barplot(data=ratioDict['Cap Color'], x='index', y='Edibility', ax = ax6, order=ratioDict['Cap Color']['index']).set(xlabel='Cap Color')

    
def show_gill_related_features(df, ratioDict):
#    fig = plt.figure(figsize=(20,15))
#    ax1 = fig.add_subplot(221)
#    ax2 = fig.add_subplot(222)
#    ax3 = fig.add_subplot(223)
#    ax4 = fig.add_subplot(224)
#    sns.countplot(data=df, x='Gill Attachment', hue="Class", ax=ax1)
#    sns.countplot(data=df, x='Gill Spacing', hue="Class", ax=ax2)
#    sns.countplot(data=df, x='Gill Size', hue="Class", ax=ax3)
#    sns.countplot(data=df, x='Gill Color', hue="Class", ax=ax4)

#    sns.set_palette("Paired")
#    fig = plt.figure(figsize=(20,15))
    col = ['Gill Attachment', 'Gill Spacing', 'Gill Size', 'Gill Color']
#    length = len(col)
#    axes = [None]*length*2
#    for i in range(0,length):
#        axes[i] = fig.add_subplot(2,length,i+1)
#        axes[i+length] = fig.add_subplot(2,length,i+length+1)
#        sns.countplot(data=df, x=col[i], hue="Class", ax=axes[i], order=ratioDict[col[i]]['index'])
#        sns.barplot(data=ratioDict[col[i]], x='index', y='Edibility', ax = axes[i+length], order=ratioDict[col[i]]['index'])

    show_features(df,ratioDict,col)
    


def show_stalk_related_features(df, ratioDict):
#    fig = plt.figure(figsize=(20,15))
#    ax1 = fig.add_subplot(231)
#    ax2 = fig.add_subplot(232)
#    ax3 = fig.add_subplot(233)
#    ax4 = fig.add_subplot(234)
#    ax5 = fig.add_subplot(235)
#    ax6 = fig.add_subplot(236)
#    sns.countplot(data=df, x='Stalk Shape', hue="Class", ax=ax1)
#    sns.countplot(data=df, x='Stalk Root', hue="Class", ax=ax2)
#    sns.countplot(data=df, x='Stalk Surface Above Ring', hue="Class", ax=ax3)
#    sns.countplot(data=df, x='Stalk Surface Below Ring', hue="Class", ax=ax4)
#    sns.countplot(data=df, x='Stalk Color Above Ring', hue="Class", ax=ax5)
#    sns.countplot(data=df, x='Stalk Color Below Ring', hue="Class", ax=ax6)

    col = ['Stalk Shape','Stalk Root','Stalk Surface Above Ring','Stalk Surface Below Ring','Stalk Color Above Ring','Stalk Color Below Ring']
    show_features(df,ratioDict,col)

def show_veil_related_features(df, ratioDict):
#    fig = plt.figure(figsize=(20,7))
#    ax1 = fig.add_subplot(121)
#    ax2 = fig.add_subplot(122)
#    sns.countplot(data=df, x='Veil Type', hue="Class", ax=ax1)
#    sns.countplot(data=df, x='Veil Color', hue="Class", ax=ax2)
    
    col = ['Veil Type','Veil Color']
    show_features(df,ratioDict,col)


def show_ring_related_features(df, ratioDict):
#    fig = plt.figure(figsize=(20,7))
#    ax1 = fig.add_subplot(121)
#    ax2 = fig.add_subplot(122)
#    sns.countplot(data=df, x='Ring Number', hue="Class", ax=ax1)
#    sns.countplot(data=df, x='Ring Type', hue="Class", ax=ax2)
    
    col = ['Ring Number','Ring Type']
    show_features(df,ratioDict,col)


def show_life_related_features(df, ratioDict):
#    fig = plt.figure(figsize=(20,7))
#    ax1 = fig.add_subplot(121)
#    ax2 = fig.add_subplot(122)
#    sns.countplot(data=df, x='Population', hue="Class", ax=ax1)
#    sns.countplot(data=df, x='Habitat', hue="Class", ax=ax2)

    col = ['Population','Habitat']
    show_features(df,ratioDict,col)


def show_miscellaneous_features(df, ratioDict):
#    fig = plt.figure(figsize=(20,6))
#    ax1 = fig.add_subplot(131)
#    ax2 = fig.add_subplot(132)
#    ax3 = fig.add_subplot(133)
#    sns.countplot(data=df, x='Spore Print Color', hue="Class", ax=ax1)
#    sns.countplot(data=df, x='Bruises', hue="Class", ax=ax2)
#    sns.countplot(data=df, x='Odor', hue="Class", ax=ax3)

    col = ['Spore Print Color','Bruises','Odor']
    show_features(df,ratioDict,col)


def show_features(df, ratioDict, col):
    sns.set_palette("Paired")
    fig = plt.figure(figsize=(20,15))
    length = len(col)
    axes = [None]*length*2
    for i in range(0,length):
        axes[i] = fig.add_subplot(2,length,i+1)
        axes[i+length] = fig.add_subplot(2,length,i+length+1)
        sns.countplot(data=df, x=col[i], hue="Class", ax=axes[i], order=ratioDict[col[i]]['index'])
        sns.barplot(data=ratioDict[col[i]], x='index', y='Edibility', ax = axes[i+length], order=ratioDict[col[i]]['index']).set(xlabel=col[i])


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

