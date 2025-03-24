import pandas as pd

movies_df = pd.read_csv("data/movies.csv")
print(movies_df)
links_df = pd.read_csv("data/links.csv", dtype=str)

movies_df['movieId'] = movies_df['movieId'].astype(str)

merged_df = movies_df.merge(links_df, on='movieId', how='left')
print(merged_df)
print(merged_df.columns)

def add_url(row):
        return f'https://www.imdb.com/title/tt{row}/'

merged_df['url'] = merged_df['imdbId'].apply(lambda x: add_url(x))
print(merged_df)