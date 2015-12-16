# nekoatsume
a commandline neko atsume game

This is a text only port of the phone game neko atsume: https://play.google.com/store/apps/details?id=jp.co.hit_point.nekoatsume&hl=en  

This game runs in python, to start type 'python display.py' and the game will buld all required database objectsand begin your game.

Currently the game doesn't obfurscate it's data directory, which is stored as a large json file that is read between plays.

This should work with standard python, but requires time, datetime, and json packages.

Todos:
* Balance income with cost of items and cat arrival frequency
* Add more items
* include fuzzy string matching for commands
