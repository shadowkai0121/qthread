
class Command(object):
    pass

class ScriptCommand(Command):
    template = ''

class BasicCommand(Command):
    pass


class HomeCommand(ScriptCommand):
