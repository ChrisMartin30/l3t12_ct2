# Readme for L3 T12 - compulsory task 2

## Task aim
The task given was: 

Let us build a system that will tell you what to watch next based on the word
vector similarity of the description of movies.
* Create a file called watch_next.py
* Read in the movies.txt file. Each separate line is a description of a different movie.
* Your task is to create a function to return which movies a user would watch next if they have watched Planet Hulk with the description “Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.”
* The function should take in the description as a parameter and return the title of the most similar movie.
* Host your solution on a Git host such as GitLab or GitHub with a Dockerfile and instructions to run included.
    * If it doesn’t already, please ensure that your repo includes a file named requirements.txt to automate the installation of the project’s requirements.
    * Remember to exclude any venv or virtualenv files from your repo.
* Add the link for your remote Git repo to your semantic_similarity.txt file.

Therefore the [**watch_next.py**](/watch_next.py) file was created.

It uses the [SpaCy](https://spacy.io) NLP and the more advanced language model of **en_core_web_md** to compare the similarity of the movie description to those in the provided file.

The python program contains a function that, when a movie description is used, accesses the information within the movies.txt file, then uses a *for* loop to iterate through the various decriptions, comparing each decription to that of the provided description, and retaining the highest ranked one.

Once all items in the file have been compared to the provided description, it prints the title of the movie that it has determined to be the most similar.

### Drawbacks
This, when using the description provided for having watched a Hulk superhero movie, recommended a movie about intrigue at a dance company, rather than the Superman movie which was also available in the file.

To try to refine the process, words that SpaCy classes as ["stop words"](https://spacy.io/usage/spacy-101#section-language-data), which are commonly used words that it may be useful to filter out, were removed from both the provided description and the descriptions in the file.

The function was then re-run and it did recommend a different movie. However, this time it also does not recommend the superhero movie, rather one with a quest, dying mother, and world ending.

### Reasons for differences
I can only speculate why it failed to recommend what I think is the most similar movie to the Hulk.
* One reason is that it is recommending the most similar movie based on purely on the decription given; it did not fail to recommend the superhero movie because that is not the most **similar** going by the definition of the model. 
* The model used, [en_core_web_md](https://spacy.io/models/en), is only the medium pipeline. A larger model may give different recommendations.
* The model used is trained on written text such as blogs, news and comments. Perhaps a more "movie" focussed model would give different recommendations.
* The descriptions given vary in length and complexity. However they are still only a few sentences in length. Longer, more accurate, descriptions may give different results.

### Further improvements
Possible improvements - other than the use of a larger or more movie focussed model, or more movies to recommend in the movies.txt - could be allowing user input to determine movie description.
