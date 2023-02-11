import cmd


# Derive a class HBNBCommand from cmd.Cmd
class HBNBCommand(cmd.Cmd):
    # Define the prompt string
    prompt = '(hbnb) '

    # Define the quit method to exit the program
    def do_quit(self, line):
        """Quit the program with a helpful message."""
        return True

    # Define the EOF method to exit the program on End Of File
    def do_EOF(self, line):
        """Exit the program when the end of file is reached."""
        return True


# If this file is run as a standalone program
if __name__ == '__main__':
    # Start the command interpreter
    HBNBCommand().cmdloop()
