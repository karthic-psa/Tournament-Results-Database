
# DESIGN A TOURNAMENT RESULTS DATABASE #

In this project, we wrote a Python module that uses the **PostgreSQL** database to keep track of players and matches in a game tournament.

The game tournament will use the *Swiss system* for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.
This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

Modern data-driven applications require developers that know how to store data and interact programmatically with that data. 
In this project, we designed a database based off of a provided specification and use case and then write code that makes use of that data.

We architect and develop a database containing fully normalized data within multiple tables. 
We modify this data and query it to meet the demands of a variety of use cases.
Persistent data is the key feature that turns static websites into dynamic data-driven web applications
Properly establishing data relationships and using the appropriate data types ensures your applications perform efficiently and error free

## CREATING YOUR DATABASE ##
1. Before you can run your code or create your tables, you'll need to use the create database command in psql to create the database. Use the name tournament for your database.

2. Then you can connect psql to your new database and create your tables from the statements you've written in ```tournament.sql```. You can do this in either of two ways:

..1. Paste each statement in to psql.

..2. Use the command ```\i tournament.sql``` to import the whole file into psql at once.

## FUNCTIONS IN ```TOURNAMENT.PY``` ##
1. ```registerPlayer(name)```:
	Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

2. ```countPlayers()```:
	Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

3. ```deletePlayers()```:
	Clear out all the player records from the database.

4. ```reportMatch(winner, loser)```:
	Stores the outcome of a single match between two players in the database.

5. ```deleteMatches()```
	Clear out all the match records from the database.

6. ```playerStandings()```:
	Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

7. ```swissPairings()```:
Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. 
Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. 
For instance, if there are eight registered players, this function should return four pairings. 
This function should use ```playerStandings()``` to find the ranking of players.


Make sure you have Vagrant and a VM (like VirtualBox) installed.
## Instructions on running the project ##
1. Launch the Vagrant VM. 

2. cd to your project folder.

3. Launch the Vagrant VM using the following commands:
	a. Run ``vagrant up`` (and then)
	b. Run ```vagrant ssh```
	c. Then run ```cd /vagrant```
	d. Then cd to tournament(project) directory using ```cd tournament```
	
4. To build and access the database we run ```psql``` followed by ```\i tournament.sql```
(We Run the psql command in the command line to launch the *PostgreSQL* CLI)
	
5. Quit the psql command line interface(CLI) using the command '\q'

6. Finally, run the test file using ```python tournament_test.py```. The file tournament_test.py contains unit tests that will test the functions you’ve written in tournament.py.
   You can run the tests from the command line, using the command ```python tournament_test.py```.

(If you want to use the tournament functions after creating your own database, import tournament.py into your python script by using ```import tournament``` in your code.)

