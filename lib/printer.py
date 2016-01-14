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


def invalid(prefix, actions):
    print("{.YELLOW}{}{.ENDC} Sorry, I didn't understand that. Valid options are: {}".format(PColors, prefix, PColors, ", ".join(actions)))


def prompt(prefix, actions):
    print("{0} Your options are: {1}".format(prefix, ", ".join(actions)))


def p(prefix, words):
    print("{} {}".format(prefix, words))


def warn(prefix, words):
    msg = "\033[0m" + prefix
    msg = "{.RED}{}{.ENDC} {}".format(PColors, msg, PColors, words)
    print(msg)
    # print()
    # print("{.YELLOW}[DEBUG]{.ENDC} Testing...".format(PColors, PColors))
