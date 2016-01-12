class PColors:
    INFO = '\033[37m'
    STATUS = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.INFO = ''
        self.STATUS = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


def invalid(prefix, actions):
    print("{.WARNING}{} Sorry, I didn't understand that. Valid \
        options are: {}{.ENDC}".format(
        PColors, prefix, ", ".join(actions)), PColors)


def prompt(prefix, actions):
    print("{.OKBLUE}{} Your options are: {}{.ENDC}".format(
        PColors, prefix, ", ".join(actions), PColors))


def info(prefix, words):
    print("{.INFO}{} {}{.ENDC}".format(PColors, prefix, words, PColors))


def ok(prefix, words):
    print("{.OKGREEN}{} {}{.ENDC}".format(PColors, prefix, words, PColors))


def fail(prefix, words):
    print("{.FAIL}{} {}{.ENDC}".format(PColors, prefix, words, PColors))


def warn(prefix, words):
    print("{.WARNING}{} {}{.ENDC}".format(PColors, prefix, words, PColors))


def yay(prefix, words):
    print("{.OKBLUE}{} {}{.ENDC}".format(PColors, prefix, words, PColors))
