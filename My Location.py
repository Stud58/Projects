import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number= input("\nEnter Number:")
print()

ch_number = phonenumbers.parse(number,"CH")
number_country = geocoder.description_for_number(ch_number,"en")

service_provider = phonenumbers.parse(number,"RO")
number_provider = carrier.name_for_number(service_provider,"en")

phone_number = phonenumbers.parse(number)
time_zone = timezone.time_zones_for_number(phone_number)

print("\nCountry :",number_country)
print("\nTimeZone and Region:",time_zone)
print("\nService/Carrier provider:",number_provider)