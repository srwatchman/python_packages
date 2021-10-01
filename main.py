from my_package import fooFunc
from my_package import Car, ElectricCar
from my_package import Restaurant, IceCreamStand

fooFunc()

ford = Car("Hummer", "85")
ford.run_car()

prius = ElectricCar("EHummer", "110", "monster-hybrid")
prius.run_car()
prius.display_electric_type()

paris = Restaurant("Le Petit Paris", "French")
paris.describe_restaurant()
paris.open_restaurant()

friendlies = IceCreamStand("Friendlies", "Ice Cream", "Rocky Road", "Orange", "Sherbert")
friendlies.describe_restaurant()
friendlies.display_flavors()