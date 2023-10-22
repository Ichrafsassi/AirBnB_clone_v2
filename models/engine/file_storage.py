#!/usr/bin/python3
from models.base_model import BaseModel

class Base():
    pass

from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()

# Add a close method to the FileStorage class
def close(self):
    """ Calls reload() method for deserializing the JSON file to objects """
    self.reload()

# Implement the cities property for the State class
@property
def cities(self):
    """ Returns the list of City objects linked to the current State """
    all_cities = models.storage.all(City)
    state_cities = [city for city in all_cities.values() if city.state_id == self.id]
    return state_cities

# Attach the close method to the FileStorage class
file_storage.FileStorage.close = close

# Attach the cities property to the State class
State.cities = cities
