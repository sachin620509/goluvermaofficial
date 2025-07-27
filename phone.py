import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Input phone number with country code
number = input("Enter phone number with country code (e.g. +91 XXXXXXXXXX): ")
phone_number = phonenumbers.parse(number)

# Extract details
print("Timezone:", timezone.time_zones_for_number(phone_number))
print("Location:", geocoder.description_for_number(phone_number, "en"))
print("Carrier:", carrier.name_for_number(phone_number, "en"))