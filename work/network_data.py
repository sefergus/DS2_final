#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:50:04 2020

@author: sarafergus
"""

import data as d
import matplotlib.pyplot as plt
import statistics as stats
import math

''' Network '''

lists, labs = d.load_university_data()


def plot_data():
    '''initial data analysis. Plots information about means, outliers, 
    and number of data points'''
    #get means
    means = []
    lengths = []
    for item in lists:
        means.append(stats.mean(item))
        lengths.append(len(item))
    means = [math.log(x) for x in means]

    print('lengths of all: ', lengths[0])

    #get outliers
    high1, high2, high3, low1, low2, low3 = d.get_outliers(means, labs)

    #plot means
    plt.figure(figsize=(10, 4))
    plt.subplot(121)
    plt.hist(means)
    plt.axvline(stats.mean(means), ls='--', color='C01')
    plt.legend(['Mean = \n' + str(round(stats.mean(means), 4))])
    plt.xlabel("Log of Average Latency")
    plt.ylabel("Number of Universities")
    plt.subplot(122)
    plt.boxplot(means)
    #outliers
    plt.annotate(str(low1), (1.03, 3.3))
    plt.annotate(str(low2), (0.75, 3.4))
    plt.annotate(str(low3), (0.75, 3.7))
    plt.annotate(str(high1), (1.03, 9.5))
    plt.xticks([1], ['Box Plot of Average Latency'])
    plt.ylabel('Log of Average Latency')
    plt.annotate(
        'Median = \n' + str(round(stats.median(means), 4)), (1.3, 9),
        bbox=dict(boxstyle="round", fc="none", ec="#d3d3d3"))
    plt.suptitle('Content Distribution Network Data (True)')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('../figures/initial_data/CDN', dpi=300)
    plt.show()

    #plot indivudal examples
    low1_list = lists[439]
    low1_list.sort()
    low2_list = lists[713]
    low2_list.sort()
    low3_list = lists[347]
    low3_list.sort()
    plt.figure(figsize=(10, 4))
    plt.subplot(121)
    d.ccdf(low1_list, 'St. John\'s')
    d.ccdf(low2_list, 'Villanova')
    d.ccdf(low3_list, 'Top 3 Networks')
    plt.legend([
        'St. John\'s \n mean:' + str(round(stats.mean(low1_list), 2)),
        'Villanova \n mean:' + str(round(stats.mean(low2_list), 2)),
        'Pace \n mean:' + str(round(stats.mean(low3_list), 2))
    ])
    plt.axvline(stats.mean(low1_list), ls='--', color='C0')
    plt.axvline(stats.mean(low2_list), ls='--', color='C1')
    plt.axvline(stats.mean(low3_list), ls='--', color='C2')
    #plt.show()
    plt.subplot(122)

    plt.yscale('log')
    plt.title('Boxplots of Top 3 Networks')
    plt.boxplot([low1_list, low2_list, low3_list])
    plt.xticks([1, 2, 3], [
        'St. John\'s \n median: ' + str(round(stats.median(low1_list), 2)),
        'Villanova \n median: ' + str(round(stats.median(low2_list), 2)),
        'Pace  \n median: ' + str(round(stats.median(low3_list), 2))
    ])
    plt.suptitle('Network Latencies (True)')
    plt.savefig('../figures/initial_data/CDN_ex', dpi=300)
    plt.show()


''' Function Call '''
#plot_data()
