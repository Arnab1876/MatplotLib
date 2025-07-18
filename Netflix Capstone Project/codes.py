# Step-1: Import the libraries..

import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset--

df= pd.read_csv("netflix_titles.csv")

# Cleaning the dataset--

df= df.dropna(subset=['type','release_year','rating','country','duration'])
type_counts=df['type'].value_counts()
plt.figure(figsize=(10, 5))
plt.bar(type_counts.index, type_counts.values, color=['blue', 'orange'])
plt.title('Movies vs TV Shows on Netflix')
plt.xlabel('Content Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('Movies_vs_Shows on Netflix.png') 
plt.show() 




rating_counts = df['rating'].value_counts()
plt.figure(figsize=(10,6))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Distribution of Ratings on Netflix')
plt.tight_layout()
plt.savefig('Distribution of Ratings on Netflix.png')
plt.show()


movie_df=df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace(' min', '').astype(int)
plt.figure(figsize=(10, 6))
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (in minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('Distribution of Movie Durations on Netflix.png')
plt.show()



release_year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.scatter(release_year_counts.index, release_year_counts.values, color='teal')
plt.title('Release Year vs No. of Titles on Netflix')
plt.xlabel('---Release Year---')
plt.ylabel('---Number of Titles---')
plt.tight_layout()
plt.savefig('Release Year vs No. of Titles on Netflix.png')
plt.show()



country_counts=df['country'].value_counts().head(10)
plt.figure(figsize=(12, 6))
plt.barh(country_counts.index, country_counts.values, color='darkcyan')
plt.title('Top 10 Countries with Most Titles on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('Top 10 Countries with Most Titles on Netflix.png')
plt.show()



content_by_year=df.groupby(['release_year', 'type']).size().unstack().fillna(0)
fig,ax= plt.subplots(1,2,figsize=(12, 6))

#First subplot: Movies

ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue', marker='o')
ax[0].set_title('Number of Movies Released Each Year')
ax[0].set_xlabel('--Release Year--')
ax[0].set_ylabel('--Number of Movies--')
#Second subplot: TV Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange', marker='o')
ax[1].set_title('Number of TV Shows Released Each Year')
ax[1].set_xlabel('--Release Year--')
ax[1].set_ylabel('--Number of TV Shows--')
plt.suptitle('Content Released on Netflix Over the Years')
plt.tight_layout()
plt.savefig('Content Released on Netflix Over the Years.png')
plt.show()