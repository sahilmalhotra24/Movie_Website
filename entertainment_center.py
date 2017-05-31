# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")



Dhoom3 = media.Movie("Dhoom 3",
                     "a story about theif",
                     "https://upload.wikimedia.org/wikipedia/en/f/f1/Dhoom_3_Film_Poster.jpg",
                      "https://www.youtube.com/watch?v=tAuv30PgAck")


school_of_rock = media.Movie("School of rock",
                     "using rock music to learn",
                     "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                      "https://www.youtube.com/watch?v=t4VASf8yeIU")

bajrangi = media.Movie("bajrangi Bhaijan",
                     "Bajrangi Bhaijan",
                     "https://shyfyy.files.wordpress.com/2015/06/bajrangibhaijaan3.jpg",
                      "https://www.youtube.com/watch?v=dWeb_ZUHErA")
avtar = media.Movie("AVTAR",
                     "Avtar",
                     "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRWMlB8l4luuMZpmyNutaV6WFuYdy61YgRz8_NbzDHYckEwPB21",
                      "https://www.youtube.com/watch?v=l7Ltbmvx5VI")


Raees = media.Movie("raees",
                     "a story about theif",
                     "http://media1.bollywoodhungama.in/wp-content/uploads/2016/03/Raees1-1-306x393.jpg",
                      "https://www.youtube.com/watch?v=J7_1MU3gDk0&t=61s")




movies = [toy_story,Dhoom3,school_of_rock,bajrangi,avtar,Raees]
fresh_tomatoes.open_movies_page(movies)
#Uses list of movie instances as input to generate an HTML file and open it in the browser.
