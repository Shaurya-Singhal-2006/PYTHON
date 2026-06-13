# WAP to ask the user to enter names of their 3 favorite movies & store them in a list

movie1 = input("enter the name of first movie: ")
movie2 = input("enter the name of second movie: ")
movie3 = input("enter the name of third movie: ")

fav_movies = [movie1 , movie2 , movie3]


# another way

# fav_movie = []

# fav_movies.append(movie1)
# fav_movies.append(movie2)
# fav_movies.append(movie3)


# another way

# fav_movies.append(input("enter the first movie: "))
# fav_movies.append(input("enter the second movie: "))
# fav_movies.append(input("enter the third movie: "))


print("the three fav movie of the user are : ",fav_movies)