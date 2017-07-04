-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE tournament;

CREATE DATABASE tournament;
\c tournament;

-- Table for Players

CREATE TABLE players (name TEXT NOT NULL,
					  id SERIAL PRIMARY KEY);
					  --age INTEGER NOT NULL,
					  --CONSTRAINT chk_age CHECK (age BETWEEN 1 AND 90)
					 
-- Table for Matches

CREATE TABLE matches (matid SERIAL primary key,
				      win INTEGER NOT NULL REFERENCES players(id),
					  lose INTEGER NOT NULL REFERENCES players(id)
					  CONSTRAINT chk_wl CHECK (win!=lose));
					 
-- View for Player Standings
                      
CREATE VIEW score AS SELECT id, name, (SELECT COUNT(win) FROM matches WHERE id = win) as wins,
									  (SELECT COUNT(*) FROM matches WHERE id=win OR id=lose) as matches
									   FROM players LEFT JOIN matches on id = win GROUP BY id
									   ORDER BY wins DESC;