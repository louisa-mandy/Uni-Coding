class fooditems():  # Creating food items class
    # Initializer
    def __init__(self, food, pounds):  # Use __init__ instead of init
        # Setting initial values
        # This is a hidden parameter
        self._food = food
        self._pounds = pounds
        self._price_standard = 0  # Set standard price to 0 because it starts from nothing
        self._calcprice = 0
        self.PriceList()

    # A method to store item in the list and price per pound from the table
    def PriceList(self):
        if self._food == 'Dry Cured Iberian Ham':
            self._price_standard = 177.80
        elif self._food == 'Wagyu Steaks':
            self._price_standard = 450.00
        elif self._food == 'Matsutake Mushrooms':
            self._price_standard = 272.00
        elif self._food == 'Kopi Luwak Coffee':
            self._price_standard = 306.50
        elif self._food == 'Moose Cheese':
            self._price_standard = 487.20
        elif self._food == 'White Truffles':
            self._price_standard = 3600.00
        elif self._food == 'Blue Fin Tuna':
            self._price_standard = 3603.00
        elif self._food == 'Le Bonnotte Potatoes':
            self._price_standard = 270.81
        else:
            self._price_standard = 0

    # Accessor
    def cost(self):
        return self._price_standard * self._pounds
