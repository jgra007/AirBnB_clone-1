#!/usr/bin/python3
"""console airbnb"""
import cmd
import sys
import json
import models
import shlex
from models import Amenity
from models.base_model import BaseModel
from models import City
from models import Place
from models import State
from models import storage
from models import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Class HBNB command line console prompt """

    prompt = "(hbnb) "
    group = {'BaseModel', 'User', 'State', 'City',
             'Amenity', 'Place', 'Review'}
    file_path: storage.__FileStorage__file_path
    err_list = ["** class name missing **", "** class doesn't exist **",
                "** instance id missing **", "** no instance found **",
                "** attribute name missing **", "** value missing **"]

    def err_msg(self, n):
        """Function to return error messages"""
        msg_dict = {1: "** class name missing **",
                    2: "** class doesn't exist **",
                    3: "** instance id missing **",
                    4: "** no instance found **",
                    5: "** attribute name missing **",
                    6: "** value missing **"
                    }
        for key, item in msg_dict.items():
            if key == n:
                print(item)

    def do_create(self, arg):
        """Used to create a new instance of BaseModel and saves
        the instance to a JSON file"""
        if arg == "":
            print(self.err_list[0])
        elif arg not in self.group:
            print(self.err_list[1])
        else:
            arg = eval(arg)()
            arg.save()
            print(arg.id)

    def do_show(self, line):
        """Function to print string representation of instance"""
        arg = line.split()
        if line == "":
            print(self.err_list[0])
        elif arg[0] not in self.group:
            print(self.err_list[1])
        elif len(arg) < 2:
            print(self.err_list[2])
        else:
            data_dump = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            try:
                obj = data_dump[key]
                print(obj)
            except KeyError:
                print(self.err_list[3])

    def do_destroy(self, line):
        """Function to print string representation of instance"""
        arg = line.split()
        if line == "":
            print(self.err_list[0])
        elif arg[0] not in self.group:
            print(self.err_list[1])
        elif len(arg) < 2:
            print(self.err_list[2])
        else:
            data_dump = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in data_dump:
                del data_dump[key]
                storage._FileStorage__objects = data_dump
                storage.save()
                return
            print(self.err_list[3])

    def do_all(self, line=""):
        """Function that displays all class instances of given argument or all
        if no argument given"""
        data_dump = models.storage.all()
        if line is "":
            for instance_key, instance_obj in data_dump.items():
                print(instance_obj)
        else:
            arg = line.split()
            if arg[0] not in self.group:
                print(self.err_list[1])
            else:
                for instance_key, instance_obj in data_dump.items():
                    obj = instance_obj.to_dict()
                    if obj['__class__'] == arg[0]:
                        print(instance_obj)

    def default(self, line):
        """Called on an input line when command prefix is swapped to
        method of instance"""
        func = {'create': self.do_create, 'show': self.do_show,
                'destroy': self.do_destroy, 'count': self.do_count,
                'all': self.do_all, 'update': self.do_update}
        symbols = {'"', ',', '{', '}', ':', "'"}
        sep = line.split('.')
        command = ""
        x = 0

        # noinspection PyBroadException
        try:
            while sep[1][x] != '(':
                command += sep[1][x]
                x += 1
            y = len(command) + 1
            arg = ""
            while sep[1][y] != ')':
                if sep[1][y] not in symbols:
                    arg += sep[1][y]
                y += 1
            if arg == "":
                new_line = "{}".format(sep[0])
                func[command](new_line)
            else:
                p = arg.split(" ")
                if len(p) == 5:
                    arg1 = "{} {} {}".format(p[0], p[1], p[2])
                    arg2 = "{} {} {}".format(p[0], p[3], p[4])
                    new_line1 = "{} {}".format(sep[0], arg1)
                    new_line2 = "{} {}".format(sep[0], arg2)
                    func[command](new_line1)
                    func[command](new_line2)
                else:
                    new_line3 = "{} {}".format(sep[0], arg)
                    func[command](new_line3)
        except Exception:
            print("Invalid command, please try again")

    def do_count(self, arg):
        """Function to return a count of all instances of a given class"""
        data_dump = models.storage.all()
        count = 0
        for key, item in data_dump.items():
            obj = item.to_dict()
            if obj['__class__'] == arg:
                count += 1
        print(count)

    def splitter(self, line):
        """Function to split line into arguments using shlex"""
        lex = shlex.shlex(line)
        lex.quotes = '"'
        lex.whitespace_split = True
        lex.commenters = ''
        return list(lex)

    def do_update(self, line=""):
        """Updates an instance based on the class name and id by adding or
        updating attribute and save the change into the JSON file"""
        data_dump = models.storage.all()
        arg = self.splitter(line)
        # arg = line.split()

        if not line:
            print(self.err_msg[0])
        elif arg[0] not in self.group:
            print(self.err_msg[1])
        elif len(arg) < 2:
            print(self.err_msg[2])
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key in data_dump:
                if len(arg) < 3:
                    print(self.err_msg[4])
                elif len(arg) < 4:
                    print(self.err_msg[5])
                else:
                    obj = data_dump[key]
                    setattr(obj, arg[2], arg[3])
            else:
                print(self.err_msg[3])

    def do_quit(self, line):
        """Quit command to exit the console\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the console\n"""
        return True

    def emptyline(self):
        """ Empty Line  """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
