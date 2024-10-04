"""
In VSCode build a class for a movie. Remember movies need to have titles, release year, director, rating, genre and cast.
"""
class Movie:
    
    #list of movies
    movie_list[]

    # create movie information
    def __init__(self, title, release_year, director, rating, genre, cast):
       self.title = title
       self.release_year = release_year
       self.director = director
       self.rating = rating
       self.genre = genre
       self.cast = cast
       Movie.movie_list.append(self)

    # make movie info printable
    def __str__(self):
       return f"Title: {self.title} \nRelease Year: {self.release_year} \nDirector: {self.director} \nRating: {self.rating} \nGenre: {self.genre} \nCast: {self.cast}"
    
    def cast(self):
       return self.cast
    
    def genre(self, title):
       
       for item in movie_list:
          
          if title == item.title:
             return item.genre
    
    def director(self):
       return self.director
    

# Movie List
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


print(genre())