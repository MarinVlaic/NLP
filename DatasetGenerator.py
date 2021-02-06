import pandas as pd

dataframe = pd.read_csv("./realdonaldtrump.csv")
# TAKE TWEETS FROM 2015 ONWARD
filtered_dates = dataframe.loc[dataframe['date'].astype('datetime64[ns]') > pd.Timestamp('2015-1-1')]
filtered_retweets = filtered_dates.loc[filtered_dates['content'].str.contains('@.+:') == False]
# FILTER RE-TWEETS
filtered_retweets['content'] = filtered_retweets['content'].replace(to_replace="@\\s*", value="@", regex=True)
# REPLACE ALL TAGS WITH @TAG
filtered_retweets['content'] = filtered_retweets['content'].replace("@[0-9a-zA-Z]+", "@TAG", regex=True)
# REPLACE ALL HASHTAGS WITH #HASHTAG
filtered_retweets['content'] = filtered_retweets['content'].replace("#\\s*[0-9a-zA-Z]+", "#HASHTAG", regex=True)
# REPLACE ALL URLS WITH !URL
filtered_retweets['content'] = filtered_retweets['content'].replace("https?:\\/\\/(www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\\+.~\\-#?&//=]*)", "!URL", regex=True)
filtered_retweets['content'] = filtered_retweets['content'].replace("[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\\+.~\\-#?&//=]*)", "!URL", regex=True)

# REMOVE "
#filtered_retweets['content'] = filtered_retweets['content'].str.replace('^"+', '', regex=True)
#filtered_retweets['content'] = filtered_retweets['content'].str.replace('"+$', '', regex=True)
filtered_retweets['content'] = filtered_retweets['content'].replace('"', '')

filtered_retweets['content'].to_csv("./data.txt", index=False, header=False)
