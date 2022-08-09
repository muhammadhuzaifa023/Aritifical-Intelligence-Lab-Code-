# -*- coding: utf-8 -*-
"""
Created on Thu May 26 00:35:53 2022

@author: muham
"""
from numpy import asarray
from numpy.random import randn
from numpy.random import rand
import math
import random

#f(x,y)=e-(x^2+y^2)
def generated_sol():
    rangeX = (-2, 2)
    rangeY = (-2, 2)
    x = random.randrange(*rangeX)
    y = random.randrange(*rangeY)
    sol=x,y
    return sol
def Evaluate(sol):
    x,y=sol
    z=math.exp(-(x**2+y**2))
    return z

def in_bounds(point, bounds):
	# enumerate all dimensions of the point
	for d in range(len(bounds)):
		# check if out of bounds for this dimension
		if point[d] < bounds[d, 0] or point[d] > bounds[d, 1]:
			return False
	return True




# hill climbing local search algorithm
def hillclimbing(objective, bounds, n_iterations, step_size, start_pt):
	# store the initial point
	solution = start_pt
	# evaluate the initial point
	solution_eval = objective(solution)
	# run the hill climb
	for i in range(n_iterations):
		# take a step
		candidate = None
		while candidate is None or not in_bounds(candidate, bounds):
			candidate = solution + randn(len(bounds)) * step_size
		# evaluate candidate point
		candidte_eval = objective(candidate)
		# check if we should keep the new point
		if candidte_eval <= solution_eval:
			# store the new point
			solution, solution_eval = candidate, candidte_eval
	return [solution, solution_eval]
def iterated_local_search(objective, bounds, n_iter, step_size, n_restarts, p_size):
	# define starting point
	best = None
	while best is None or not in_bounds(best, bounds):
		best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	# evaluate current best point
	best_eval = objective(best)
	# enumerate restarts
	for n in range(n_restarts):
		# generate an initial point as a perturbed version of the last best
		start_pt = None
		while start_pt is None or not in_bounds(start_pt, bounds):
			start_pt = best + randn(len(bounds)) * p_size
		# perform a stochastic hill climbing search
		solution, solution_eval = hillclimbing(objective, bounds, n_iter, step_size, start_pt)
		# check for new best
		if solution_eval < best_eval:
			best, best_eval = solution, solution_eval
			print('Restart %d, best: f(%s) = %.5f' % (n, best, best_eval))
	return [best, best_eval]




sol=generated_sol()
print(sol)
print(Evaluate(sol))

bounds = asarray([[-2, 2], [-2, 2]])
print(in_bounds(sol, bounds))
n_iter = 1000
# define the maximum step size
s_size = 0.05
# total number of random restarts
n_restarts = 30
# perturbation step size
p_size = 1.0
# perform the hill climbing search
best, score = iterated_local_search(Evaluate, bounds, n_iter, s_size, n_restarts, p_size)
print('Done!')
print('f(%s) = %f' % (best, score))