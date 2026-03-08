def get_name(city_name, band_member_list):
    return city_name + ' ' + ''.join(letter.upper() for letter in band_member_list)


name_of_city = input("Enter the city where you grew up: ")
name_of_members = input("Enter the band member's names (comma-separated): ").split(',')
members_list = [name.strip()[0] for name in name_of_members]

name_of_band = get_name(name_of_city, members_list)
print(name_of_band)
