import movie

toy_story = movie.Movie("Toy Story-3",
                        "Story of a boy and his toy",
                        "https://en.wikipedia.org/wiki/Toy_Story_3#/media/File:Toy_Story_3_poster.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")  #module/filename. classname

#print (toy_story.storyline)
#toy_story.play_trailer()

avatar = movie.Movie("Avatar-2",
                     "Return to Pandora - A sequel to Avatar",
                     "http://vignette1.wikia.nocookie.net/jamescameronsavatar/images/4/40/Avatar2logo.jpg/revision/latest?cb=20160414215211",
                     "https://www.youtube.com/watch?v=vGNGGBzaNQ0")
#print ("\n")
#print (avatar.storyline)

kong = movie.Movie("Kong - Skull Island",
                   "Kong - Skull Island - For the ride at Islands of Adventure",
                   "https://en.wikipedia.org/wiki/Kong:_Skull_Island#/media/File:Kong_Skull_Island_poster.jpg",
                   "https://www.youtube.com/watch?v=2onxgmKT1fw")
print (kong.storyline)
kong.play_trailer()
