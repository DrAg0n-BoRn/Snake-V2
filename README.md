# CLASSIC SNAKE GAME

## Description:

Hello, World! This is my final project for the course CS50x by Harvardx. 

My inspiration comes from video-games. I started playing video-games at a young age, with the ATARI system and the first Nintendo console.
In this project I have recreated one of my favorite games. Based on the first game I played on my first mobile phone: Snake.

A big thanks to the instructor Angela Yu from The London APP Brewery for providing me with all the basic knowledge about Python programming. She has been my mentor, and provided me with the building blocks that made this project possible.

I used Python and its in-built libraries: 
* turtle
* tkinter 
* sqlite3 
* time
* random
* datetime

I practiced using Object Oriented Programming to make a Snake class using turtles to add up segments. Next, a Food class which is a single turtle jumping randomly across the screen. Finally, a Scoreboard class that uses an invisible turtle to write the score on the screen.

After the basic logic of the game was implemented, I decided to interact with the player(s) using tkinter's simple dialogs. This way I can know the name of the player and if he wants to continue playing after a game session is over.

To store this data I used Python's sqlite3. The project is able to successfully CRUD data. Many bugs and issues have been addressed thanks to the help of Google, Stackoverflow, but mostly the print() function and my perseverance.

### Snake Class

It creates a new instance of turtle everytime the "head" comes closer to a "food" turtle.

Since turtles cannot be deleted from the screen, I have come up with a way to recycle them. After a game is over (snake touching its body segment or touching the wall) all turtles that made part of the snake's body become "hidden" and are no longer attached to the head. 

Once the new head comes closer to a "food" turtle again, an old instance of a segment turtle gets recycled instead of creating a new turtle.
I believe this can greatly improve performance and memory usage. Without this, the longer the game keeps going, the more turtles that would be created. 

The Snake class uses a method called initialize(), that gets called every time a new session starts. I think this method can be further improved and made more efficient, so I will be keeping track of it.

### Food Class

This is actually a very simple part of the code. It uses a single instance of turtle, that becomes hidden when touched and quickly moves to another random position. It then becomes visible again. 

### Scoreboard Class

This is the most complex class. Originally it had to be a single turtle in charge of drawing the score on the display. However it turned very complicated once I included the possibility to track players and high scores using a SQLite database.

I think a different approach would have been using a different class for the database, but I wanted to try and merge everything together and see how I could make it work.

By using some extra functions, the Scoreboard class is able to interact with the user and store responses in the database. For the interaction I used tkinter prompt boxes.

### Game Over

After a game is over a tkinter window pops up showing the scoreboard. By using a sqlite3 query, I restructured the data into a dictionary for the top 3 players. This way I can call a single function to plot all results on a tkinter canvas. And the code can be easily changed to plot even more results if needed.

## Final Thoughts

In the future I plan to further improve the design. I have been reading about how to embed the turtle module inside a Tkinter canvas. This would allow me to include control buttons and other features that improve the user experience.

This seems quite challenging, but I just need to read more documentation and find solutions to the problems. I am confident it will be implemented. Afterwards, I will move on to new projects and practice with some different python libraries.

A special thanks to the instructors David J. Malan and Doug Lloyd, whom I learned so much from and made all of this possible.

### Video Demo: [Link](https://youtu.be/e0_a8mjqIQY)
