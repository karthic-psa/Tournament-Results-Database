#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2



def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
	    return psycopg2.connect("dbname=tournament")
    except:
	    print("Cannot conncet to DATABASE")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cu = db.cursor()
    cu.execute('DELETE FROM matches;')
    db.commit()
    db.close()
	

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cu = db.cursor()
    cu.execute('DELETE FROM players;')
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cu = db.cursor()
    cu.execute('SELECT COUNT(*) FROM players;')
    results = cu.fetchone()
    return results[0]
    db.close()

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cu = db.cursor()
    cu.execute('INSERT INTO players VALUES (%s);',(name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cu = db.cursor()
    cu.execute('SELECT * FROM score;')
    results = cu.fetchall()
    #db.commit()
    return results
    db.close()
    


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cu = db.cursor()
    cu.execute('INSERT INTO matches (win,lose) VALUES (%s,%s);',(winner,loser,))
    db.commit()
    db.close() 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    scores = playerStandings()
    nop = int(countPlayers())
    swPairings = []
    a = 0
    if (nop>0):
		for i in range (0,nop/2):
			id1 = scores[a][0]
			name1 = scores[a][1]
			id2 = scores[a+1][0]
			name2 = scores[a+1][1]
			tupPair = (id1,name1,id2,name2)
			swPairings.append(tupPair)
			a = a+2
    return swPairings


