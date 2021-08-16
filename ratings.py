"""Restaurant rating lister.

1. Reads the ratings in from the file

2. Stores them in a dictionary

3. And finally, spits out the ratings in alphabetical order by restaurant
"""

def process_file(filepath):
    
    #open the file
    file = open(filepath)
    # empty dictionary 
    restaurant_ratings = {}

    #loop each line of the file
    for line in file:
        #removes any trailing whitespace
        line = line.rstrip()
        words = line.split(":") # words = ["restaurant name", "5"]
        restaurant_ratings[words[0]] = words[1]

    return restaurant_ratings

    
def print_ordered_restaurant_ratings(restaurant_ratings):  
    
    for restaurant in sorted(restaurant_ratings):
        print(f"{restaurant} is rated at {restaurant_ratings[restaurant]}")  


def user_add_restaurant(restaurant_ratings):
    
    rest_name = input("restaurant name: ").title()
    rest_score = input("score: ")

    restaurant_ratings[rest_name] = rest_score

ratings = process_file("scores.txt")  
user_add_restaurant(ratings) 
print_ordered_restaurant_ratings(ratings)
