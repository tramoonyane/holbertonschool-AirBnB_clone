#!/usr/bin/python3
"""
FileStorage class for serialisation and deserialisation of instances.
"""
import json
import os


class FileStorage:
    """
    Serialises instances to a JSON file & deserialises back to instances
    """

    __file_path = "file.json"  # path to json file
    __objects = {}  # dictionary to store objects
    CLASS_NAME_MAP = {
        "BaseModel": "models.base_model.BaseModel",
        "User": "models.user.User",
        "State": "models.state.State",
        "City": "models.city.City",
        "Place": "models.place.Place",
        "Review": "models.review.Review",
        "Amenity": "models.amenity.Amenity",
    }

    def all(self):
        """Return the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Sets an object in the objects dictionary with a formatted key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialise the __objects to JSON file."""
        dict_to_save = {}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            for key, obj in self.__objects.items():
                dict_to_save[key] = obj.to_dict()
            json.dump(dict_to_save, f, indent=4)

    def reload(self):
        """Deserialise the JSON file to __objects, if the file exists."""
        if os.path.exists(self.__file_path):
            # load the serialised objects from the file
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                seri_objs = json.load(f)
                for key, value in seri_objs.items():
                    class_name = value['__class__']
                    # get the module and class path from mapping
                    cls_path = self.CLASS_NAME_MAP.get(class_name)
                    if cls_path:
                        # extract module and class names from the path
                        module_name, class_name = cls_path.rsplit('.', 1)
                        # import the module and extract the class
                        module = __import__(module_name, fromlist=[class_name])
                        cls = getattr(module, class_name)
                        # create new instance of the class with serialised data
                        instance = cls(**value)
                        self.__objects[key] = instance
