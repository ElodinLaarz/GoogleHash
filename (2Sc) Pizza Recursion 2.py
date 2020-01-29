# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np


# %%
with open('data/d_quite_big.in') as file:
    data = file.read().split()

data = [int(_) for _ in data]
MAXSLICES = data[0]
TYPES = data[1]
PIZZAS = data[2:]
pizza_dict = {pizza: index for index, pizza in enumerate(PIZZAS)}


# %%
def create_prob_list(size = 1, dist = np.random.uniform):
    prob_list = sorted(dist(size = size))
    total = sum(prob_list)
    prob_list = prob_list/total
    return prob_list


# %%
def step(max = MAXSLICES, pizza_list = PIZZAS):
    admissible_pizzas = [pizza for pizza in pizza_list if pizza <= max]
    if admissible_pizzas:
        num_pizzas = len(admissible_pizzas)
        prob_list = create_prob_list(size=num_pizzas, dist=lambda size: np.random.exponential(scale = 1, size = size))
        index = np.random.choice(num_pizzas,p=prob_list)
        rand_pizza = admissible_pizzas.pop(index)
        new_max = max - rand_pizza
        return rand_pizza, new_max, admissible_pizzas
    return (), -1, []


# %%
def deterministic_step(target = 10000, pizza_list = PIZZAS):
    admissible_pizzas = [pizza for pizza in pizza_list if pizza <= max]
    for admissible_pizzas:


# %%
def recursion(max = MAXSLICES, pizza_list = PIZZAS):
    final_list = []
    while (max >= 0):
      admissible_pizzas = [pizza for pizza in pizza_list if pizza <= max]
      if admissible_pizzas:
        num_pizzas = len(admissible_pizzas)
        prob_list = create_prob_list(size=num_pizzas, dist=lambda size: np.random.exponential(scale = 0.0001, size = size))
        index = np.random.choice(num_pizzas,p=prob_list)
        rand_pizza = admissible_pizzas.pop(index)
        pizza_list = admissible_pizzas
        max = max - rand_pizza
        final_list.append(rand_pizza)
      else:
        max = -1
    return final_list


# %%
MAX = 1000000
output = recursion(max = MAX)
remaining = [p for p in PIZZAS if p not in output]
total = sum(pizza for pizza in output)
print(f'Total = {total} \n diff = {MAX - total}')


# %%
t = sorted(output)


# %%



