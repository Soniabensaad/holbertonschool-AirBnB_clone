#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import FileStorage
class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    
    def do_quit(self, arg):
        return True
    
    def do_EOF(self, arg):
        return True
    
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()