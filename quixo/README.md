I implemented an agent which chooses its moves based on a MiniMax strategy extended with alpha-beta pruning. The policy takes into account both final states and intermediate ones: the latter category includes every state which is not final and their value is computed as the maximum number of the agent's symbols in a single row/column/diagonal, divided by 5. The value of a winning state is +1 and the one corresponding to a losing one is -1. The MiniMax depth is set to 2 as default since the simulation time is much worse with 3 or higher depths while no real improvement is measured.
When playing against a completely random agent, my MiniMax agent wins 95+ out of 100 games, both when playing first or second.