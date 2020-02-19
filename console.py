#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
class_list = ('User', 'City', 'BaseModel')
uuid_list = ('test', 'test2', '1234')

class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class that inherits from cmd
       acts as command line console"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """create a new instance of BaseModel"""
        parsed = parse(arg)
        if parsed:
            if parsed[0] in class_list:
                model = BaseModel()
                return print("{}".format(model.id))
            return print("** class doesn't exist **")
        print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of instance id/class
Requires class_name and id"""
        parsed = parse(arg)
        if len(parsed) >= 1:
            if parsed[0] in class_list:
                model = BaseModel()
                if len(parsed) >= 2:
                    if parsed[1] in uuid_list:
                        # condition to check if id does exist is missing
                        # checks if id is true code goes here
                        # tobe done with Franky Spacy
                        return print("checked:\n{}".format(model))
                    return print("** no instance found **")
                return print("**instance id missing**")
            return print("** class doesn't exist **")
        return print("** class name missing **")

    def emptyline(self):
        """emptyline handler"""
        if self.lastcmd is None:
            return self.onecmd('\n')

    def help(self):
        print("""
           Documented commands (type help <topic>):
           ========================================
             """)

    def do_quit(self, arg):
        "Quit command to exit the program\n"
        return True

    def do_EOF(self, arg):
        "EOF: type Ctrl + d to exit"
        return True


def parse(arg):
    return tuple(map(str, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
