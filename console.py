#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
from models import storage, MODELS
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Represents the console"""
    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif line not in MODELS:
            print("** class doesn't exist **")
        else:
            obj = MODELS[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name
        """
        args = line.split()
        if not len(args):
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not len(args):
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """
        objs_str = []
        if not line:
            for value in storage.all().values():
                objs_str.append(str(value))
            print(objs_str)
        elif line in MODELS:
            for value in storage.all().values():
                if value.__class__.__name__ == line:
                    objs_str.append(str(value))
            print(objs_str)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not len(args):
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = storage.all()[f"{args[0]}.{args[1]}"]
            name = args[2]
            value = args[3]

            if value.isdigit():
                if "." in value:
                    value = float(value)
                else:
                    value = int(value)
            elif (value[0] == '"' and value[-1] == '"') or \
                    (value[0] == "'" and value[-1] == "'"):
                value = value[1:-1]
            setattr(obj, name, value)

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
