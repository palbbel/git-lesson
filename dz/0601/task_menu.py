from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass




class Menu(metaclass=ABCMeta):

    def __init__(self):
        self.commands = {}
        self.ind = 0


    #@classmethod
    def add_command(self, name, klass):
        if not name:
            raise CommandException('Command must have a name!')
        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))
        self.commands[name] = klass


    #@classmethod
    def execute(self, name, *args, **kwargs):
        command = self.commands.get(name)
        if command:
            command.execute(args, kwargs)
        else:
            raise CommandException('Command with name "{}" not found'.format(name))


    def __next__(self):
        if self.ind < len(self.commands):
            command = (list(self.commands.items()))[self.ind]
            self.ind += 1
            return command
        else:
            raise StopIteration


    def __iter__(self):
        return self




class ShowCommand(Command):
    def __init__(self, task_id):
        pass


    def execute(self, *args, **kwargs):
        pass

class ListCommand(Command):
    def __init__(self):
        pass

    def execute(self, *args, **kwargs):
        pass


class CommandException(Exception):
    pass


if __name__ == '__main__':
    menu = Menu()
    menu.add_command('show', ShowCommand)
    menu.add_command('list', ListCommand)
    menu.execute('show', 1)
    menu.execute('list')
    menu.execute('unknown')