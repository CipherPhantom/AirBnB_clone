#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Represents the console"""
    
    def __init__(self):
        """Initializes the class"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def emptyline(self):
        """Define what happens when line is empty"""
        pass

    def do_quit(self, line):
        """Exits the console"""
        return True

    def do_EOF(self, line):
        """Exits the console"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
