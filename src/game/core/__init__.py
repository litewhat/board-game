from game.console import Console
from game.exceptions import GameStoppedException
from game.core.models import Model


class Unit(Model):
    attributes = ('name')


class Player(Model):
    attributes = ('name')

    def __init__(self, name):
        super().__init__()
        self.name = name


class BaseGame(Model):

    def start(self, **kwargs):
        raise NotImplementedError()

    def stop(self, **kwargs):
        raise NotImplementedError()


def resolve_actions(handlers, *commands):
    for cmd in set(*commands):
        yield handlers[cmd]


class Game(BaseGame):
    attributes = ('name', 'console', 'player')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.exceptions = []
        self.actions = []
        self.running = False
        self.stopped = False

    def start(self, **kwargs):
        if self.stopped:
            raise GameStoppedException()
        running_mode = kwargs.get('running_mode', None)
        self.run(mode=running_mode)

    def _run_live_mode(self):
        self.running = True
        while True:
            try:
                command = self.get_command()
                self.actions.extend(resolve_actions(command))

                if command.strip().lower() == 'exit':
                    self.running = False
                    self.stop()
                    break

                self.actions.append(command)
            except (KeyboardInterrupt, EOFError) as exc:
                self.running = False
                self.stop(exc=exc)
                break

    def _run_test_mode(self):
        self.running = True

    def run(self, *, mode):
        if mode == 'test':
            self._run_test_mode()
        else:
            self._run_live_mode()

    def stop(self, *, exc=None, **kwargs):
        self.stopped = True
        self.exceptions.append(exc)

    def get_command(self):
        return self.console.input(prompt=f'({self.player.name}) ~> ')
