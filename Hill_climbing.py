import random
import string

guess = 'this !!'


def generate_solution(len_guess):
    return([random.choice(string.printable) for _ in range(len_guess)])

def evaluate(sol, guess):
    fitness = 0
    for i in range(len(guess)):
        fitness += abs(ord(sol[i])-ord(guess[i]))
    return fitness

def gen_neighbor(sol):
    index = random.randint(0,len(sol)-1)
    sol[index] = random.choice(string.printable)
    return sol

#
sol = generate_solution(len(guess))
print(sol)
print(evaluate(sol,guess))
# print(gen_neighbor(sol))
# print(evaluate(sol, guess))
counter = 0
while True:
    counter += 1
    score = evaluate(sol, guess)


    print(counter, sol, score)
    new_sol = list(sol)
    if score == 0:
        break

    gen_neighbor(new_sol)
    new_score = evaluate(new_sol, guess)

    if score > new_score:
        sol = new_sol
        score = new_score


