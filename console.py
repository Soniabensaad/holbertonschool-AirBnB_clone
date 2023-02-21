#!/usr/bin/python3
import cmd

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
        #Overrides the dafult repeating of previous command
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()