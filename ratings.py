"""Restaurant rating lister:

1. Reads the ratings in from the file

2. Stores them in a dictionary

3. And finally, spits out the ratings in alphabetical order by restaurant

"""


# open scores.txt file
file = open('scores.txt')

def restaurant_rating(file):

    # read ratings in from the file
    # store them in a dictionary
    restaurant_ratings = {}


    for restaurant in file:
        
        restaurant_ratings[restaurant] = restaurant_ratings.get(restaurant, 0) + 1
       
    return restaurant_ratings
        

        

    # outputs restaurant ratings in alphabetical order
