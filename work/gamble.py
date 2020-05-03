# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Tue Mar 17 16:21:03 2020

@author: sarafergus
"""
from MAB import mab
import measures as m
import numpy as np
from itertools import chain

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import algorithms as a
import statistics as stats
import matplotlib.pyplot as plt
import data as d
from wine_data import countries
from presidents_data import dem, rep
from click_bait import clicks
from network_data import lists

presidents = [dem, rep]


def printProgressBar(iteration,
                     total,
                     prefix='',
                     suffix='',
                     decimals=1,
                     length=100,
                     fill='█',
                     printEnd="\r"):
    """
    BORROWED from: https://stackoverflow.com/questions/3173320/text-
                   progress-bar-in-the-console 
             user: Greenstick
    """
    percent = ("{0:." + str(decimals) + "f}").format(
        100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def choose_trial(mean, data):
    '''Create list of "strategies" for parallel processing. Use Basic 
    6 algorithms, intialize greedy with the mean (parameter) and pass in
    either data set or distribution (parameter)'''
    return ([(a.rand_strat, 0.25, data), (a.greedy, mean, data),
             (a.eps_first, 0.5, data), (a.eps_greedy, 0.5, data),
             (a.UCB1, 1.1, data), (a.elimination, 0.25, data)])


def pmap(fn, iterable):
    '''Parallel Processing: run all algorithms at the same time'''
    with ProcessPoolExecutor() as executor:
        return list(executor.map(fn, iterable))


def one_strategy(gambles,
                 plays,
                 arms,
                 algorithm,
                 epsilon,
                 data=None,
                 distribution=None,
                 index=[10 * p for p in range(100)]):
    '''Run the gamble on a particular algorithm. Create an MAB (change faulty here), collect results for all of the separate gambles of lengths corresponding 
    with entries of "index"'''
    all_regrets = []
    all_opt = []
    all_rew = []
    all_avg = []
    mab_inst = mab(
        arms,
        plays=plays,
        gambles=gambles,
        data=data,
        dist=distribution,
        faulty=False)
    index = index
    for i in index:
        mab_inst.plays = i
        mab_inst.epsilon = epsilon
        regret_list, opt_list, rew, avg, total_plays = mab.gamble(
            mab_inst, algorithm)
        if i != index[-1]:
            total_plays = []
        mab_inst.all_plays = []
        all_regrets.append(stats.mean(regret_list))
        all_opt.append(stats.mean(opt_list))
        all_rew.append(stats.mean(rew))
        all_avg.append(stats.mean(avg))
        printProgressBar(iteration=i / 10, total=100, length=50)
    return all_regrets, all_opt, all_rew, all_avg, total_plays


def map_strategy(strat):
    '''Parallel Processing, put information into the one_strategy method
    Change third parameter of theoretical call as necessary'''
    algorithm, epsilon, data = strat
    if type(data) == str:
        #change third parameter based on number of arms in theory
        return one_strategy(100, 0, 720, algorithm, epsilon, distribution=data)
    print('arms: ', len(data))
    return one_strategy(100, 0, len(data), algorithm, epsilon, data=data)


def int_regret(strategies, results):
    '''Calculate internal regret'''
    total_plays = []
    for j in range(len(strategies)):
        if j != 0:
            means = np.mean(np.array(results[j][-1]), axis=0)
            total_plays = np.vstack((total_plays, means[:990]))
        else:
            means = np.mean(np.array(results[j][-1]), axis=0)
            total_plays = np.array(means)
    internal = m.internal_regret(list(total_plays))

    new_lists = []
    for i in internal:
        lst = i
        n = 10
        temp = list(
            chain.from_iterable(
                [stats.mean(lst[i:i + n])] for i in range(0, len(lst), n)))
        new_lists.append(temp)
    return new_lists


def plotting(strategies, new_lists, results):
    '''Plot results'''
    index = [10 * p for p in range(100)]
    plt.figure(figsize=(20, 7))
    titles = ["External Regret", "Percent Optimal Pulls", "Internal Regret"]
    for j in range(2):
        plt.subplot(130 + j + 1)
        for i in range(len(strategies)):
            plt.plot(index[1:], results[i][j][1:])
            plt.xlabel("Gamble Length")
            plt.legend(['Random', 'Greedy', '$\epsilon$-first', '$\epsilon$-greedy',
                'UCB1', 'Elimination'])
            plt.ylabel(titles[j])
    plt.subplot(133)
    for item in new_lists:
        plt.plot(index[1:], item)
    plt.legend(['Random', 'Greedy', '$\epsilon$-first', '$\epsilon$-greedy', 'UCB1',
        'Elimination' ])
    plt.ylabel('Internal Regret')
    plt.xlabel("Pull Number")

    plt.suptitle( "Gambles of up to 1000 Pulls \n Network Data Set (Theoretical)")
    plt.show()


'''Function Calls'''

strategies = choose_trial(87, countries)  #wine
#strategies = choose_trial(616111, lists)           #CDN
#strategies = choose_trial(15, presidents)          #Nat'l Debt
#strategies = choose_trial(0.04, clicks)            #Click Bait
#strategies = choose_trial(87, 'normal')            #Theo wine
#strategies = choose_trial(15, 'normal_pres')       #Theo Nat'l Debt
#strategies = choose_trial(616111, 'exponential')   #Theo CDN
#strategies = choose_trial(0.04, 'bernoulli')       #Theo Click Bait

results = pmap(map_strategy, strategies)
internal = int_regret(strategies, results)
plotting(strategies, internal, results)
