# Capstone
First capstone project for galvanize

##Datasets
https://www.kaggle.com/tamber/steam-video-games
A collection of hours played of 3600 unique games across 11350 users. 


### Context
Steam is a digital, PC video game application which hosts a store front, as well as a library of your personal purchases, and more. The store often hosts sizable discounts on individual games, bundle deals, and multi-day "Steam Sales". Through the library you can download, install, and launch your games.


### EDA
Our data gives us information on the playtime of specific games for individual users. Grouping by games can give us metrics for measuring popularity

```
top10_playtime = steam.sort_values('playtime', ascending=False)['playtime'].head(10)
top10_playtime.plot.bar()
plt.xticks(rotation=45, ha='right')
plt.ylabel('Hours(Mill)')
plt.xlabel('')
plt.title("Top 10 most played by hour")
plt.savefig("images/top10gamesplayed.jpg")
```

![GamesPlayed](/images/topowned.png)


The most common game to own from these 11,350 users was Dota 2. Not surprising considering it is a micro-transaction based, free-to-play game. Also not very surprising is that seven of the top ten games are owned by Valve, the parent company of steam.

![GamesPlayed](/images/top10gamesplayed.png)


The top most played games looks similar, but we can really see Dota 2’s dominance on the Steam market, with almost 1,000,000 hours. 


![GamesPlayed](/images/totaltime_pie.png)


In fact, the combined playtime of the every game below the top 9 still does not equal that of Dota 2.




## A look at Dota 2 users

A high percentage of the sample owning a free-to-play game may not be surprising, but it’s clearly a popular game otherwise. That raises the question of why a store would give away a highly successful game. Let’s look at the metrics available for the two groups: Players who own Dota 2, and players who do not. The data has both a ‘play’ and a ‘purchase’ categories in order to distinguish between games the users owns, and those that they have played.

```
dota_owners = steam[(steam['game'] == "Dota 2")]['userid'].unique()
ownsdota = steam[steam['userid'].isin(dota_owners)]
duser_purchasecount = ownsdota[ownsdota['own'] == 'purchase'].groupby('userid').count()
duser_playtime = ownsdota[ownsdota['own'] == 'play'].groupby('userid')['playtime'].sum()

dota_users = duser_purchasecount.merge(duser_playtime, on = 'userid')
```

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

```
fig, axs = plt.subplots(4, figsize = (10,10))
axs[0].hist(owned_bootstrap, bins = 100)
axs[0].set_title(f"Dota 2 users own {means[0]} more games than none Dota 2 users", fontsize = 15)
axs[0].axvline(perc[0][0], color='orange', alpha = 1)
axs[0].axvline(perc[0][1], color='red', alpha = 1)
axs[0].set_xlabel("Difference in mean games owned per user")
axs[0].legend(('2.5%', '97.5%'))
```

![Games Owned bootstrap](/images/owned_bootstrap.png)
![Games played bootstrap](/images/played_bootstrap.png)
![Time played](/images/playtime_bootstrap.png)

We can conclude at the very least that Dota 2 player prefer to buy more games from the Steam store than Non-Dota 2 players. But more than that a ratio of the users games played of the games they own tells us more. 

![O/P Ratio](/images/op_bootstrap.png)

This demonstrates the real power of hosting a free-to-play game on a game store. Dota 2 users own more, as well as spend more time playing video games on Steam, but they play less of their library then users who do not own Dota 2. 

## Conclusion
Here we have seen the value added to the Steam store by giving away a hugely popular game for free. Each time user wants to play Dota 2, they must first launch Steam, which lands them on the store's front page, list all the sales and new releases, where more exposures lead to more sales over time.

## Further inquiries

-This data set is over six years old, videos games and the FTP model have only gotten more popular. A similar but updated data set would be interest to analyze in a similar way.

-Do other popular games share this relationship? Is it a matter of time spent playing video games in general or is it specific to Dota 2 players?