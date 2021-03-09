from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2"

# load url
response = requests.get(URL)
response.raise_for_status()
movie_html = response.text

# parse through BS4
soup = BeautifulSoup(movie_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
all_titles = [movie.getText() for movie in all_movies]
rev_titles = all_titles[::-1]

# create a file with a list of the movies
with open("movies.txt", mode="w") as file:
    for title in rev_titles:
        file.write(f"{title}")
