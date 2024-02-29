#!/usr/bin/python3
"""
Command interpreter for HBnB console program
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

VALID_MODELS = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    """Console command interpreter for HBnB"""

    prompt = "(hbnb) "
    doc_header = "Documented commands (type help <topic>):"

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        # ctrl-d
        print()  # \n before exit
        return True

    def do_create(self, arg):
        """Creates a new instance of the specified class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name in VALID_MODELS:
            new_instance = VALID_MODELS[class_name]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in VALID_MODELS:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in VALID_MODELS:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Displays all instances of a class"""
        args = arg.split()
        obj_list = []
        if not args or args[0] not in VALID_MODELS:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        else:
            for key, instance in storage.all().items():
                 if instance.__class__.__name__ == args[0]:
                    obj_list.append(str(instance))
        print(obj_list)

    def do_update(self, arg):
        """Updates attributes of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in VALID_MODELS:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
                print("** no instance found **")
            else:
                setattr(storage.all()[key], args[2], args[3].strip('"'))
                storage.save()

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass


if __name__ == '__main__':
    """Console main loop"""
    HBNBCommand().cmdloop()
