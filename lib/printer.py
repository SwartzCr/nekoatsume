class PColors:
    RED = '\033[31m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    GOODBYE = '\033[93m'
    HELP = '\033[36m'
    MAIN = '\033[37m'
    SHOP = '\033[95m'
    YARD = '\033[92m'
    ENDC = '\033[0m'

    def disable(self):
        self.RED = ''
        self.YELLOW = ''
        self.GREEN = ''
        self.BLUE = ''
        self.PURPLE = ''
        self.GOODBYE = ''
        self.HELP = ''
        self.MAIN = ''
        self.SHOP = ''
        self.YARD = ''
        self.ENDC = ''


def fail(prefix, words):
    print("{.RED}{}{.ENDC} {}".format(PColors, prefix, PColors, words))


def invalid(prefix, actions):
    sorry_msg = "{.YELLOW}{}{.ENDC} Sorry, I don't understand. Options are: {}"
    print(sorry_msg.format(PColors, prefix, PColors, ", ".join(actions)))


def prompt(prefix, actions):
    print("{0} Your options are: {1}".format(prefix, ", ".join(actions)))


def p(prefix, words):
    print("{} {}".format(prefix, words))


def shop(prefix, words):
    print("{.SHOP}{}{.ENDC} {}".format(PColors, prefix, PColors, words))


def success(prefix, words):
    print("{.GREEN}{}{.ENDC} {}".format(PColors, prefix, PColors, words))


def warn(prefix, words):
    print("{.YELLOW}{}{.ENDC} {}".format(PColors, prefix, PColors, words))

def yard(prefix, words):
    print("{.GREEN}{}{.ENDC} {}".format(PColors, prefix, PColors, words))
