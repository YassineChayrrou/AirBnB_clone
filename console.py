#!/usr/bin/python3
import cmd
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
class_list = ('BaseModel')
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
                model.save()
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
                if len(parsed) >= 2:
                    if parsed[1]:
                        model.reload()
                        return print("{}".format(model))
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
        d = storage.all()
        if len(parsed) == 0:
            l = []
            for k, v in d.items():
                l.append(str(v))
            return(print(l))
        if parsed[0] in class_list:
            l = []
            for k, v in d.items():
                if v.__class__.__name__ == parsed[0]:
                    l.append(str(v))
            return(print(l))
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
                                   new_parsed = arg.split('"')
                                   return print(new_parsed[1])
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
