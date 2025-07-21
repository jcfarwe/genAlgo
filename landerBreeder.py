"""
# Example usage
from genetic import *
target = 371
p_count = 100
i_length = 6
i_min = 0
i_max = 100
p = population(p_count, i_length, i_min, i_max)
fitness_history = [grade(p, target),]
for i in xrange(100):
	p = evolve(p, target)
	fitness_history.append(grade(p, target))

for datum in fitness_history:
print datum
"""
from random import randint, random, uniform
#import random
#from operator import add
import lunarLander
#from geneticAlgoritm import individual

#import sys


def create_individual(length, min, max):
	'Create a member of the population.'
	#return [ randint(min,max) for x in range(length) ]
	individual = [0,0,0,0,0,0,0,0]
	for __ in range(length - len(individual)):
		individual.append(randint(min,max))
	return individual
	#return [0,0,0,0,0,0,0,0,200,200,200,200,200,200,200,90,60,16,16,12.189,12,12,12,12,12,12,12]

def population(count, length, min, max):
	"""
	Create a number of individuals (i.e. a population).

	count: the number of individuals in the population
	length: the number of values per individual
	min: the minimum possible value in an individual's list of values
	max: the maximum possible value in an individual's list of values

	"""
	return [ create_individual(length, min, max) for __ in range(count) ]

def fitness(individual):
	"""
	Determine the fitness of an individual. Higher is better.

	individual: the individual to evaluate
	target: the target number individuals are aiming for
	"""
	#sum = reduce(add, individual, 0)
	#print individual
	speed, fuel, score = lunarLander.loop(enumerate(individual))
	print ('{:.3f},{:.3f},{:.3f};'.format(speed, fuel, score),end="")
	return (speed, fuel, score)

def grade(pop, target):
	'Find average fitness for a population.'
	summed = 0
	for x in pop:
		summed += fitness(x, target)[2]
	return summed / (len(pop) * 1.0)

def get_score(individual):
	return individual[0][2]

def evolve(pop, retain=0.7, random_select=0.05, mutate=0.3):
	graded = [ (fitness(x), x) for x in pop]
	#top_score = graded[0][0]
	graded = [ x[1] for x in sorted(graded,key=get_score,reverse=True)]
	retain_length = int(len(graded)*retain)
	parents = graded[:retain_length]
	# randomly add other individuals to
	# promote genetic diversity
	for individual in graded[retain_length:]:
		if random_select > random():
			parents.append(individual)
	# mutate some individuals
	"""for individual in parents:
		if mutate > random():
			pos_to_mutate = randint(0, len(individual)-1)
			# this mutation is not ideal, because it
			# restricts the range of possible values,
			# but the function is unaware of the min/max
			# values used to create the individuals,
			individual[pos_to_mutate] += randint(-2, 2)
			if individual[pos_to_mutate] < 0:
				individual[pos_to_mutate] = 0
			if individual[pos_to_mutate] > 200:
				individual[pos_to_mutate] = 200"""
	# crossover parents to create children
	parents_length = len(parents)
	desired_length = len(pop) - parents_length
	children = []
	while len(children) < desired_length:
		male = randint(0, parents_length-1)
		female = randint(0, parents_length-1)
		if male != female:
			male = parents[male]
			if random() > 0.001:
				female = parents[female]
			else:
				female = create_individual(30, 0, 200)
			child = []
			for i in range(0,len(male) - 1, 2):
				child.append(male[i]* 0.4 + female[i] * 0.6)
				child.append(male[i+1]* 0.6 + female[i+1] * 0.4)
			if mutate > random():
				#if top_score[0] < 2:
				#	first_gene = 0
				#	mutated_thrust = 2
				#	mutation_1 = .1
				#	mutation_2 = .2
				#else:
				first_gene = 8
				mutated_thrust = 5
				mutation_1 = 1
				mutation_2 = 2

				for __ in range(randint(0, mutated_thrust)):
					pos_to_mutate = randint(first_gene, len(child)-1)
					# this mutation is not ideal, because it
					# restricts the range of possible values,
					# but the function is unaware of the min/max
					# values used to create the individuals,
					child[pos_to_mutate] += uniform(-mutation_1, mutation_1)
					if child[pos_to_mutate] < 0:
						child[pos_to_mutate] = 0
					if child[pos_to_mutate] > 200:
						child[pos_to_mutate] = 200
					if pos_to_mutate is 0:
						pos_to_mutate += 1
					else:
						pos_to_mutate -= 1
					child[pos_to_mutate] += uniform(-mutation_2, mutation_2)
					if child[pos_to_mutate] < 0:
						child[pos_to_mutate] = 0
					if child[pos_to_mutate] > 200:
						child[pos_to_mutate] = 200

			#half = len(male) / 2
			#child = male[:half] + female[half:]
			children.append(child)
	parents.extend(children)
	return parents

if __name__ == "__main__":
#	target = 12000
	p_count = 1000
	i_length = 26
	i_min = 0
	i_max = 200

	#print(sys.version)
	# generate initial population
	p = population(p_count, i_length, i_min, i_max)
	# evaluate initial individuals
	#fitness_history = []
	# iteratively cull, breed, mutate, and evaluate successive generations
	for i in range(4000):
		print ("\nGeneration %i,"%(i),end="")
		p = evolve(p)
		#fitness_history.append(grade(p, target))

	# print out successful recipe
	print ("\n",p[0])
	#for datum in fitness_history:
	#	print datum