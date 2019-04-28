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
        "Enter 'a' to add a movie, 'l' to see your movies, and 'f' to find a" +
        " movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("Entry not applicable. Try agaom")

        user_input = input(
            "Enter 'a' to add a movie, 'l' to see your movies, and 'f' to " +
            "find a movie, and 'q' to quit: ")


def add_movie():
    title = input("\nTitle of movie you want to add: ")
    director = input("\nDirector of the movie: ")
    release_year = int(input("\nYear of release: "))

    movies.append({
        'name': title.title(),
        'director': director.title(),
        'year': release_year
    })


def show_movies(movies_list):
    print("\nHere are your movies: \n")
    for movie in movies:
        show_movie_details(movie)


def show_movie_details(movie):
    for item in movies:
        print(f"Name: {item['name']}")
        print(f"Director: {item['director']}")
        print(f"Year: {item['year']}")


def find_movie():
    find_by = input("\nWhat property of the movie are you looking for?")
    # find_by will = either 'year' 'director' or 'title'
    looking_for = input("\nWhat are you searching for?")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])
    show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


menu()


