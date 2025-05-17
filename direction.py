import googlemaps

def find_nearby_places(api_key, origin, destination, place_type='restaurant'):
    gmaps = googlemaps.Client(key=api_key)

    # Step 1: Get directions
    directions_result = gmaps.directions(origin, destination, mode="driving")
    if not directions_result:
        print("Could not find directions.")
        return

    # Step 2: Get destination location
    end_location = directions_result[0]['legs'][0]['end_location']
    lat, lng = end_location['lat'], end_location['lng']

    # Step 3: Find nearby places around the destination
    places_result = gmaps.places_nearby(location=(lat, lng), radius=2000, type=place_type)

    print(f"Nearby {place_type}s near {destination}:")
    for place in places_result['results'][:5]:  # Limit to 5 results
        name = place['name']
        address = place.get('vicinity', 'Address not available')
        rating = place.get('rating', 'No rating')
        print(f"- {name} ({rating}⭐): {address}")

# 🔐 Replace with your real API key
API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"

# 🎯 Example usage
origin = "Times Square, New York, NY"
destination = "Central Park, New York, NY"
find_nearby_places(API_KEY, origin, destination)
