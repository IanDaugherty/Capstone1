# Capstone
First capstone project for galvanize

##Datasets
https://www.kaggle.com/tamber/steam-video-games
A collection of hours played of 3600 unique games across 11350 users. 


### Context
Steam is a digital, PC video game application which hosts a store front, as well as a library of your personal purchases, and more. The store often hosts sizable discounts on individual games, bundle deals, and multi-day "Steam Sales". Through the library you can download, install, and launch your games.


### EDA
Our data gives us information on the playtime of specific games for individual users. Grouping by games can give us metrics for measuring popularity

The most common game to own from these 11,350 users was Dota 2. Not surprising considering it is a micro-transaction based, free-to-play game. Also not very surprising is that seven of the top ten games are owned by Valve, the parent company of steam.
![GamesPlayed](/images/topowned.png)

The top most played games looks similar, but we can really see Dota 2’s dominance on the Steam market, with almost 1,000,000 hours. 
![GamesPlayed](/images/top10gamesplayed.png)

In fact, the combined playtime of the every game below the top 9 still does not equal that of Dota 2.

![GamesPlayed](/images/totaltime_pie.png)

A high percentage of the sample owning a free-to-play game may not be surprising, but it’s clearly a popular game otherwise. That raises the question of why a store would give away a highly successful game. Let’s look at the metrics available for the two groups: Players who own Dota 2, and players who do not. The data has both a ‘play’ and a ‘purchase’ categories in order to distinguish between games the users owns, and those that they have played.

![Dota 2 Users graph](/images/Users_db.png)

#### Analysis
A bootstrap sampling method was used to compare sample means. The two groups where compared and plotted over 50,000 samples. 

```
def bootstrap_diff(samp1, samp2):
    bootstrap_diff = []
    for i in range(0, 50000):
        bootstrap1 = np.random.choice(samp1, size=len(samp1), replace=True)
        bootstrap2 = np.random.choice(samp2, size=len(samp2), replace=True)
        bootstrap_diff.append(np.mean(bootstrap1)-np.mean(bootstrap2))
    return bootstrap_diff
```
The results are that across the board, Steam users who own Dota 2 own more games, play more unique games, and spend more time playing games.
[Games Owned bootstrap](/images/owned_bootstrap.png)
[Games played bootstrap](/images/played_bootstrap.png)
[Time played](/images/playtime_bootstrap.png)
## Conclusion
