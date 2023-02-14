#!/usr/bin/python3
""" console """

# Import necessary modules
import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes

# Create a dictionary mapping class names to their corresponding class
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

# Define a class that inherits from the cmd module, which provides the
# functionality to create a console application
class HBNBCommand(cmd.Cmd):

    """ HBNH console """
    prompt = '(hbnb) '

    # Define a method to handle the 'EOF' command, which exits the console
    def do_EOF(self, arg):
        """Exits console"""
        return True

    # Define a method to handle empty line inputs
    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    # Define a method to handle the 'quit' command, which exits the console
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    # Define a method to parse a list of strings into a dictionary of key-value pairs
    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                # Check if the value is a string enclosed in double quotes
                if value[0] == value[-1] == '"':
                    # Use shlex.split to split the value into a list of words
                    # and replace any underscores with spaces
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                # Add the key-value pair to the dictionary
                new_dict[key] = value
        return new_dict

    # Define a method to handle the 'create' command, which creates a new instance of a class
    def do_create(self, arg):
        """Creates a new instance of a class"""
        # Split the input into a list of strings
        args = arg.split()
        # Check if the first argument is missing
        if len(args) == 0:
            print("** class name missing **")
            return False
        # Check if the class name is valid
        if args[0] in classes:
            # Parse the remaining arguments as a dictionary of key-value pairs
            new_dict = self._key_value_parser(args[1:])
            # Create a new instance of the class with the parsed dictionary as the arguments
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        # Print the id of the new instance and save it to the database
        print(instance.id)
        instance.save()

    # Define a method to handle the 'show' command, which prints an instance based on class and id
    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
