from geolocation import GeoLocation
from info import Place


def make_eiffel():
    eiffel_name = "Eiffel Tower"
    eiffel_address = "Eiffel Tower, 75007 Paris, France"
    eiffel_tag = "France Tower"
    eiffel_location = GeoLocation(48.859556, 2.294441)
    return Place(eiffel_name, eiffel_address, eiffel_tag, eiffel_location)


def make_louvre():
    louvre_name = "Louvre Museum"
    louvre_address = "Cour Carrée, 75001 Paris, France"
    louvre_tag = "France Museum"
    louvre_location = GeoLocation(48.860717, 2.337708)
    return Place(louvre_name, louvre_address, louvre_tag, louvre_location)


def make_needle():
    needle_name = "Space Needle"
    needle_address = "Queen Anne, Seattle, WA 98109"
    needle_tag = "Seattle Tower"
    needle_location = GeoLocation(47.620761, -122.348531)
    return Place(needle_name, needle_address, needle_tag, needle_location)


def make_liberty():
    liberty_name = "Statue of Liberty"
    liberty_address = "Liberty Island, New York, NY 10004"
    liberty_tag = "New York Monument"
    liberty_location = GeoLocation(40.689355, -74.044468)
    return Place(liberty_name, liberty_address, liberty_tag, liberty_location)


def make_pisa():
    pisa_name = "Leaning Tower of Pisa"
    pisa_address = "56126 Pisa, Province of Pisa, Italy"
    pisa_tag = "Italy Tower"
    pisa_location = GeoLocation(43.723099, 10.396629)
    return Place(pisa_name, pisa_address, pisa_tag, pisa_location)


def search(search_geolocation):
    locations = [make_eiffel(), make_louvre(), make_needle(), make_liberty(), make_pisa()]

    for i in range(0, 1):
        if search_geolocation == locations[0].location:
            print("Random Geolocation from List:", locations[0].location)
            print("Location Found!")
            print(make_eiffel())
        elif search_geolocation == locations[1].location:
            print("Random Geolocation from List:", locations[1].location)
            print("Location Found!")
            print(make_louvre())
        elif search_geolocation == locations[2].location:
            print("Random Geolocation from List:", locations[2].location)
            print("Location Found!")
            print(make_needle())
        elif search_geolocation == locations[3].location:
            print("Random Geolocation from List:", locations[3].location)
            print("Location Found!")
            print(make_liberty())
        elif search_geolocation == locations[4].location:
            print("Random Geolocation from List:", locations[4].location)
            print("Location Found!")
            print(make_pisa())
        else:
            print("Out of Geolocation!")


# client program that computes things about the geolocations
def main():
    print()
    print("------------------M Y   P L A C E S------------------")

    eiffel_tower = make_eiffel()
    louvre_museum = make_louvre()
    space_needle = make_needle()
    statue_of_liberty = make_liberty()
    leaning_tower_of_pisa = make_pisa()
    print(eiffel_tower)
    print("-----------------------------------------------------")
    print(louvre_museum)
    print("-----------------------------------------------------")
    print(space_needle)
    print("-----------------------------------------------------")
    print(statue_of_liberty)
    print("-----------------------------------------------------")
    print(leaning_tower_of_pisa)
    print("-----------------------------------------------------\n")
    print("---------------D I S T A N C E  F R O M--------------")
    print("Louvre Museum from Eiffel Tower:", round(eiffel_tower.distance_from(louvre_museum),2))
    print("Louvre Museum from Statue of Liberty:", round(statue_of_liberty.distance_from(louvre_museum), 2))
    print("Statue of Liberty from Leaning Tower of Pisa:", round(leaning_tower_of_pisa.distance_from(statue_of_liberty), 2))
    print("-----------------------------------------------------\n")
    print("------F I N D   P L A C E   W I T H   G E O L O C A T I O N------")
    search(GeoLocation(48.859556, 2.294441))
    print("-----------------------------------------------------")


if __name__ == '__main__':
    main()
