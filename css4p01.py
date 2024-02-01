# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:31:56 2024

@author: User
"""
import pandas as pd
data = pd.read_csv("C:/Users/User/Desktop/css_2024_uj/movie_dataset.csv", index_col=0)

df = pd.DataFrame(data)
df.dropna(inplace=True)

#Movie with the Highest Rating
highest_rating_movie = df.loc[df['Rating'].idxmax()]
print(highest_rating_movie)

#Average Revenue of All movies in the Dataset
average_movie_revenue = df["Revenue (Millions)"].mean() 
print(f'The average revenue in million is ${average_movie_revenue:.2f}')

'''
average revenue of movies from 2015 to 2017
'''
#create a dataframe for 2015- 2017
df_15_17 = df[(df['Year']>=2015) & (df['Year'] <=2017)]

average_movie_revenue_15_17 = df_15_17["Revenue (Millions)"].mean() 
print(f'The average revenue for movies produced between 2015 and 2017 in million is ${average_movie_revenue_15_17:.2f}')

#How many movies released in 2016
#2016_count = df["Year"]==2016).count()
#count_2016 = (df["Year"] == 2016).count()
#print(f'the number of movies made in 2016 is {count_2016}')
movies_2016_count = (data["Year"] == 2016).sum()
print(f'the number of movies made in 2016 is {movies_2016_count}')


#Hw many movies were made by Chris Nolan 

# Count the number of movies directed by Christopher Nolan
count_nolan_movies = (data["Director"] == "Christopher Nolan").sum()

print(f'Number of movies directed by Christopher Nolan: {count_nolan_movies}')


#movies in the dataset have a rating of at least 8.0

movies_8_rating = (data["Rating"] >= 8.0).sum()
print(f'Number of movies with atleast 8.0 rating: {movies_8_rating}')

#What is the median rating of movies directed by Christopher Nolan?
median_nolan_rating = data[data["Director"] == "Christopher Nolan"]["Rating"].median()

print(f'Median rating of movies directed by Christopher Nolan: {median_nolan_rating}')

# Sort the DataFrame by the "Rating" column for movies directed by Christopher Nolan
sorted_nolan_movies = data[data["Director"] == "Christopher Nolan"].sort_values(by="Rating")

# Calculate the median rating
median_nolan_rating = sorted_nolan_movies["Rating"].median()

print(f'Median rating of movies directed by Christopher Nolan: {median_nolan_rating}')

# the year with the highest average rating
average_rating_by_year = data.groupby("Year")['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print(f'Year with the highest average rating: {year_highest_average_rating} (Average Rating: {highest_average_rating:.2f})')

# percentage increase in number of movies made between 2006 and 2016
# movie_count_2006 = len(data["Year"] == 2006)
# movie_count_2016 = len(data["Year"] == 2016)
# percentage_2006_2016 = (movie_count_2016 - movie_count_2006) *100/movie_count_2006
# print(f'The percentage increase : {percentage_2006_2016:.2f}')

# Filter the DataFrame for movies made in 2006 and 2016
movies_2006 = data[data['Year'] == 2006]
movies_2016 = data[data['Year'] == 2016]

# Calculate the number of movies made in each year
count_movies_2006 = len(movies_2006)
count_movies_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = ((count_movies_2016 - count_movies_2006) / count_movies_2006) * 100

print(f'Percentage increase in the number of movies made between 2006 and 2016: {percentage_increase:.2f}%')

# Create a new DataFrame with each actor in a separate row
actors_df = data['Actors'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True).to_frame('Actor')

# Find the most common actor
most_common_actor = actors_df['Actor'].mode().iloc[0]

print(f'Most common actor in all movies: {most_common_actor}')

#How many unique genres are there in the dataset?
unique_genre = data['Genre'].str.split(',').explode().str.strip()
unique_genre_num = unique_genre.nunique()
print(f' The number of unique genres is {unique_genre_num}')

'''
Do a correlation of the numerical features, what insights can you deduce? 
Mention at least 5 insights.
And what advice can you give directors to produce better movies?
'''

# Select only numeric columns
numeric_cols = data.select_dtypes(include=['number']).columns

# Calculate the correlation matrix
corr_matrix = data[numeric_cols].corr()


