#simple movie recommendation system

movies = {
    "action": ["Mad Max: Fury Road", "John Wick", "The Dark Knight"],
    "comedy": ["The Hangover", "Superbad", "21 Jump Street"],
    "romance": ["La La Land", "The Notebook", "Me Before You"],
    "horror": ["The Conjuring", "Insidious", "A Quiet Place"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix"]
}

print("Welcome to the movie recommendor!")
print("\nGenres: " " " .join(movies.keys()))

genre = input("Enter a genre you like: ").lower()

if genre in movies :
    print("\nRecommended movies for you:")
    for m in movies[genre]:
         print(m)
        
else: 
    print("\nSorry, that genre is not available. ")        