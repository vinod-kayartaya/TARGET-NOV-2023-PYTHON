"""
Make api calls using `requests` library
"""
import requests

url = 'https://omdbapi.com'
apikey = 'aa9e49f'

def fetch_movies(title: str, page: int = 1) -> list:
    args = {'apikey': apikey, 's': title, 'page': page}
    resp = requests.get(url, params=args)
    if resp.status_code == 200:
        data = resp.json()
        return data['Search']

def fetch_movie_actors(imdbId) -> list:
    params = dict(apikey=apikey, i=imdbId)
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        return resp.json()['Actors'].split(', ')

def main():
    title = input('Enter part of a movie title: ')
    page = int(input('Enter page number: '))
    movies = fetch_movies(title, page)
    for movie in movies:
        actors = fetch_movie_actors(movie['imdbID'])
        print(f'{movie["Title"]} --> {actors}')


if __name__ == '__main__':
    main()
