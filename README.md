### Vaxman is like Pacman but with a V.

In Vaxman, you need to collect all the yellow dots before the coronavirus ghosts take over your screen. Every 30 seconds each corona-ghost will spilt itself in two, once the number ghostVID19s reaches 32 times their starting number (that'd be 128), the pacman race will be wiped out. That's bad. Fear not, no viral specter can survive being rammed with your uber covid-19 vaccination!
Made for Electronic Art's Forage task 1.

![Pacman Game Window](https://raw.github.com/hbokmann/Pacman/master/images/pacman.jpg)


# Future development

* Rewrite code for style consistency, less redundancy, and just plain more better
* Make covid ghosts run away when vaxman is within their line of sight
* Change sprites to more lore-relevant images
* Esc should pause the game
* Fix bug: Win screen displays when window is closed after winning the game once
* Fix bug: Raised exception when quitting the game in some cases.
* Fix bug: Intersection dots are drawn on top of entities in some cases.

# Alternate design idea

* Ghosts enter the field every time interval
* Game starts with one infected ghost, which spreads the plague
* Ghosts either die or recover from covid
* Vaxman can get and spread covid too
* After awhile, vaccines appear in the game, which when collected allow vaxman to immunize ghosts, preventing them from being infected
* Once all ghosts are vaccinated the game is won
* If all ghosts or vaxman dies, the game is lost

Tested with PyGame 2.0.1 and Python 3.9.1 64bit

### Additional resources
* See https://github.com/hbokmann/Pacman
