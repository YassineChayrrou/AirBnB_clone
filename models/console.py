#!/usr/bin/python3
import cmd
import json
from base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class that inherits from cmd
       acts as command line console"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        model = BaseModel()
        return print("{}".format(model))

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
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
