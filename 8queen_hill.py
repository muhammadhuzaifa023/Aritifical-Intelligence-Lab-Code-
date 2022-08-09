import random

def gen_solution():
    sol = [(random.randint(0,7)) for _ in range(8)]
    return sol

def evaluate(sol):
    count = 0
    for i in range(len(sol)):
        for j in range(len(sol)):
            if i == j:
                continue
            if sol[i] == sol[j]:
                count += 1

            if abs(i-j) == abs(sol[i] - sol[j]):
                count += 1

    return count

def gen_neighbor(sol):
    index = random.randint(0,len(sol)-1)
    sol[index] = random.randint(0,7)
    return sol

sol = gen_solution()
print(sol)
score = evaluate(sol)

count= 0
while True:
    count += 1
    print(count, sol, score)
    new_sol = list(sol)

    if score == 0:
        break

    new_sol = gen_neighbor(new_sol)
    new_score = evaluate(new_sol)

    if new_score < score:
        sol = new_sol
        score = new_score
