# milestone one - movie filing system


""""
- must allow to add new movies to collection
- must allow users to view all the movies in the collection
- allow user to find movie by any attribute


[] - tell user options: 'a' - add, 's' - show, 'f' - find, 'q' - quit program
[x] - what format is a movie ~~~~~list of dicts
[x] - decide where to store movies

- Functions -
[] - create add_movie
[] - create show_movie
[] - create find_movie
[]

"""
movies = []


def menu():
    user_input = input(
        "Enter 'a' to add a movie, 'l' to see your movies, and 'f' to find a movie: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie()
        elif user_input == 'f':
            find_movie()
        else:
            print("Entry not applicable. Try agaom")


def add_movie():
    title = input("\nTitle of movie you want to add: ")
    director = input("\nDirector of the movie: ")
    release_year = input("\nYear of release: ")
    movie = dict('Title'=title, 'Director'=director, 'Release Year'=release_year)
