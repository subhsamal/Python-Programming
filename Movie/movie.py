import webbrowser

class Movie():
    def __init__ (self, movie_title, movie_storyline, poster_image, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.image = poster_image
        self.trailer = youtube_trailer

    def play_trailer(self):
        webbrowser.open(self.trailer)
