# Compulsory Task 2

# Read in file movies.txt

with open("movies.txt", "r") as f_movies:
    movies = f_movies.readlines()

for i in movies:
    print(i)


# Create a function that will return a movie recommendation based on the description
#  of their previous movie. Function should take in description as parameter and 
# return the title of most similar movie.


# Import spacy and appropriate language model
import spacy
nlp = spacy.load('en_core_web_md')


# Create function that compares description to each movie in movies.txt
#   File has lines of "Movie :description", so find index of first colon 
# of each line and split at that point.
#   Use NLP to search for similarity, return whichever movie in file has the 
# greatest similarity.

def film_finder(description):
    try:
        with open("movies.txt", "r") as f_movies:
            movies = f_movies.readlines()
    except FileNotFoundError:
        print("The movie list could not be found")
    
    film_name = ""
    film_desc = ""
    film_rate = 0

    viewed_film = nlp(description)
    rec_film = ""

    for film in movies:
        colon = film.find(":")
        film_name = film[:colon]
        film_desc = film[colon + 1:]
        similarity = nlp(film_desc).similarity(viewed_film)
        # print(f"{film_name} : {similarity} \n{film_desc}\n")
        if similarity > film_rate:
            rec_film = film_name
            film_rate = similarity
    
    return rec_film


# Watched movie and description

watched = "Planet Hulk"
watched_description = """Will he save their world or destroy it? When the Hulk 
becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and 
launch him into space to a planet where the Hulk can live in peace. Unfortunately 
Hulk land on the planet SaKaar where he is sold into slavery and trained as a gladiator."""


print(f"As you have watched {watched}, the recommended next film is : \n", film_finder(watched_description))


# As it returns a somewhat unusual result, not recommending another 
# superhero movie, will refine function by removing stopwords from 
# movie descriptions.

def ref_film_finder(description):
    try:
        with open("movies.txt", "r") as f_movies:
            movies = f_movies.readlines()
    except FileNotFoundError:
        print("The movie list could not be found")
    
    film_name = ""
    film_desc = ""
    film_rate = 0

    viewed_film = nlp(description)
    ref_viewed_film = nlp(' '.join([str(t) for t in viewed_film if not t.is_stop]))
    rec_film = ""

    for film in movies:
        colon = film.find(":")
        film_name = film[:colon]
        film_desc = nlp(film[colon + 1:])
        ref_film_desc = nlp(' '.join([str(t) for t in film_desc if not t.is_stop]))
        similarity = nlp(ref_film_desc).similarity(ref_viewed_film)
        # print(f"{film_name} : {similarity} \n{film_desc}\n{ref_film_desc}")
        if similarity > film_rate:
            rec_film = film_name
            film_rate = similarity
    
    return rec_film

print(f"As you have watched {watched}, the refined recommendation for the next film is : \n", ref_film_finder(watched_description))