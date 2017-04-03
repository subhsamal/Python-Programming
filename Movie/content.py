import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story-3",
                        "Story of a boy and his toy",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcRUAG6E1nL4GRxsB1G5upnKfQVgm8zeILqd_EbN-2kjMeZZPcah",
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
                   "http://t3.gstatic.com/images?q=tbn:ANd9GcS3OOr06uE3lEZwum5WxKkkdsC37ObLwjKZgSSx-V96yrt6DhKE",
                   "https://www.youtube.com/watch?v=2onxgmKT1fw")
print (kong.storyline)
#kong.play_trailer()

avengers = movie.Movie("Avengers -2",
                       "Infinity War",
                       "http://media.comicbook.com/2017/03/avengers-infinity-war-238299.jpg",
                       "https://www.youtube.com/watch?v=Ptfk0TF9MF0")
print (avengers.storyline)
#avengers.play_trailer()

deadpool = movie.Movie("Deadpool -2",
                       "Deadpool -2",
                       "http://img.cinemablend.com/cb/a/9/a/d/5/5/a9ad5581630dc20adc5413fcc4e9ca44e9b1bc063ffa97b7ca26ab870ded2552.jpg",
                       "https://www.youtube.com/watch?v=Tpo9WYxLdLY")
print (deadpool.storyline)
#deadpool.play_trailer()

movies_list = [toy_story, avatar, kong, avengers, deadpool]
fresh_tomatoes.open_movies_page(movies_list)
