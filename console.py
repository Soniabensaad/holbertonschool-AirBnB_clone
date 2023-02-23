#!/usr/bin/python3
"""HBNBCommand Class.
Custom command line for AirBnB project.
"""
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """Defines methods and attributes of the console"""
    prompt = "(hbnb)"
    models = {"BaseModel": BaseModel(),
              'FileStorage': FileStorage(), "User": User(),
              'Amenity': Amenity(), 'City': City(), 'Place': Place(),
              'Review': Review(), 'State': State()}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program when user calls EOF"""
        return True

    def emptyline(self):
        """Overrides the dafult repeating of previous command"""
        pass

    def do_create(self, inp):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        args = inp.split()
        if not self.class_verification(args):
            return
        instance = eval(str(args[0]) + "()")
        if not isinstance(instance, BaseModel):
            return
        instance.save()
        print(instance.id)

    def do_show(self, inp):
        """Prints the string representation of an instance
          based on the class name and id"""
        args = inp.split()
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        string_r = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        print(objects[string_r])

    def do_destroy(self, inp):
        """Deletes an instance based on the class name and id"""
        args = inp.split(" ")
        if not self.class_verification:
            return

        if args[0] not in self.models:
            print("** class name missing **")
            return
        if not self.id_verification:
            return
        args = inp.split(" ")
        x = models.storage.all()
        for i in x.keys():
            j = i.split(".")
            if j[1] == args[1] and j[0] == args[0]:
                x.pop(i)
                models.storage.save()
                return
        print("** no instance found **")

    @classmethod
    def class_verification(cls, args):
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in cls.models:
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def id_verification(args):
        if len(args) < 2:
            print("** instance id missing **")
            return False
        objects = models.storage.all()
        string = str(args[0]) + '.' + str(args[1])
        if string not in objects.keys():
            print("** no instance found **")
            return False
        return True

    def do_all(self, inp):
        """Prints all string representation of
        all instances based or not on the class name"""
        args = inp.split()
        result = []
        objects = models.storage.all()
        if len(args) == 0:
            for value in objects.values():
                result.append(str(value))
        elif args[0] in self.models:
            for key, value in objects.items():
                if args[0] in key:
                    result.append(str(value))
        else:
            print("** class name missing **")
        print(result)

    def do_update(self, line):
        """ Updates an instance based on the class name and
          id by adding or updating attribute"""
        act = ""
        for argv in line.split(','):
            act = act + argv
        args = shlex.split(act)
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        if not self.attribute_verification(args):
            return
        all_objects = models.storage.all()
        for key, value in all_objects.items():
            object_name = value.__class__.__name__
            object_id = value.id
            if object_name == args[0] and object_id == args[1].strip('"'):
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(value, args[2], args[3])
                    models.storage.save()
                return

    @staticmethod
    def attribute_verification(args):
        """to verify attributes"""
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
