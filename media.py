
"""
Creation of Movie class , #init is a reserved method in python, also known as
Constructor of the class, self is an instance of the class that allows us to
access attributes and methods such (movie, trailer, title) of the class.
"""
class Movie ():      
     def __init__ (self, movie_title, movie_storyline, poster_image, movie_trailer_youtube): 

        self.title = movie_title  
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url= movie_trailer_youtube




"""
show_trailer is a function block,
webbrowser is a module that allows the webbased document to open, in this case
we will open trailer.

"""
def show_trailer(self):
    webbrowser.open(self.trailer_url)
