#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:34:38 2020

@author: sarafergus
"""
import algorithms as a


def regret(mab, p):
    '''
    Calculate Regret
    @params: list of arms, number of plays
    @returns: regret of gamble (float)
    '''
    mab.est = False
    best = a.find_best(mab)
    r_star = best.r_true
    total_reward = 0
    for item in mab.arms:
        total_reward += sum(item.plays)
    regret = p * r_star - total_reward
    mab.est = True
    return regret


def internal_regret(results):
    '''Compare the algorithms performance to the performance of every other option'''
    # print(results)
    int_regret = [[] for item in results]
    for i in range(len(results[0])):
        best = max([item[i] for item in results])
        for j in range(len(int_regret)):
            int_regret[j].append(best - results[j][i])
    return int_regret


def optimal(mab, p):
    '''Determine Percent of time the optimal arm was pulled'''
    if p == 0:
        return 0
    for r in mab.arms:
        if r.best == True:
            return len(r.plays) / p


def cum_reward(mab):
    ''' Calculate Cumulative Reward'''
    total_reward = 0
    for item in mab.arms:
        total_reward += sum(item.plays)
    return total_reward


def average_reward(mab, p):
    if p == 0:
        return 0
    average_reward = cum_reward(mab) / p
    return average_reward
