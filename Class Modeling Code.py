
class animal:
    """Animal Class"""
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def get_name(self):
        return self._name
    @property
    def get_age(self):
        return self._age
    

    def move(self):
        print("Moving")
    
    def eat(self):
        print("Eating")
    
    def sleep(self):
        print("Sleeping")


class book:
    """Book Class"""
    def __init__(self,title,author,genre,publisher):
        self._title = title
        self._author = author
        self._genre = genre
        self._publisher = publisher
   
    @property
    def get_title(self):
        return self._title
    @property
    def get_author(self):
        return self._author
    @property
    def get_genre(self):
        return self._genre
    @property
    def get_publisher(self):
        return self._publisher
    

class vehicle:
    """Vehicle Class"""
    def __init__(self,model,color,manufacturer,year,four_wheels):
        self._model = model
        self._color = color
        self._manufacturer = manufacturer
        self._year = year
        self._four_wheels = four_wheels
    
    @property
    def get_model(self):
        return self._model
    @property
    def get_color(self):
        return self._color
    @property
    def get_manufacturer(self):
        return self._manufacturer
    @property
    def get_year(self):
        return self._year
    @property
    def get_four_wheels(self):
        return self._four_wheels

    def move(self):
        print("Moving")
    def reverse(self):
        print("Reversing")
        
