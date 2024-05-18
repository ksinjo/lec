country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆
# def add_new_country(n,v,c):
#     n_country = {}
#     travel_log["country"] = n 
#     travel_log["visits"] = v 
#     travel_log["cities_visited"] = c  
#     travel_log.append(n_country)

def add_new_country(n,v,c):
  new_country = {}
  new_country["country"] = n
  new_country["visits"] = v
  new_country["cities"] = c
  travel_log.append(new_country)  
# TODO: Write the function that will allow new countries
# to be added to the travel_log. 


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")