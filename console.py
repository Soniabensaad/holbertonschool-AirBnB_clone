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


class HBNBCommand(cmd.Cmd):
    """Defines methods and attributes of the console"""
    prompt = "(hbnb)"
    models = ["BaseModel", "User",
              "Amenity", "City", "Place",
              "Review", "State"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program when user calls EOF"""
        return True

    def emptyline(self):
        """Overrides the dafult repeating of previous command"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
        if arg not in self.models:
            print("** class doesn't exist **")
        if arg == "User":
            instance = User()
        if arg == "City":
            instance = City()
        if arg == "Review":
            instance = Review()
        if arg == "Amenity":
            instance = Amenity()
        if arg == "Place":
            instance = Place()
        if arg == "State":
            instance = State()
        if arg == "BaseModel":
            instance = BaseModel()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
          based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        args = arg.split(" ")
        if args[0] not in self.models:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        objects = models.storage.all()
        key = args[0] + '.' + args[1]
        if key in objects:
            print(objects[key])
            return
        print("** no instance found **")
        return
        
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split(" ")
        if args[0] not in self.models:
            print("** class doesn't exist **") 
        if len(args) < 2:
            print("** instance id missing **")
        objects = models.storage.all()
        key = args[0] + '.' + args[1]
        if key in objects:
            del objects[key]
            models.storage.save()
            return
        print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of
        all instances based or not on the class name"""
        args = arg.split(" ")
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

    def do_update(self, arg):
        """ Updates an instance based on the class name and
          id by adding or updating attribute"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in lst:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        x = models.storage.all()
        to_upd = 0
        for i in x.keys():
            k = i.split(".")
            if k[1] == args[1]:
                to_upd = 1
                f = i
        if to_upd == 0:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        args = args[0] + " " + args[1]+" "+args[2]+" " + args[3]
        args = args.split(" ")
        k = x[f].__dict__
        p = args[3].split("\"")
        k[args[2]] = p[1]
        x[f].save
if __name__ == '__main__':
    HBNBCommand().cmdloop()
