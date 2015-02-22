from Model.Entities.Movie import MovieClass as Movie

class MovieManagerClass():
    """Movie entity manager"""
    
    def ListMovies(self):
        movies = []
        # Add Movies to the list
        movies.append(Movie("d2e008d4-efd9-46fe-8449-b1a3f2bdaf46",
                            "Equilibrium", 
                            "http://upload.wikimedia.org/wikipedia/en/f/f6/Equilibriumposter.jpg", 
                            "https://www.youtube.com/watch?v=ZVDiaYQXBVs",
                            "http://www.imdb.com/title/tt0238380/",
                            "http://en.wikipedia.org/wiki/Equilibrium_(film)",
                            "2002",
                            "107",
                            "Kurt Wimmer"))
        movies.append(Movie("0619b1b0-320e-47ce-aa3d-7472c355c034",
                            "Interstellar", 
                            "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", 
                            "https://www.youtube.com/watch?v=zSWdZVtXT7E",
                            "http://www.imdb.com/title/tt0816692/",
                            "http://en.wikipedia.org/wiki/Interstellar_(film)",
                            "2014",
                            "169",
                            "Christopher Nolan"))
        movies.append(Movie("5d437c09-3ec9-4fde-b901-9231949ce609",
                            "Avatar", 
                            "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
                            "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                            "http://www.imdb.com/title/tt0499549/",
                            "http://en.wikipedia.org/wiki/Avatar_(2009_film)",
                            "2009",
                            "170",
                            "James Cameron"))
        movies.append(Movie("5a8a9a8e-4edb-4745-932e-bd69d030a3e8",
                            "2001: A Space Odyssey", 
                            "http://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg", 
                            "https://www.youtube.com/watch?v=Z2UWOeBcsJI",
                            "http://www.imdb.com/title/tt0062622/",
                            "http://en.wikipedia.org/wiki/2001:_A_Space_Odyssey_(film)",
                            "1968",
                            "161",
                            "Stanley Kubrick"))
        movies.append(Movie("70b2024a-72ec-4401-8b13-299f40bf96f7",
                            "Stargate", 
                            "http://upload.wikimedia.org/wikipedia/en/e/e0/Stargateposter.jpg", 
                            "https://www.youtube.com/watch?v=kiJtZUPvJxY",
                            "http://www.imdb.com/title/tt0111282/",
                            "http://en.wikipedia.org/wiki/Stargate_(film)",
                            "1994",
                            "128",
                            "Roland Emmerich"))
        movies.append(Movie("ba5d5cb1-f9d4-46db-8d2a-56ba1dcd2213",
                            "Tron", 
                            "http://upload.wikimedia.org/wikipedia/en/1/17/Tron_poster.jpg", 
                            "https://www.youtube.com/watch?v=1D3WLzPQK0w",
                            "http://www.imdb.com/title/tt0084827/",
                            "http://en.wikipedia.org/wiki/Tron",
                            "1982",
                            "95",
                            "Steven Lisberger"))
        movies.append(Movie("340105ee-2ed1-4758-9dfe-c2cbc15fb7c8",
                            "Star Wars", 
                            "http://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg", 
                            "https://www.youtube.com/watch?v=vP_1T4ilm8M",
                            "http://www.imdb.com/title/tt0076759/",
                            "http://en.wikipedia.org/wiki/Star_Wars_(film)",
                            "1977",
                            "121",
                            "George Lucas"))
        movies.append(Movie("020120bb-42fd-4159-9219-6ac07479796e",
                            "The Matrix", 
                            "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", 
                            "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                            "http://www.imdb.com/title/tt0076759/",
                            "http://en.wikipedia.org/wiki/The_Matrix",
                            "1999",
                            "136",
                            "The Wachowski Brothers"))
        movies.append(Movie("626e0b99-1efb-43e8-904c-347403a3d3b8",
                            "Terminator 2: Judgment Day", 
                            "http://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg", 
                            "https://www.youtube.com/watch?v=eajuMYNYtuY",
                            "http://www.imdb.com/title/tt0103064/",
                            "http://en.wikipedia.org/wiki/Terminator_2:_Judgment_Day",
                            "1991",
                            "136",
                            "James Cameron"))
        
        return movies