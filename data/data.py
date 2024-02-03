import requests as req
from connect_db import COLLECTION

data = req.get("https://datasets-server.huggingface.co/rows?dataset=AIatMongoDB%2Fembedded_movies&config=default&split=train&offset=0&length=100")

json_movies = data.json()
data_movies = json_movies["rows"]

clean_data_movies = []
for movie in data_movies:
    movie_data = movie["row"]
    if movie_data["awards"]["nominations"] > 0:
        movie_data["price"] = 299
    else:
        movie_data["price"] = 199
    movie_data.pop("plot_embedding", None)
    movie_data.pop("writers", None)
    movie_data.pop("countries", None)
    movie_data.pop("awards", None)
    movie_data.pop("type", None)
    movie_data.pop("metacritic", None)
    movie_data.pop("languages", None)
    movie_data.pop("num_mflix_comments", None)
    movie_data.pop("imdb", None)
    movie_data.pop("runtime", None)
    movie_data.pop("rated", None)
    movie_data["status"] = "available"
    movie_data["image_url"] = movie_data.pop("poster", None)
    clean_data_movies.append(movie_data) 

if COLLECTION.find_one({}) is not None:
    print("Ya se insertaron las peliculas")
else:
    res = COLLECTION.insert_many(clean_data_movies)
    print("IDs:", res.inserted_ids)
# res = COLLECTION.delete_many({})