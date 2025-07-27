from opencage.geocoder import OpenCageGeocode

key = 'YOUR_API_KEY'
geocoder = OpenCageGeocode(key)

# Forward geocoding
results = geocoder.geocode('Mushahari, Bihar, India')
print(results[0]['geometry'])

# Reverse geocoding
location = geocoder.reverse_geocode(26.12, 85.45)
print(location[0]['formatted'])