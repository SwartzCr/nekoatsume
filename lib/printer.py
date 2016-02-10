"""
Print output.

This module handles special printing of output to player including
colorization of game areas.
"""


class PColors:
    """Define some colors up in this piece."""

    RED = '\033[31m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    GOODBYE = '\033[93m'
    HELP = '\033[36m'
    MAIN = '\033[37m'
    SHOP = '\033[95m'
    YARD = '\033[32m'
    ENDC = '\033[0m'

    def disable(self):
        """Disable colorization and revert to plain text."""
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


def invalid(prefix):
    """Apologize for not understand user input"""
    print("{0} Sorry, I didn't understand that.".format(prefix))

def fail(prefix, words):
    """Print failure messages."""
    if prefix == '[Item Shop]':
        print("{.SHOP}{}{.ENDC} {.RED}{}{.ENDC}".format(
            PColors, prefix, PColors, PColors, words, PColors))
    elif prefix == '[Yard]':
        print("{.YARD}{}{.ENDC} {.RED}{}{.ENDC}".format(
            PColors, prefix, PColors, PColors, words, PColors))
    else:
        print("{.MAIN}{}{.ENDC} {.YELLOW}{}{.ENDC}".format(
            PColors, prefix, PColors, PColors, words, PColors))

def prompt(prefix, actions):
    """Action prompt."""
    options = ", ".join(actions)
    prompt = "Your options are:"
    if prefix == '[Item Shop]':
        print("{.SHOP}{}{.ENDC} {} {}".format(
            PColors, prefix, PColors, prompt, options))
    elif prefix == '[The Yard]':
        print("{.YARD}{}{.ENDC} {} {}".format(
            PColors, prefix, PColors, prompt, options))
    else:
        print("{.MAIN}{}{.ENDC} {} {}".format(
            PColors, prefix, PColors, prompt, options))


def p(prefix, words):
    """Print plain messages."""
    print("{} {}".format(prefix, words))


def shop(prefix, words):
    """Print shop messages."""
    print("{.SHOP}{}{.ENDC} {}".format(PColors, prefix, PColors, words))


def success(prefix, words):
    """Print success messages."""
    if prefix == '[Item Shop]':
        print("{.SHOP}{}{.ENDC} {.GREEN}{}{.ENDC}".format(
            PColors, prefix, PColors, PColors, words, PColors))
    elif prefix == '[The Yard]':
        print("{.YARD}{}{.ENDC} {.GREEN}{}{.ENDC}".format(
            PColors, prefix, PColors, PColors, words, PColors))
    elif prefix == '[Welcome!]':
        print("{.YARD}{}{.ENDC} {.GREEN}{}{.ENDC}".format(
            PColors, prefix, PColors, PColors, words, PColors))
    else:
        print("{.MAIN}{}{.ENDC} {.GREEN}{}{.ENDC}".format(
            PColors, prefix, PColors, PColors, words, PColors))


def warn(prefix, words):
    """Print warning messages."""
    if prefix == '[Item Shop]':
        print("{.SHOP}{}{.ENDC} {.YELLOW}{}{.ENDC}".format(
            PColors, prefix, PColors, PColors, words, PColors))
    elif prefix == '[The Yard]':
        print("{.YARD}{}{.ENDC} {.YELLOW}{}{.ENDC}".format(
            PColors, prefix, PColors, PColors, words, PColors))
    else:
        print("{.MAIN}{}{.ENDC} {.YELLOW}{}{.ENDC}".format(
            PColors, prefix, PColors, PColors, words, PColors))


def yard(prefix, words):
    """Print yard messages."""
    print("{.GREEN}{}{.ENDC} {}".format(PColors, prefix, PColors, words))
