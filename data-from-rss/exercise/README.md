# Source

Everything implemented in this exercise is from the [source](https://www.youtube.com/watch?v=A42voDYkFZw&feature=youtu.be&t=7396)

# Tools
- Sublime Text Editor

# Components

- [FeedParser](https://pypi.org/project/feedparser/) python package to work with the RSS feed. FeedParser will allow us to deconstruct the data in the feed.
	- Install FeedParser: `pip install feedparser`
	- Verify installation: `pip list`

# Additonal Info

- Do FeedParser handle UTF and ASCII data encoding?

- Pandas also allows converting list to a data frame.

```
df = pd.DataFrame(frame.entries)
df.head()
```

- When working with multiple RSS feeds, we can append data into CSV file: 

```
#save the dataframe to a csv. if the csv exists, append to it
import os

if not os.path.isfile('top10.csv'):
   top10_df.to_csv('top10.csv', header = DF_COLUMNS, index=False)
else:
    top10_df.to_csv('top10.csv', mode = 'a', header=False, index=False)
```

