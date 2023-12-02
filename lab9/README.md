I used a GA (most of the code comes from [here](https://github.com/squillero/computational-intelligence/blob/master/2023-24/set-covering_ea.ipynb)) with a crossover operation copied by the course's slides with a twist: the best parent (based on fitness) among the 2 chosen get to pass its genes with 70% of probability while the other weaker parent does the same thing with 30% probability. The resulting individual gets mutated and inserted into the population. Then every offspring gets evaluated and only the top individuals get to pass to the next generation (1000 generations in total).  

Here are the parameters used to obtain some results:

POPULATION_SIZE = 200  
OFFSPRING_SIZE = 300  
TOURNAMENT_SIZE = 2  
PROBLEM_SIZE = 2  
GENOME_SIZE = 1000  

Problem size: 1  
Max fitness: 100.00%  
Number of fitness calls: 28100  

Problem size: 2  
Max fitness: 100.00%  
Number of fitness calls: 240200  

Problem size: 5  
Max fitness: 61.00%  
Number of fitness calls: 300200  

Problem size: 10  
Max fitness: 33.00%  
Number of fitness calls: 300200
