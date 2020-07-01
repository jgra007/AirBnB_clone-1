#!/usr/bin/python3
""" Create Class FileStorage """
import json
import models
from models.base_model import BaseModel


class FileStorage:
    """Private class attributes for Class FileStorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary with objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Returns __objects with obj set as key"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file inside"""
        save_file = self.__file_path
        new_dict = {}
        for key, item in self.__objects.items():
            new_dict[key] = item.to_dict()
        with open(save_file, mode="w", encoding='utf-8') as new_file:
            json.dump(new_dict, new_file)

    def reload(self):
        """ Reload File Json """
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file_json:
                from models.base_model import BaseModel
                from models.user import User
                from models.place import Place
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.review import Review
                json_des = json.load(file_json)
            for key, value in json_des.items():
                value = eval(value["__class__"])(**value)
                FileStorage.__objects[key] = value
        except OSError:
            pass
