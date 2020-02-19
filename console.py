#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
class_list = ('User', 'City', 'BaseModel')
uuid_list = ('test', 'test2', '1234')
attribute_list = ('name','email','something_else')


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
                #save method by aziz
                return print("{}".format(model.id))
            return print("** class doesn't exist **")
        print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance
based on class name and id
        """
        parsed = parse(arg)
        if len(parsed) >= 1:
            if parsed[0] in class_list:
                model = BaseModel()
                model.first_name = "Yassine"
                model = BaseModel()
                if len(parsed) >= 2:
                    if parsed[1] in uuid_list:
                        print("still under active development")
                        return print("checked:\n{}".format(model))
                    return print("** no instance found **")
                return print("** instance id missing **")
            return print("** class doesn't exist **")
        return print("** class name missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        parsed = parse(arg)
        if len(parsed) >= 1:
            if parsed[0] in class_list:
                if len(parsed) >= 2:
                    if parsed[1] in uuid_list:
                        return print("under active development")
                    return print("** no instance found **")
                return print("** instance id missing **")
            return print("** class doesn't exist **")
        return print("** class name missing **")

    def do_all(self, arg):
        parsed = parse(arg)
        if len(parsed) == 0:
            #prints storage.json in case of argument all(only)
            return print("prints all classes string representation")
        if parsed[0] in class_list:
            model = BaseModel()
            return print('mimics all string rep of class <BaseModel>\n["{}"]'.format(model))
        return print("** class doesn't exit **")

    def do_update(self, arg):
       parsed = parse(arg)
       if len(parsed) >= 1:
           if parsed[0] in class_list:
               if len(parsed) >= 2:
                   if parsed[1] in uuid_list:
                       if len(parsed) >= 3:
                           if len(parsed) >= 4:
                               if parsed[3][0] == '"':
                                   quote = arg.split('"')
                                   return print(quote[1])
#                                   return print("<{}> is set and to be added here ------///".format(parsed[3]))
                           return print("** value missing **")
                       return print("** attribute name missing **")
                   return print("** no instance found **")
               return print("** instance id missing **")
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
