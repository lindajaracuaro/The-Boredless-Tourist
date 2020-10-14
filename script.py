destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
attractions = [ [] for destination in range(len(destinations))]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attraction(destination, attraction):
  try: 
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
    return
  except ValueError:
    return
    
# ADD ATTRACTIONS
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction[0]
    attraction_tags = attraction[1]
    for tag in attraction_tags:
      for interest in interests:
        if interest == tag:
          attractions_with_interest.append(possible_attraction)
  return attractions_with_interest
  
def get_attractions_for_traveler(traveler):
  traveler_name = traveler[0]
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  traveler_attractions_formatted = ""
  for attraction in range(len(traveler_attractions)):
    traveler_attractions_formatted += str(traveler_attractions[attraction])
    if attraction < len(traveler_attractions) -1 :
      traveler_attractions_formatted += ", "
  interests_string = "Hi " + str(traveler_name) + ", we think you'll like these places around " + str(traveler_destination) + ": " + str(traveler_attractions_formatted) + "."
  return interests_string

# TEST TRAVELERS
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
smills_france = ['Dereck Smill', 'Paris, France', ['monument']]
print(get_attractions_for_traveler(smills_france))
print(get_attractions_for_traveler(test_traveler))
