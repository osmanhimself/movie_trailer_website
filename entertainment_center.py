import fresh_tomatoes
import media
"""
Above import statement allow to find the module, loads and initialize the modul
e it defines a name of names in the local namespace (folder) for the scope
where import statement happens
"""
"""
Martian is a instance that calls Movie class, calls out init function thats
being created in this case "martian", next it calls instance variables
movie_title,movie_storylin,movie_image,movie,trailer """
martian = media.Movie("Martian", "A Man trying to survive Mars",
                      "https://bit.ly/2Iwub0S",
                      "https://www.youtube.com/watch?v=ej3ioOneTy8")


godfather = media.Movie("GodFather 2",
                        "A Man with a mission",
                        "http://www.movienewsletters.net/photos/071112R1.jpg",
                        "https://www.youtube.com/watch?v=BpzVFdDeWyo")

inception = media.Movie("inception",
                        "matrix on steroids",
                        "https://bit.ly/2J2OAKy",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

interstellar = media.Movie("interstellar",
                           "A Mission to Wider Universe",
                           "https://bit.ly/1JReOr0",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

Dunkirk = media.Movie("Dunkirk",
                      "Story of WW2",
                      "https://bit.ly/2rWcFsI",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

Shrek = media.Movie("Shrek",
                    "Story of Ogre named Shrek",
                    "https://bit.ly/2Lf6qbm",
                    "https://www.youtube.com/watch?v=W37DlG1i61s")
"""
[ ] creates a matrix or array of all the movies , frest tomatoes calls
out the instance of movies defined in array
"""
movies = [martian, godfather, inception, interstellar, Dunkirk, Shrek]
fresh_tomatoes.open_movies_page(movies)
# print(movie-name.storyline) --prints storyline of the movie
# print(movie-name.title) -- will print title of the movie
