import media
import fresh_tomatoes

the_matrix = media.Movie("The Matrix",
						"Story of a computer hacker with alias neo.",
						"https://www.movieposter.com/posters/archive/main/9/A70-4902",
						"https://www.youtube.com/watch?v=m8e-FF8MsqU")
now_you_see_me = media.Movie("Now You See Me",
							"Story of Magicians who call themselves Horsemen.",
							"http://theimpactnews.com/wp-content/uploads/2013/06/now-you-see-me-poster2.jpg",
							"https://www.youtube.com/watch?v=8MHDYZJWLXA")
#print(the_matrix.storyline)
#the_matrix.show_trailer()
movies = [the_matrix,now_you_see_me]
fresh_tomatoes.open_movies_page(movies)