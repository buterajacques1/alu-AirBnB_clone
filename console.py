import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class that implements the command interpreter for the HBNB project.
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit on End Of File (EOF)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line + ENTER"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
