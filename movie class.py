import os

searching = True

def clear():   
    os.system('cls' if os.name == 'nt' else 'clear')

class Movie:
    
    listed = []
    
    def __init__(self, title, release_year, director, rating, genre, cast):
        self.title = title
        self.release_year = release_year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast
        Movie.listed.append(self)
        
    def __str__(self):
        return f"Title: {self.title} \nRelease Year: {self.release_year} \nDirector: {self.director} \nRating: {self.rating} \nGenre: {self.genre} \nCast: {self.cast}"
        
    def info(self, title):
        
        for item in Movie.listed:
            
            if item.title == title:
                
                return Movie.__str__(item)
        
    def genre(self, genre):
        
        genre_list = []
        
        for item in Movie.listed:
            
            if item.genre == genre:
                
                genre_list.append(item.title)
        
        return genre_list
        
    def director(self, director):
        
        director_list = []
        
        for item in Movie.listed:
            
            if item.director == director:
                
                director_list.append(item.title)
        
        return director_list
        
    def cast(self, actor):
        
        actor_list = []
        
        for item in Movie.listed:
            
            if actor in item.cast:
                
                actor_list.append(item.title)
        
        return actor_list
        
    def alphabetize(self):
        
        alpha_list = []
        
        for item in Movie.listed:
            alpha_list.append(item.title)
            
        alpha_list.sort()
            
        return alpha_list
        
    def chronologize(self):

        year_list = []
        chrono_list = []

        for item in Movie.listed:
            year_list.append(item.release_year)

        year_list.sort()

        for year in year_list:

            for item in Movie.listed:
    
                if item.release_year == year:
                    chrono_list.append(item.title)

        return chrono_list
        
        
        
                
                
       
for i in range(1): #make collapsable
    movie1 = Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"])
    
    movie2 = Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta", "Uma Thurman", "Samuel L. Jackson"])
    
    movie3 = Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"])
    
    movie4 = Movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"])
    
    movie5 = Movie("The Matrix", 1999, "Lana and Lilly Wachowski", "R", "Sci-Fi", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"])
    
    movie6 = Movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", ["Tom Hanks", "Robin Wright", "Gary Sinise"])
    
    movie7 = Movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", ["Christian Bale", "Heath Ledger", "Aaron Eckhart"])
    
    movie8 = Movie("Schindler's List", 1993, "Steven Spielberg", "R", "Drama", ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"])
    
    movie9 = Movie("Fight Club", 1999, "David Fincher", "R", "Drama", ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"])
    
    movie10 = Movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", ["Robert De Niro", "Ray Liotta", "Joe Pesci"])
    
    movie11 = Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", ["Jodie Foster", "Anthony Hopkins", "Scott Glenn"])
    
    movie12 = Movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"])
    
    movie13 = Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", ["Elijah Wood", "Ian McKellen", "Orlando Bloom"])
    
    movie14 = Movie("Gladiator", 2000, "Ridley Scott", "R", "Action", ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"])
    
    movie15 = Movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", ["Tom Hanks", "Michael Clarke Duncan", "David Morse"])
    
    movie16 = Movie("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", ["Tom Hanks", "Matt Damon", "Tom Sizemore"])
    
    movie17 = Movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", ["Sam Neill", "Laura Dern", "Jeff Goldblum"])
    
    movie18 = Movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson"])
    
    movie19 = Movie("The Lion King", 1994, "Roger Allers and Rob Minkoff", "G", "Animation", ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"])
    
    movie20 = Movie("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", ["Jim Carrey", "Kate Winslet", "Kirsten Dunst"])
    
    movie21 = Movie("Inglourious Basterds", 2009, "Quentin Tarantino", "R", "War", ["Brad Pitt", "Christoph Waltz", "Mélanie Laurent"])
    
    movie22 = Movie("The Sixth Sense", 1999, "M. Night Shyamalan", "PG-13", "Thriller", ["Bruce Willis", "Haley Joel Osment", "Toni Collette"])
    
    movie23 = Movie("The Usual Suspects", 1995, "Bryan Singer", "R", "Mystery", ["Kevin Spacey", "Gabriel Byrne", "Chazz Palminteri"])
    
    movie24 = Movie("Memento", 2000, "Christopher Nolan", "R", "Thriller", ["Guy Pearce", "Carrie-Anne Moss", "Joe Pantoliano"])
    
    movie25 = Movie("Braveheart", 1995, "Mel Gibson", "R", "Biography", ["Mel Gibson", "Sophie Marceau", "Patrick McGoohan"])
    
    movie26 = Movie("The Terminator", 1984, "James Cameron", "R", "Sci-Fi", ["Arnold Schwarzenegger", "Linda Hamilton", "Michael Biehn"])
    
    movie27 = Movie("Back to the Future", 1985, "Robert Zemeckis", "PG", "Adventure", ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"])
    
    movie28 = Movie("Alien", 1979, "Ridley Scott", "R", "Horror", ["Sigourney Weaver", "Tom Skerritt", "John Hurt"])
    
    movie29 = Movie("The Truman Show", 1998, "Peter Weir", "PG", "Drama", ["Jim Carrey", "Laura Linney", "Noah Emmerich"])

clear()
       
while searching == True:
    
    clear()

    action = input("Would you like to: \n\
a. Print movie information\n\
b. Search genre\n\
c. Search director\n\
d. Search cast\n\
e. See movies in alphabetical order\n\
f. See movies in chronological order\n\n")

    
    if action == "a":
        
        movie = input("\nWhich movie?: ")
        
        print()
        print(Movie.info(Movie, movie.title()))
        
    elif action == "b":
        
        genre_choice = input("\nWhich genre?: ")
        
        genre_search = Movie.genre(Movie, genre_choice.lower().capitalize())
        
        print("\nMovies in the", genre_choice, "genre include:\n")
        print(genre_search)
        
    elif action == "c":
        
        director_choice = input("\nWhich director?: ")
        
        director_search = Movie.director(Movie, director_choice.lower().title())
        
        print("\nMovies directed by", director_choice.lower().title(), "include:\n")
        print(director_search)
        
    elif action == "d":
        
        actor_choice = input("\nWhich actor?: ")
        
        actor_search = Movie.cast(Movie, actor_choice.lower().title())
        
        print()
        print(actor_choice.lower().title(), "has appeared in:\n")
        print(actor_search)
        
    elif action == "e":
        
        print()
        print("Here is the list of movies in alphabetical order:\n")
        print()
        print(Movie.alphabetize(Movie))
        
    elif action == "f":

        print("\nHere is the list of movies listed by order of release, from earliest to latest:\n")
        print(Movie.chronologize(Movie))

    action_2 = input("\nWould you like to continue searching? (y/n): ")

    if action_2 == "y":
        clear()

    elif action_2 == "n":
        clear()
        print("Have a great day!")
        searching = False