from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    "La interfaz command, que todos los comandos van a implementar"
    @staticmethod
    @abstractmethod
    def execute():
        """
        Se requiere un metodo execute para todos los objetos command
        The required execute method that all command objects
        will use
        """

class Invoker:
    "Clase invoker"
    def __init__(self):
        self._commands = {}
    def register(self, command_name, command):
        "Registra los comandos en invoker"
        self._commands[command_name] = command
    def execute(self, command_name):
        "Ejecuta los comandos"
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")

class Receiver:
    "Clase Receiver"
    @staticmethod
    def run_command_1():
        "A set of instructions to run"
        print("Executing Command 1")
    @staticmethod
    def run_command_2():
        "A set of instructions to run"
        print("Executing Command 2")

class Command1(ICommand):  # pylint: disable=too-few-public-methods
    """ un objeto Command, que implementa la interfaz ICommand y ejecuta el comando designado en receiver
    """
    def __init__(self, receiver):
        self._receiver = receiver
    def execute(self):
        self._receiver.run_command_1()

class Command2(ICommand):  # pylint: disable=too-few-public-methods
    """
    un objeto Command, que implementa la interfaz ICommand y ejecuta el comando designado en receiver
    """
    def __init__(self, receiver):
        self._receiver = receiver
    def execute(self):
        self._receiver.run_command_2()

# The CLient
# Create a receiver
RECEIVER = Receiver()
# Create Commands
COMMAND1 = Command1(RECEIVER)
COMMAND2 = Command2(RECEIVER)
# Register the commands with the invoker
INVOKER = Invoker()
INVOKER.register("1", COMMAND1)
INVOKER.register("2", COMMAND2)
# Execute the commands that are registered on the Invoker
INVOKER.execute("1")
INVOKER.execute("2")
INVOKER.execute("1")
INVOKER.execute("2")