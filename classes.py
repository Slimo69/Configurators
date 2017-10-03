class Project:
    def __init__(self, id, name, country, altitude, currency):
        self.id = id
        self.name = name
        self.country = country
        self.altitude = altitude
        self.currency = currency

    def __str__(self):
        return "ID: {} \nName: {} \nCountry: {} \nAltitude: {} \nCurrency: {}".format(self.id, self.name, self.country, self.altitude, self.currency)
