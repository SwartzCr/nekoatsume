class PColors:
    BANNERR = '\033[31m'
    BANNERY = '\033[33m'
    BANNERG = '\033[32m'
    BANNERB = '\033[34m'
    BANNERP = '\033[35m'
    GOODBYE = '\033[93m'
    HELP = '\033[36m'
    INFO = '\033[37m'
    MAIN = '\033[37m'
    SHOP = '\033[95m'
    WELCOME = '\033[34m'
    YARD = '\033[92m'
    ENDC = '\033[0m'

    def disable(self):
        self.BANNERR = ''
        self.BANNERY = ''
        self.BANNERG = ''
        self.BANNERB = ''
        self.GOODBYP = ''
        self.HELP = ''
        self.INFO = ''
        self.MAIN = ''
        self.SHOP = ''
        self.WELCOME = ''
        self.YARD = ''
        self.ENDC = ''


def invalid(prefix, actions):
    print("{0} Sorry, I didn't understand that. Valid options are: {1}".format(
        prefix, ", ".join(actions)))


def prompt(prefix, actions):
    print("{0} Your options are: {1}".format(prefix, ", ".join(actions)))


def p(prefix, words):
    print("{0} {1}".format(prefix, words))
