#!/usr/bin/python3
"""console airbnb"""
import cmd



class HBNBCommand(cmd.Cmd):
    """ Class HBNB command line console prompt """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the console\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the console\n"""
        return True

    def emptyline(self):
        """ Empty Line  """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_inst = eval(args[0] + '()')
            models.storage.save()
            print(new_inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                print(objects[key_find])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                objects.pop(key_find, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel
        """
        args = line.split()
        objects = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)

        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute (save
        the change into the JSON file).
        Ex: $ update BaseModel <valid id> attrib value
        """
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        elif len(args) == 2:
            print("** attribute name missing **")

        elif len(args) == 3:
            print("** value missing **")

        else:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def do_User(self, line):
        """Retrieve all instances of User class.
        Ex: $ User.all()
        """
        objects = models.storage.all()
        class_name = "User"
        method = line.split(".")[1].split("(")[0]

        if "(" and ")" in line:
            if method == "all":
                HBNBCommand.do_all(HBNBCommand, class_name)
            elif method == "count":
                counter = 0
                for key in objects:
                    if key.split(".")[0] == class_name:
                        counter += 1
                print(counter)
            elif method == "show":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        print(value)
            elif method == "destroy":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        objects.pop(key, None)
                        models.storage.save()

    def do_BaseModel(self, line):
        """Retrieve all instances of BaseModel class.
        Ex: $ BaseModel.all()
        """
        objects = models.storage.all()
        class_name = "BaseModel"
        method = line.split(".")[1].split("(")[0]

        if "(" and ")" in line:
            if method == "all":
                HBNBCommand.do_all(HBNBCommand, class_name)
            elif method == "count":
                counter = 0
                for key in objects:
                    if key.split(".")[0] == class_name:
                        counter += 1
                print(counter)
            elif method == "show":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        print(value)
            elif method == "destroy":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        objects.pop(key, None)
                        models.storage.save()

    def do_Amenity(self, line):
        """Retrieve all instances of Amenity class.
        Ex: $ Amenity.all()
        """
        objects = models.storage.all()
        class_name = "Amenity"
        method = line.split(".")[1].split("(")[0]

        if "(" and ")" in line:
            if method == "all":
                HBNBCommand.do_all(HBNBCommand, class_name)
            elif method == "count":
                counter = 0
                for key in objects:
                    if key.split(".")[0] == class_name:
                        counter += 1
                print(counter)
            elif method == "show":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        print(value)
            elif method == "destroy":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        objects.pop(key, None)
                        models.storage.save()

    def do_City(self, line):
        """Retrieve all instances of City class.
        Ex: $ City.all()
        """
        objects = models.storage.all()
        class_name = "City"
        method = line.split(".")[1].split("(")[0]

        if "(" and ")" in line:
            if method == "all":
                HBNBCommand.do_all(HBNBCommand, class_name)
            elif method == "count":
                counter = 0
                for key in objects:
                    if key.split(".")[0] == class_name:
                        counter += 1
                print(counter)
            elif method == "show":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        print(value)
            elif method == "destroy":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        objects.pop(key, None)
                        models.storage.save()

    def do_Place(self, line):
        """Retrieve all instances of Place class.
        Ex: $ Place.all()
        """
        objects = models.storage.all()
        class_name = "Place"
        method = line.split(".")[1].split("(")[0]

        if "(" and ")" in line:
            if method == "all":
                HBNBCommand.do_all(HBNBCommand, class_name)
            elif method == "count":
                counter = 0
                for key in objects:
                    if key.split(".")[0] == class_name:
                        counter += 1
                print(counter)
            elif method == "show":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        print(value)
            elif method == "destroy":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        objects.pop(key, None)
                        models.storage.save()

    def do_Review(self, line):
        """Retrieve all instances of Review class.
        Ex: $ Review.all()
        """
        objects = models.storage.all()
        class_name = "Review"
        method = line.split(".")[1].split("(")[0]

        if "(" and ")" in line:
            if method == "all":
                HBNBCommand.do_all(HBNBCommand, class_name)
            elif method == "count":
                counter = 0
                for key in objects:
                    if key.split(".")[0] == class_name:
                        counter += 1
                print(counter)
            elif method == "show":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        print(value)
            elif method == "destroy":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        objects.pop(key, None)
                        models.storage.save()

    def do_State(self, line):
        """Retrieve all instances of State class.
        Ex: $ State.all()
        """
        objects = models.storage.all()
        class_name = "State"
        method = line.split(".")[1].split("(")[0]

        if "(" and ")" in line:
            if method == "all":
                HBNBCommand.do_all(HBNBCommand, class_name)
            elif method == "count":
                counter = 0
                for key in objects:
                    if key.split(".")[0] == class_name:
                        counter += 1
                print(counter)
            elif method == "show":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        print(value)
            elif method == "destroy":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        objects.pop(key, None)
                        models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
