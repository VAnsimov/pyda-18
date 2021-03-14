# Скачайте с сайта https://grouplens.org/datasets/movielens/ датасет любого размера. Определите какому фильму было
# выставлено больше всего оценок 5.0.

import pandas

def main():
    print_ratings()

def print_ratings():
    ratings_MovieId = get_ratings_MovieId(5)
    moveies = get_move(ratings_MovieId)
    print(moveies)

def get_ratings_MovieId(value: int) -> pandas.Series:
    ratings = pandas.read_table(
        '10_base_pandas/task_01/ratings.dat',
        names=['UserID', 'MovieID', 'Rating', 'Timestamp'],
        sep='::',
        engine='python'
    )
    return ratings[ratings['Rating'] == value]['MovieID']

def get_move(ratings_MovieId: pandas.Series) -> pandas.DataFrame:
    moveies = pandas.read_table('10_base_pandas/task_01/movies.dat', names=['MovieID', 'Title', 'Genres'], sep='::', engine='python')
    return moveies[moveies['MovieID'] == ratings_MovieId[0]]

main()
