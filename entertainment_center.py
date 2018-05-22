import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://image.tmdb.org/t/p/w300_and_h450_bestv2/rhIRbceoE9lR4veEXuwCC2wARtG.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
avatar = media.Movie("Avatar",
                     "A hybrid human-alien called an Avatar is created to facilitate communication with the indigenous Na'vis from the planet Pandora and pave the way for ",
                     "https://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
titanic= media.Movie("Titanic",
                     "Titanic is a 1997 American epic romance-disaster film directed, written, co-produced and co-edited by James Cameron",
                     "https://images-na.ssl-images-amazon.com/images/I/51n%2BW2kt8DL.jpg",
                     "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")
spirited_away = media.Movie("Spirited Away",
                            "test",
                                "http://www.impawards.com/2002/"
                                "posters/spirited_away.jpg",
                                "https://www.youtube.com/watch?v=ByXuk9QqQkk")

akira = media.Movie("Akira",
                    "test",
                        "https://s-media-cache-ak0.pinimg.com/736x/"
                        "60/81/5e/60815e5067ce8be81c8297655abdd019"
                        "--akira-film-akira-poster.jpg",
                        "https://www.youtube.com/watch?v=pC6Qk5XxGIY")

princess_mononoke = media.Movie("Princess Mononoke",
                                "test",
                                    "http://img12.deviantart.net/ee3c/i/2016/"
                                    "093/e/8/princess_mononoke__alternative_m"
                                    "ovie_poster_by_marioredsigns-d9xm2lk.jpg",
                                    "https://www.youtube.com/watch?"
                                    "v=4OiMOHRDs14")

porco_rosso = media.Movie("Porco Rosso",
                          "test",
                              "http://img.moviepostershop.com/"
                              "porco-rosso-movie-poster-1992-1020670123.jpg",
                              "https://www.youtube.com/watch?v=awEC-aLDzjs")

castle_in_the_sky = media.Movie("Castle in the sky",
                                "test",
                                    "https://thespectatorial.files."
                                    "wordpress.com/2013/12/castleinthesky.jpg",
                                    "https://www.youtube.com/watch?"
                                    "v=McM0_YHDm5A")

ponyo = media.Movie("Ponyo",
                    "test",
                        "https://cdn.traileraddict.com/content"
                        "/walt-disney-pictures/ponyo-5.jpg",
                        "https://www.youtube.com/watch?v=CsR3KVgBzSM")
#print(toy_story.storyline)
#print(avatar.storyline)
#titanic.show_trailer()
movies = [toy_story,
          avatar,
          titanic,
          spirited_away,
          akira,
          princess_mononoke,
          porco_rosso,
          castle_in_the_sky,
          ponyo]
    
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
