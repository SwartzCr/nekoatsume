# 0( =^･_･^)=〇 Neko Atsume

This is a text based command line port of the phone game [Neko Atsume](https://play.google.com/store/apps/details?id=jp.co.hit_point.nekoatsume&hl=en).

## Play

This game runs in Python; to play the game do the following from a Terminal:

```
git clone https://github.com/SwartzCr/nekoatsume.git
cd nekoatsume
./nekoatsume.py
```

This builds all required database objects and begins your game.

The game doesn't currently obfurscate its data directory, stored as a large
JSON file that gets read between plays.

This should work with standard python, but requires the `time`, `datetime`,
and `json` packages.

## Roadmap

TODOs:

* [ ] Balance income with cost of items and cat arrival frequency
* [ ] Add more items
* [ ] Include fuzzy string matching for commands
