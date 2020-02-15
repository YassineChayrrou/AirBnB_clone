#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    intro='''
             __   __  _______  _______  _______  ___   _______ 
            |  | |  ||   _   ||       ||       ||   | |       |
            |  |_|  ||  |_|  ||  _____||____   ||   | |____   |
            |       ||       || |_____  ____|  ||   |  ____|  |
            |_     _||       ||_____  || ______||   | | ______|
              |   |  |   _   | _____| || |_____ |   | | |_____ 
              |___|  |__| |__||_______||_______||___| |_______|
    ''' 
    prompt='(hbnb) '

    def help(self):
        print(''.join([
            'Documented commands (type help <topic>):',
            '========================================',
                ]))
 
    def emptyline():


    def do_quit(self, *args):
        return True

    def help_quit(self, *args):
        print("Quit command to exit the program\n")


    def do_EOF(self, *args):
        return True

    def help_EOF(self, *args):
        print("End Of File")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

