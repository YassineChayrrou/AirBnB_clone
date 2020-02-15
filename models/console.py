#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class that inherits from cmd
       acts as command line console"""
    prompt = '(hbnb) '

    def emptyline(self):
        """emptyline handler"""
        if self.lastcmd is None:
            return self.onecmd('\n')

    def help(self):
        print('\n\n'.join([
            'Documented commands (type help <topic>):',
            '========================================',
                ]))

    def do_quit(self, *args):
        "Quit command to exit the program\n"
        return True

    def do_EOF(self, *args):
        "EOF: type Ctrl + d to exit"
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
