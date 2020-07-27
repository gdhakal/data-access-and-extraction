# Data from RSS

RSS is an acronym for Really Simple Syndication. Syndication means sharing or transferring. RSS feed is a way to deliver content to users when new content is added to the website. This way users do not have to visit the website everyday to find new content. Instead, the user can subscribe to the RSS feed of the website and be notified whenever there is a new post.

Many websites provide RSS feeds:

- blogs and news website. 
- iTunes delivers podcasts by RSS feeds from content creators.
- library website can have RSS feed. You search for Python and put this in your RSS feed. Every time there is a new book that matches the word, it updates in your RSS reader.

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