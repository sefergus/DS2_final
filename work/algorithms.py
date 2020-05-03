#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:34:37 2020

@author: sarafergus
"""
import random
import measures as m
import math

'''Helper Functions'''

def find_best(mab_inst):
    '''
    Determine which arm is the true or estimated best. 
    @params: list of arms, whether to return true best or estimated best
    @return: best arm
    '''
    highest = 0
    best = None
    for item in mab_inst.arms:
        if mab_inst.est == False:
            if item.r_true > highest:
                highest = item.r_true
                best = item
        else:
            if item.r_est > highest:
                highest = item.r_est
                best = item
    if mab_inst.est == False and best != None:
        best.set_best()
    #ties
    if best == None:
        best = random.choice(mab_inst.arms)
        best.set_best()
    return best


def best_UCB1(mab_inst):
    '''Use different measure to estimate the best for UCB method'''
    highest = 0
    best = None
    best_list = []
    for r in mab_inst.arms:
        UCB = max(r.UCB_vals)
        if UCB > highest:
            highest = UCB
            best = r
        elif UCB == highest:
            best_list.append(r)
    if len(best_list) != 0:
        return random.choice(best_list)
    else:
        return best


def num_trials(mab_inst):
    '''Determine how many pulls of each arm  in exploration
    for epsilon algorithms, based on total length of gamble'''
    divide = mab_inst.plays / len(mab_inst.arms)
    return int(round(0.2 * divide, 0))


def eps_gen(mab, num):
    '''Helper function for epsilon algorithms'''
    regret_time = []
    for j in range(1, len(mab.arms) + 1):
        for s in range(num):
            mab.arms[j - 1].play(update=True)
            regret_time.append(m.regret(mab, (j - 1) * num + s))
    best = find_best(mab)
    return best, regret_time


def eps_gen2(best, regret_time, j, mab):
    '''Helper function for epsilon algorithms'''
    best.play(update=False)
    regret_time.append(m.regret(mab, j))
    return regret_time


'''Algorithms'''


def rand_strat(mab_inst):
    '''play arm at random'''
    for i in range(mab_inst.plays):
        arm = random.choice(mab_inst.arms)
        arm.play(update=False)


def greedy(mab_inst):
    '''play arm with best estimated mean, and update estimated mean'''
    for r in mab_inst.arms:
        r.set_est(mab_inst.epsilon)
    for j in range(mab_inst.plays):
        best = find_best(mab_inst)
        best.play(update=True)


def eps_first(mab):
    '''pull each arm num times, then play the best arm for the rest of 
    the gamble'''
    num = num_trials(mab)
    best, regret_time = eps_gen(mab, num)
    for j in range(num * len(mab.arms) + 1, mab.plays + 1):
        regret_time = eps_gen2(best, regret_time, j, mab)


def elimination(mab):
    '''pull each arm, remove the worst arm. Repeat until there is only
    1 arm to play for the remainder of the gamble'''
    dont_play = []
    i = 0
    while i <= mab.plays:
        if len([r for r in mab.arms if r not in dont_play]) > 1:
            for r in [r for r in mab.arms if r not in dont_play]:
                r.play(update=True)
                i += 1
            lowest = random.choice([r for r in mab.arms if r not in dont_play])
            for r in [r for r in mab.arms if r not in dont_play]:
                if r.r_est < lowest.r_est:
                    lowest = r
            dont_play.append(lowest)
        else:
            for r in [r for r in mab.arms if r not in dont_play]:
                r.play(update=True)
                i += 1


def eps_greedy(mab):
    '''pull each arm num times, then play the arm with the highest estimated mean
    and update estimated mean'''
    num = num_trials(mab)
    #epsilon: probability of pulling a random arm
    best, regret_time = eps_gen(mab, num)
    for j in range(num * len(mab.arms) + 1, mab.plays + 1):
        if random.random() < mab.epsilon:
            arm = random.choice(mab.arms)
            arm.play(update=True)
            best = find_best(mab)
            regret_time.append(m.regret(mab, j))
        else:
            regret_time = eps_gen2(best, regret_time, j, mab)


def UCB1(mab):
    '''Pull each arm once. Pull arm who at any point had the highest upper
    confidence bound'''
    for r in range(len(mab.arms)):
        mab.arms[r].play(update=True)
        mab.arms[r].UCB_vals.append(
            mab.arms[r].r_est + math.sqrt(2 * math.log(r + 1, math.e)))
    for j in range(mab.plays - len(mab.arms)):
        best = best_UCB1(mab)
        best.play(update=True)
        best.UCB_vals.append(best.r_est + math.sqrt(
            2 * math.log(len(mab.all_plays), math.e) / len(best.plays)))
