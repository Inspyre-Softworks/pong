# InsPyPong

### Usage 
'''bash

$>./InsPyPong ~p1=Taylor ~p1c=pink ~p2=Steve ~p2c=green +v 

```

The above command would start the pong game with all player attributes defined. 
  - Player one would be named **Taylor**(*~p1=Taylor*<sup>[1](#p1arg)</sup>) and would have a paddle that is **pink** in
  color(*~p1c=pink*<sup>[2](#p1carg)</sup>).
  - Player two would be named **Steve**(*~p2=Steve*) and would have a paddle that is **green** in color (*~p2c=green*).
  - With the +v flag (or the \~~verbose modifier argument) the program will run in verbose mode where it will spit a 
  bunch of output to it's console that the program believes you might find useful.

![Screenshot 1](https://raw.github.com/Inspyre-Softworks/pong/dev1.6/docs/screen1.png?raw=true)


## Starting without arguments
  
There is no problem with just starting the game like so:

```bash
$>./InsPyPong.py # Note that there are no arguments present
```

The game will just be pre-empted by the InsPyPong Start screen which will allow you to configure your two pong players.

![Screenshot 2](https://raw.github.com/Inspyre-Softworks/pong/dev1.6/docs/screen2.png?raw=true)

See the Pong by [Inspyre Softworks wiki](https://github.com/tayjaybabee/pong/wiki) for more detailed information.


 <a name="p1arg">1</a>: To find out more about this argument please visit the wiki.
 
 
 <a name="p1carg">2</a>: This argument takes two types of strings. One containing html color hexcode, or one containing a color name. 
 
## ToDo

### Deployment

- Create an EXE file for InsPyPong on Windows
- Assemble project into an installable pypi package

### Asthetic Options


- Give the user the ability to change the game's background color
- Give the user the ability to change the background to an image of their choosingProvide a selection of images for
 backgrounds 
- Assign user's paddle color to their name on the scoreboard
- Create a dual coloring schema for player scores. For example, the score that currently ahead in points can be
  displayed in green while the lowest current score can be shown in red. This should assist players in spending less
  time trying to assess the scoring situation and more time situating their score
 
