# PingPongLeague
Creates weekly matchups for a 2 v 2 ping pong league by using pandas to read in players' previous teammates and league positions from an excel file, then the matching object, created by Henry Wilde and can be viewed at https://github.com/daffidwilde/matching/tree/3baec44dd7e039fa82db24efc7646c38017c01b6/src/matching, to run the Stable Roomate algorithm on the players to create stable pairings.

Invariants:
This program asserts that players can not be matched with someone they have either played with or that is in the same quartile of the league table as them. To accomplish this, all players that would create invalid matches for the current player get added to the end of the current players' preference list (This is to maintain the invariant for stable roomates that all players have equal sized preference lists. (Irving 85))

However, because the stable roomates algorithm is not always guaranteed to produce stable matchings, if invalid matchings are created all one has to do is re-run the program.

To ensure all valid players have equal chance of being matched, every players preference list is randomized before invalid players are added to the end of the list.
