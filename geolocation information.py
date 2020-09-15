# This place stores information about a place on Earth

class Place:

    # create a constructor
    def __init__(self, name, address, tag, location):
        self._name = name
        self._address = address
        self._tag = tag
        self._location = location

    @property
    def address(self):
        return self._address

    def distance_from(self, other):
        return self._location.distance_from(other.location)

    @property
    def location(self):
        return self._location

    @property
    def name(self):
        return self._name

    @property
    def tag(self):
        return self._tag

    # determine if two place are equal to each other
    def __eq__(self, other):
        exp_1 = self._address == other.address
        exp_2 = self._name == other.name
        exp_3 = self._tag == other.tag
        exp_4 = self._location == other.location

        return exp_1 and exp_2 and exp_3 and exp_4

    # returns a string representation of a place object
    def __str__(self):
        string_1 = f"Name:        {self._name} \n"
        string_2 = f"Address:     {self._address} \n"
        string_3 = f"Search Tag:  {self._tag} \n"
        string_4 = f"Coordinates: {self._location} \n"

        return string_1 + string_2 + string_3 + string_4