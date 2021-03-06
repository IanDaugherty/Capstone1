# Galvanize Capstone
### Exploritory data anlysis of a Steam user data base

![Steam logo](/images/Steam.jpg)


 
### Context
Steam is a PC video game application which hosts a store front as well as a library of personal purchases, friends list, and more. The store often hosts sizable discounts on individual games, bundle deals, and multi-day "Steam Sales." 

![Steam logo](/images/steamstore.jpeg)

Through the library you can download, install, and launch your games.

![Steam logo](/images/steam-lib.jpg)

Our data gives us information on the individual's playtime for all games in their library. 

## Datasets

https://www.kaggle.com/tamber/steam-video-games
A collection of hours played of 3600 unique games across 11,350 users. 

![Raw import data set](/images/steam_raw.png)


### EDA

We start by aggregating information about individial games. These groupings can give us metrics for measuring popularity and an idea of at what we are looking. 

```
top10_playtime = steam.sort_values('playtime', ascending=False)['playtime'].head(10)
top10_playtime.plot.bar()
plt.xticks(rotation=45, ha='right')
plt.ylabel('Hours(Mill)')
plt.xlabel('')
plt.title("Top 10 most played by hour")
plt.savefig("images/top10gamesplayed.jpg")
```

![GamesOwned](/images/topowned.png)


The most common game to own from these 11,350 users was Dota 2. Not surprising considering it is a micro-transaction-based, free-to-play game. Also unsurprisingly, seven of the top ten games are owned by Valve, the parent company of Steam.

![GamesPlayed](/images/top10gamesplayed.png)


It would make sense that the top most played would look similar to most owned, but we can really see Dota 2’s dominance on the Steam market, with almost 1,000,000 hours bewteen approximately 4,800 users.


![TotalTime](/images/totaltime_pie.png)


In fact, the combined playtime of every game below the top 9 still does not equal that of Dota 2.




## A look at Dota 2 users

A high percentage of the sample owning a free-to-play game may not be surprising, but Dota is clearly popular to play. That raises the question of why a store would give away a highly successful game. Let’s look at the metrics available for the two groups: Players who own Dota 2, and players who do not. 

```
dota_owners = steam[(steam['game'] == "Dota 2")]['userid'].unique()
ownsdota = steam[steam['userid'].isin(dota_owners)]
duser_purchasecount = ownsdota[ownsdota['own'] == 'purchase'].groupby('userid').count()
duser_playtime = ownsdota[ownsdota['own'] == 'play'].groupby('userid')['playtime'].sum()

dota_users = duser_purchasecount.merge(duser_playtime, on = 'userid')
```

![Dota 2 Users graph](/images/Users_db.png)

Here we look at each user's games purchased, games played, and total time spent playing all games on Steam. 

#### Analysis
![Games vs Hours](/images/Users_owned_played.png)

A bootstrap sampling method was used to compare sample means. The two groups were compared and plotted over 50,000 samples. 

```
def bootstrap_diff(samp1, samp2):
    bootstrap_diff = []
    for i in range(0, 50000):
        bootstrap1 = np.random.choice(samp1, size=len(samp1), replace=True)
        bootstrap2 = np.random.choice(samp2, size=len(samp2), replace=True)
        bootstrap_diff.append(np.mean(bootstrap1)-np.mean(bootstrap2))
    return bootstrap_diff
```
The results show that across the board Steam users who own Dota 2 own more games, play more unique games, and spend more time playing games.

```
fig, axs = plt.subplots(4, figsize = (10,10))
axs[0].hist(owned_bootstrap, bins = 100)
axs[0].set_title(f"Dota 2 users own {means[0]} more games than none Dota 2 users", fontsize = 15)
axs[0].axvline(perc[0][0], color='orange', alpha = 1)
axs[0].axvline(perc[0][1], color='red', alpha = 1)
axs[0].set_xlabel("Difference in mean games owned per user")
axs[0].legend(('2.5%', '97.5%'))
```

![Games Owned bootstrap](/images/owned_bootstrap2.png)


![Games played bootstrap](/images/played_bootstrap2.png)


![Time played](/images/playtime_bootstrap2.png)


We can conclude that Dota 2 players prefer to buy more games from the Steam store than non-Dota 2 players. Also, a ratio of the user's games played to the total number of games they own tells us that they play less of the games that they purchase. 

![O/P Ratio](/images/op_bootstrap2.png)

This demonstrates the real power of hosting a free-to-play game on a game store. Dota 2 users own more and spend more time playing video games on Steam, but they play less of their overall library than users who do not own Dota 2. 

## Conclusion
Here we have seen the value added to the Steam store by giving away a hugely popular game for free. Each time a user goes to play Dota 2, they must first launch Steam; this lands them on the store's front page listing of sales and new releases where more exposure will eventually lead to more sales over time.

Potenential biases abound.
- People who play Valve games on Steam may be biased towords Valve products, making purchases on Steam
- Many users have 1 game with less than 1 hours of play time, greatly skewing any results
![O/P Ratio](/images/steamsale.jpg)



## Further inquiries


-There are many users in both samples with less than one hour played. Should these be controlled for? Should it count that you 'played' a game if you loaded it up once and never played it again? Do Dota players have more or less '< 1.0 hour' games than non-Dota users?

-Do other popular games, regardless of their price, share this relationship? Is it a matter of time spent playing video games in general or is the correlation specific to Dota 2 players only?


-This data set is over six years old; videos games and the FTP model have only gotten more popular. A similar but updated data set would be interesting to analyze in a similar way.