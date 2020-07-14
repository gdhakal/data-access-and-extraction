import feedparser
import pandas as pd

from datetime import datetime


ITUNES = 'http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/ws/RSS/topMovies/xml'
RSS_LIST = [ITUNES]
DF_COLUMNS = ['source', 'date', 'rank', 'title', 'link', 'summary']

def top10_movies(rss, df):
	# parse is the primary function in FeedParser and the returned object is a dictionary
	feed = feedparser.parse(rss)

	# FeedParser sets the bozo bit when it detects a feed is not well-formed.
	# FeedParser will still parse the feed if it is not well-formed. The bozo bit can be used for error handling.
	if feed.bozo == 0:
		print("%s is a well-formed feed!" % feed.feed.title)
	elif feed.bozo == 1:
		print("%s has flipped the bozo bit. Potential errors ahead!" % feed.feed.title)
		return None

	# use get method of dictionary to see if the key exists.
	# set the feed date to be the published date, if it exists. If not, use the current date.
	feed_date = feed.feed.get('published', datetime.now().strftime('%Y-%m-%d'))

	# append the info of top 10 moves to the dataframe
	i = 0
	while i < 10:
		entry = feed.entries[i]
		feed_items = pd.Series([feed.feed.title, feed_date, i + 1, entry.title, entry.id, entry.summary], DF_COLUMNS)
		df = df.append(feed_items, ignore_index = True)
		i += 1

	return df

if __name__ == "__main__":
	# create an empty dataframe
	# pands also allows converting list to a data frame: pd.DataFrame(frame.entries)
	top10_df = pd.DataFrame(columns = DF_COLUMNS)

	for item in RSS_LIST:
		top10_df = top10_movies(item, top10_df)

	# save the dataframe to a csv
	top10_df.to_csv('topmovies.csv', header = DF_COLUMNS, index = False)