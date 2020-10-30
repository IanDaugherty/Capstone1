import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

steam_path = '/home/ian/Desktop/galvanize/Capstone1/data/steam-200k.csv'



def read_to_pandas(file_path):
    return pd.read_csv(file_path)


def clean_steam_data(path):
    """
    Steamdb needs cleaning:
    -removed supurfluous rows with game purchased data
    -removed all zeros col
    -renamed and reorganized cols
    """
    db = read_to_pandas(path)
    purchases = db[db['purchase'] == 'purchase'].index
    db.drop(purchases, inplace = True)
    db.drop(labels = '0', axis = 1, inplace = True)
    db['user'] = db['151603712']
    db['game'] = db['The Elder Scrolls V Skyrim']
    db['playtime'] = db['1.0']
    return db[['game', 'playtime','user']]

def steam_game_totals(db):
    """
    steam DB grouped by unique game name
    counts for total hours, unique users pergame
    returns db grouped by games
    """
    db['usercount'] = 1
    gamecount = db.groupby(['game']).sum()
    gamecount['Hours/User'] = gamecount['playtime'] / gamecount['usercount']
    print(gamecount.sort_values('playtime', ascending = False)['playtime'].head(10))
    print(gamecount.sort_values('usercount', ascending = False)['usercount'].head(10))
    print(gamecount.sort_values('Hours/User', ascending = False)['Hours/User'].head(10))
    return gamecount

def steam_user_totals(path):
    """
    returns a DB grouped by users, summed over playtime and counted by purchases
    """
    db = read_to_pandas(path)
    db = db.append({'151603712':'151603712',
                    'The Elder Scrolls V Skyrim':'The Elder Scrolls V Skyrim',
                    'purchase':'purchase',
                    '1.0':'1.0'}, ignore_index = True)
    db = db.rename(columns = {"151603712":"userid", 
                                    "The Elder Scrolls V Skyrim":"game", 
                                    "purchase":"own", 
                                    "1.0":"playtime"})
    purchasecount = db[db['own'] == 'purchase'].groupby('userid').count()
    playtime = db[db['own'] == 'play'].groupby('userid')['playtime'].sum()
    return purchasecount.merge(playtime, on = 'userid')



if __name__ == '__main__':
     steam = clean_steam_data(steam_path)
