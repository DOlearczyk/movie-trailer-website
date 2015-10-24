from datetime import date
import fresh_tomatoes
import media

# Create a list of movies to show on website
movies=[]
movies.append(media.Movie("Schindler's List", 
                          "In Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.",
                          "http://ia.media-imdb.com/images/M/MV5BMzMwMTM4MDU2N15BMl5BanBnXkFtZTgwMzQ0MjMxMDE@._V1_SX214_AL_.jpg",
                          "https://www.youtube.com/watch?v=JdRGC-w9syA",
                          date(1993, 11, 30)))
movies.append(media.Movie("Star Wars: Episode V - The Empire Strikes Back",
                          "After the rebels have been brutally overpowered by the Empire on their newly established base, Luke Skywalker takes advanced Jedi training with Master Yoda, while his friends are pursued by Darth Vader as part of his plan to capture Luke.",
                          "http://ia.media-imdb.com/images/M/MV5BMjE2MzQwMTgxN15BMl5BanBnXkFtZTcwMDQzNjk2OQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                          "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
                          date(1980, 6, 20)))
movies.append(media.Movie("The Lion King",
                          "Lion cub and future king Simba searches for his identity. His eagerness to please others and penchant for testing his boundaries sometimes gets him into trouble.",
                          "http://ia.media-imdb.com/images/M/MV5BMjEyMzgwNTUzMl5BMl5BanBnXkFtZTcwNTMxMzM3Ng@@._V1_SY317_CR15,0,214,317_AL_.jpg",
                          "https://www.youtube.com/watch?v=GaJWzJfoXlE",
                          date(1994, 6, 24)))

# Display on website defined movies
fresh_tomatoes.open_movies_page(movies)
                          
