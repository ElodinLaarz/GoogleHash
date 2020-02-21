#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys

def getDist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def run(rides, bonus, output):
    total_score = 0
    for line in output:
        l = line.split()
        num_rides = int(l[0],10)
        last_time = 0
        last_pos = (0,0)
        vehicle_score = 0
        for i in range(num_rides):
            score = 0
            ride = rides[int(l[i+1],10)]
            try:
                last_time += getDist(last_pos, (ride[0], ride[1]))
                last_pos = (ride[0],ride[1])
                assert(last_time <= ride[4])
                score += bonus
            except AssertionError:
                pass
            try:
                last_time += getDist((ride[0], ride[1]), (ride[2], ride[3]))
                last_pos = (ride[2],ride[3])
                assert(last_time <= ride[5])
                score += getDist((ride[0], ride[1]), (ride[2], ride[3]))
            except AssertionError:
                continue
            vehicle_score += score
        total_score += vehicle_score
    #print(f'Final score: {total_score}')
    #print("Final score: " + str(total_score))
    return total_score





