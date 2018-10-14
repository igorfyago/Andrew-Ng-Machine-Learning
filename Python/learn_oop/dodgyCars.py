import random

class CarBase(object):
    pass

class MetaCar(type):
    car_brands = {}
    def __init__(cls, cls_name, cls_bases, cls_dict):
        super(MetaCar, cls).__init__(cls_name, cls_bases, cls_dict)
        if(not CarBase in cls_bases):
            MetaCar.car_brands[cls_name] = cls

    def __call__(self, *args, **kwargs):
        make = kwargs.get("make", "")
        if(MetaCar.car_brands.has_key(make) and not (self is MetaCar.car_brands[make])):
            obj = MetaCar.car_brands[make].__call__(*args, **kwargs)
            if(make == "Toyota"):
                if(random.randint(0, 100) < 2):
                    obj.defect = "sticky accelerator pedal"
            elif(make == "GM"):
                if(random.randint(0, 100) < 20):
                    obj.defect = "shithouse"
            elif(make == "Great Wall"):
                if(random.randint(0, 100) < 101):
                    obj.defect = "cancer"
        else:
            obj = None
            if(not MetaCar.car_brands.has_key(self.__name__)):
                new_class = MetaCar(make, (GenericCar,), {})
                globals()[make] = new_class
                obj = new_class(*args, **kwargs)
            else:
                obj = super(MetaCar, self).__call__(*args, **kwargs)
        return obj

class Car(CarBase):
    __metaclass__ = MetaCar

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        return "<%s>" % self.description

    @property
    def description(self):
        return "%s %s %s %s" % (self.color, self.year, self.make, self.model)

class GenericCar(Car):
    def __init__(self, **kwargs):
        kwargs["make"] = self.__class__.__name__
        super(GenericCar, self).__init__(**kwargs)

class Toyota(GenericCar):
    pass

colours = \
[
    "blue",
    "green",
    "red",
    "yellow",
    "orange",
    "purple",
    "silver",
    "black",
    "white"
]

def rand_colour():
    return colours[random.randint(0, len(colours) - 1)]

some_cars = \
[
    Car(make="Toyota", model="Prius", year=2005, color=rand_colour()),
    Car(make="Toyota", model="Camry", year=2007, color=rand_colour()),
    Car(make="Toyota", model="Camry Hybrid", year=2013, color=rand_colour()),
    Car(make="Toyota", model="Land Cruiser", year=2009, color=rand_colour()),
    Car(make="Toyota", model="FJ Cruiser", year=2012, color=rand_colour()),
    Car(make="Toyota", model="Corolla", year=2010, color=rand_colour()),
    Car(make="Toyota", model="Hiace", year=2006, color=rand_colour()),
    Car(make="Toyota", model="Townace", year=2003, color=rand_colour()),
    Car(make="Toyota", model="Aurion", year=2008, color=rand_colour()),
    Car(make="Toyota", model="Supra", year=2004, color=rand_colour()),
    Car(make="Toyota", model="86", year=2013, color=rand_colour()),
    Car(make="GM", model="Camaro", year=2008, color=rand_colour())
]

dodgy_vehicles = filter(lambda x: hasattr(x, "defect"), some_cars)
print(list(dodgy_vehicles))