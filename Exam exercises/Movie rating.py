numberOfMovies = int(input('Number of movies: '))

#   Variables
averageRating = 0.0
highestRating = 0.0
lowestRating = 10.0
highestRatingName = None
lowestRatingName = None


#   Loop
for i in range(1, numberOfMovies + 1):
    movieName = input('Name of the movie: ')
    movieRating = float(input('Rating: '))
    averageRating += movieRating
    if movieRating > highestRating:
        highestRating = movieRating
        highestRatingName = movieName
    if movieRating < lowestRating:
        lowestRating = movieRating
        lowestRatingName = movieName
averageRating /= numberOfMovies

#   Output
print(f'{highestRatingName} is with highest rating: {highestRating:.1f}')
print(f'{lowestRatingName} is with lowest rating: {lowestRating:.1f}')
print(f'Average rating: {averageRating:.1f}')
