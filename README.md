# PingPongLeague:
Creates weekly matchups for a 2 v 2 ping pong league by using pandas to read in players' previous teammates and league positions from an excel file, then the [matching library](https://github.com/daffidwilde/matching/tree/3baec44dd7e039fa82db24efc7646c38017c01b6), created by Henry Wilde, to run the Stable Roomate algorithm on the players to create stable pairings.

## Invariants:
This program asserts that players can not be matched with someone they have either played with or that is in the same quartile of the league table as them. To accomplish this, all players that would create invalid matches for the current player get added to the end of the current players' preference list (This is to maintain the invariant for stable roomates that all players have equal sized preference lists[^1].)

[^1]: [Irving_1985](https://uvacs2102.github.io/docs/roomates.pdf)

However, because the stable roomates algorithm is not always guaranteed to produce stable matchings, if invalid matchings are created all one has to do is re-run the program.

To ensure all valid players have equal chance of being matched, every players preference list is randomized before invalid players are added to the end of the list.

## Excel File:

To have a valid excel file for this program, it must have two sheets. Sheet 1 should be titled "Players Teamates" where players are listed (doesn't matter which order - I've done alphabetically) in the first column, column A, of the sheet. In the following columns, their matched-up teammates should be added for each week. Sheet 2 should be titled "League Table" where players are sorted into their current league positions, this matters for making the correct quartiles."

## Matching Object:
The matching library is most easily installed using pip:

$ python -m pip install matching

If this does not work, further instructions can be found [here](https://github.com/daffidwilde/matching/blob/3baec44dd7e039fa82db24efc7646c38017c01b6/INSTALLATION.rst)
