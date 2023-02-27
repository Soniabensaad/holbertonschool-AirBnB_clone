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
from models import theModels


class HBNBCommand(cmd.Cmd):
    """Defines methods and attributes of the console"""
    prompt = "(hbnb)"

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
        """creates a new instance"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = arg.split()

        try:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            eval(args[0])
        except:
            print("** class doesn't exist **")

        obj_dict = storage.all()
        key_id = args[0] + "." + args[1]

        try:
            value = obj_dict[key_id]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[1] == 0:
            print("** instance id missing **")

        try:
            eval(args[0])
        except:
            print("** class doesn't exist **")
        obj_dict = storage.all()
        key_id = args[0] + "." + args[1]

        try:
            del obj_dict[key_id]
        except:
            print("** no instance found **")
        storage.save()

    def do_all(self, arg):
        """ Prints string represention of all instances of a given class """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in theModels:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            new_list = []

            for key, val in all_objs.items():
                obj_name = val.__class__.__name__
                if obj_name == args[0]:
                    new_list += [val.__str__()]
            print(new_list)
        

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in theModels:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                ob_id = val.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(val, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")
        
    def do_count(self, cls_name):
        """retrieve the number of instances of a class:
          <class name>.count()."""
        count = 0
        all_objs = storage.all()
        for key, val in all_objs.items():
            args = key.split('.')
            if args[0] == cls_name:
                count =count + 1
        print(count)
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
