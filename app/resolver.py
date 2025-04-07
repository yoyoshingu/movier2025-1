import pandas as pd

def random_items():
    movies_df = pd.read_csv("data/movies_final.csv")
    movies_df = movies_df.fillna('')
    result_items = movies_df.sample(n=10).to_dict("records")
    return result_items

def random_genres_items(genre):
    movies_df = pd.read_csv("data/movies_final.csv")
    genre_df = movies_df[ movies_df['genres'].apply(lambda x: genre in x.lower())]
    genre_df = genre_df.fillna('')

    # Todo 선택한 장르의 갯수가 5보다 작은경우 처리해야함 : 2025.3.31 이용희
    # genre_df.size, len(genre_df), genre_df.shape

    nitem = min(5, genre_df.size)  # genre_df.shape[0] : 크기. [1]: 칼럼갯수
    result_items = genre_df.sample(n=nitem).to_dict("records")
    return result_items

# Todo1 지정된 장르를 포함하는 영화중 평점이 높은 5개의 영화를 추천함,
# 단 추천인수가 5명이상 - done
def random_genres_items_best(genre):
    movies_df = pd.read_csv("data/movies_final.csv")
    genre_df = movies_df[ movies_df['genres'].apply(lambda x: genre in x.lower())]
    genre_df = genre_df[genre_df['rcount']>=5]
    genre_df = genre_df.sort_values(by = 'rmean', ascending=False)
    genre_df = genre_df.fillna('')

    # Todo2 선택한 장르의 갯수가 5보다 작은경우 처리해야함 -done
    result_items = genre_df.head(5).to_dict("records")
    return result_items