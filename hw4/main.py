#%%

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import csv
from textblob import TextBlob
from wordcloud import WordCloud
from social_media_analysis import extract_hashtags,extract_mentions, clean_post_content, get_sentiment, get_avg_engagement

data = pd.read_csv('social_media_posts.csv')
df = pd.DataFrame(data)

text = df['post_content'].to_string()
hashtags = extract_hashtags(text)

wc = WordCloud(width=800, height=400).generate(' '.join(hashtags))
plt.figure(figsize=(10,5))
plt.imshow(wc)
plt.axis('off')
plt.show()


# df['month'] = pd.to_datetime(df['post_date']).dt.month
# df['day'] = pd.to_datetime(df['post_date']).dt.day

# count = df.groupby(['month']).size().reset_index(name="count").plot(title="Monthly Posts", legend=True)

# plt.scatter(df['likes'], df['shares'])
# plt.title("Likes vs Shares")
# plt.xlabel("likes")
# plt.ylabel("shares")
# plt.show()

# print(extract_hashtags(df.get('post_content').to_string()))
# print(get_avg_engagement(df)

# text = df['post_content']
# print(text)

# sentiment_list = []

# for row in df['post_content']:
#     sentiment_list.append(get_sentiment(str(row)))

# df['polarity'] = sentiment_list


# average = df.groupby('user_id').agg(
#     Avg_Polarity=('polarity', 'mean'),
# ).reset_index()

# average_df = pd.DataFrame(average)
# # print(average_df)

# plt.bar(average_df['user_id'], average_df['Avg_Polarity'])
# plt.xlabel("user_id")
# plt.ylabel("polarity")
# plt.title("Average Sentiment per User")
# plt.show()


# %%
