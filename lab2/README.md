# Lab 2 ES

## 2.1

I implemented an expert agent which is based on nim-sum: it selects the minimum value between the most populated row and the bound k (if defined), then it tests all the rows from most populated to least populated and selects a play to be returned as soon as it finds one which corresponds to a consequent nim-sum != 0, if no moves with nim-sum != 0 are possible it selects the largest value of matches to be taken (or k if the game has a bound). If it remains only a single row with 2 or more matches it selects that row and a number of objects to be taken so that an odd number of rows with one match each remains.
This agent wins against "optimal" more than 75% of the time (half of the games starting first and the other half starting second).

# 2.2

I implemented an (mu+lambda)-ES based agent which plays a move based on the weights of which row to choose ('love_small_row' that makes the system choose a low ) and how many matches to take from a row ('love_small_number' and 'love_large_number').
I sat the population size to 50 and 100 and parents selected each generation to 2, 5 and 10, everything repeated for 100 generations. The mutations are regulated by a sigma of 1 and 0.1 which updates the value of the 2 weights.
Every generation each individual gets ranked playing 10 games against every existing strategy, half starting first and half starting second; then individuals are ranked based on how many wins they have accomulated.
This agent on average performs better than "pure_random" and "gabriele" while it falls behind with "optimal" and "expert".

Here are reported some of the results obtained with different parameters:

mu = 5<br>
lam = 50<br>
sig = 1<br>
GENERATIONS = 100<br>
N_GAMES = 100<br>
Adaptive champion wins 27.0% of the time against expert<br>
Adaptive champion wins 20.0% of the time against optimal<br>
Adaptive champion wins 100.0% of the time against gabriele<br>
Adaptive champion wins 62.0% of the time against pure_random<br>

mu = 5<br>
lam = 50<br>
sig = 0.1<br>
GENERATIONS = 100<br>
N_GAMES = 100<br>
Adaptive champion wins 41.0% of the time against expert<br>
Adaptive champion wins 28.000000000000004% of the time against optimal<br>
Adaptive champion wins 100.0% of the time against gabriele<br>
Adaptive champion wins 53.0% of the time against pure_random<br>

mu = 2<br>
lam = 50<br>
sig = 0.1<br>
GENERATIONS = 100<br>
N_GAMES = 100<br>
Adaptive champion wins 49.0% of the time against expert<br>
Adaptive champion wins 28.000000000000004% of the time against optimal<br>
Adaptive champion wins 100.0% of the time against gabriele<br>
Adaptive champion wins 60.0% of the time against pure_random<br>

mu = 10<br>
lam = 50<br>
sig = 0.1<br>
GENERATIONS = 100<br>
N_GAMES = 100<br>
Adaptive champion wins 28.000000000000004% of the time against expert<br>
Adaptive champion wins 25.0% of the time against optimal<br>
Adaptive champion wins 100.0% of the time against gabriele<br>
Adaptive champion wins 55.00000000000001% of the time against pure_random<br>

mu = 10<br>
lam = 100<br>
sig = 1<br>
GENERATIONS = 100<br>
N_GAMES = 100<br>
Adaptive champion wins 50.0% of the time against expert<br>
Adaptive champion wins 25.0% of the time against optimal<br>
Adaptive champion wins 100.0% of the time against gabriele<br>
Adaptive champion wins 53.0% of the time against pure_random<br>

mu = 10<br>
lam = 100<br>
sig = 0.1<br>
GENERATIONS = 100<br>
N_GAMES = 100<br>
Adaptive champion wins 55.00000000000001% of the time against expert<br>
Adaptive champion wins 25.0% of the time against optimal<br>
Adaptive champion wins 100.0% of the time against gabriele<br>
Adaptive champion wins 56.00000000000001% of the time against pure_random<br>

Sources from which I took inspiration:
https://archimedes-lab.org/game_nim/nim.html#
https://en.wikipedia.org/wiki/Nim