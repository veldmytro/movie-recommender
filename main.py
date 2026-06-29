import pandas as pd

print("Movie Recommender")
movies_df = pd.read_csv("data/movies.csv")

# Preparing dataset
prepared_df = movies_df[
    ['title', 'genres', 'vote_average', 'release_date', 'overview']
].copy()
prepared_df = prepared_df.dropna(subset = ['overview'])
prepared_df["release_date"] = pd.to_datetime(prepared_df["release_date"])
prepared_df['year'] = prepared_df['release_date'].dt.year
prepared_df = prepared_df.drop(['release_date'], axis=1)

# Merging overviews and genres into one text column combined_ovge for TF-IDFs
prepared_df["genres"] = prepared_df["genres"].fillna("")
prepared_df["combined_ovge"] = (prepared_df["genres"] + " " + prepared_df["overview"])
prepared_df = prepared_df.drop(
    columns=['genres','overview'])
prepared_df.info()