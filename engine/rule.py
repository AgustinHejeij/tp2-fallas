def cost_to_int(cost):
    if cost == "bajo":
        return 1
    elif cost == "intermedio":
        return 2
    else:
        return 3

class Rule:
    def __init__(self, name, type, biome, weather, cost, country, languages, trip_length):
        self._name = name
        self._type = type
        self._biome = biome
        self._weather = weather
        self._cost = cost_to_int(cost)
        self._country = country
        self._languages = languages
        self._trip_length = trip_length

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def biome(self):
        return self._biome

    @biome.setter
    def biome(self, value):
        self._biome = value

    @property
    def weather(self):
        return self._weather

    @weather.setter
    def weather(self, value):
        self._weather = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def languages(self):
        return self._languages

    @languages.setter
    def languages(self, value):
        self._languages = value

    @property
    def trip_length(self):
        return self._trip_length

    @trip_length.setter
    def trip_length(self, value):
        self._trip_length = value

    def is_equal(self, destiny):
        return self._biome == destiny.biome and self._weather == destiny.weather and self._cost == destiny.cost and self._country == destiny.country and self._languages == destiny.languages and self._trip_length == destiny.trip_length

    def get_similarity(self, destiny):
        count = 0
        if destiny.type in self._type:
            count += 1
        if destiny.biome in self._biome:
            count += 1
        if destiny.weather in self._weather:
            count += 1
        if self._cost <= destiny.cost:
            count += 1
        if self._country == destiny.country:
            count += 1
        if any(x in self._languages for x in destiny.languages):
            count += 1
        if self._trip_length <= destiny.trip_length:
            count += 1

        return count
