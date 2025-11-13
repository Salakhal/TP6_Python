from film import Film

film1 = Film("Matrix", "Wachowski", 1999, 8.7)
film2 = Film("Inception", "Christopher Nolan", 2010, 9.0)
film3 = Film("Le Seigneur des Anneaux", "Peter Jackson", 2001, 8.8)

films = [film1, film2 , film3]
films_tries = sorted(films, key=lambda f: f.note)


for f in films_tries:
    print(f.to_json())
