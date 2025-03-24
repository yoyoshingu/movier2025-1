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

rating_df = pd.read_csv("data/ratings.csv")
rating_df['movieId'] = rating_df['movieId'].astype(str)
agg_df = rating_df.groupby('movieId').agg(rcount = ('rating', 'count'), rmean=('rating', 'mean'))
print(agg_df)
merged_df = merged_df.merge(agg_df, on='movieId')
print(merged_df)
print(merged_df.columns)

# step 4 포스터 경로 추가
import requests
from tqdm import tqdm

def add_poster(df):
        for i, row in tqdm(df.iterrows(), total=df.shape[0]):
                tmdb_id = row['tmdbId']
                tmdb_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key=f2a1fddeef038db026fb3e05415e80f2&language=en-US"
                result = requests.get(tmdb_url)
                try:
                        df.at[i, "poster_path"] = "https://image.tmdb.org/t/p/original" + result.json()['poster_path']
                        print(df.at[i, "poster_path"])
                except(TypeError, KeyError) as e:
                        df.at[i, "poster_path"] = "https://image.tmdb.org/t/p/original/p67m5dzwyxWd46a6of2c9IVfQz7.jpg"
        return df

merged_df['poster_path'] = None
merged_df = add_poster(merged_df)
print(merged_df.shape)
merged_df.to_csv("data/movies_final.csv", index=None)

