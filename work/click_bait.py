#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:35:54 2020

@author: sarafergus
"""
import data as d
import matplotlib.pyplot as plt
import statistics as stats


''' Clicks '''

clicks, lab = d.load_click_data()


def plot_data():
    '''Initial data analysis. Get means, outliers, distributions and examples'''
    lengths = []
    means = []
    for item in clicks:
        ones = [x for x in item if x == 1]
        means.append(len(ones) / len(item))
        lengths.append(len(item))

    plt.hist(lengths)
    plt.annotate('min = ' + str(min(lengths)), (100, 8.5))
    plt.axvline(stats.mean(lengths), ls='--', color='C1')
    plt.legend(['Mean = ' + str(round(stats.mean(lengths), 0))])
    plt.title('Number of Data Points per Article')
    plt.savefig('../figures/initial_data/click_len.png', dpi=300)

    print(len(lengths))

    labels = []
    for item in lab.keys():
        labels.append(item)
    high1, high2, high3, low1, low2, low3 = d.get_outliers(means, labels)

    #plot data for all documents
    plt.figure(figsize=(10, 4))
    plt.subplot(121)
    plt.hist(means)
    plt.axvline(stats.mean(means), ls='--', color='C01')
    plt.legend(['Mean = \n' + str(round(stats.mean(means), 4))])
    plt.xlabel("Percent Clicks")
    plt.ylabel("Number of Articles")
    plt.subplot(122)
    plt.boxplot(means)
    #outliers
    plt.annotate(str(high1), (.77, .097))
    plt.annotate(str(high2), (1.03, .096))
    plt.annotate(str(high3), (1.03, .09))
    plt.xticks([1], ['Box Plot of Click Percent'])
    plt.ylabel('Percent Clicks')
    plt.annotate(
        'Median = \n' + str(round(stats.median(means), 4)), (1.3, .0915),
        bbox=dict(boxstyle="round", fc="none", ec="#d3d3d3"))
    plt.suptitle('Click Bait Data (True)')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('../figures/initial_data/click_bait', dpi=300)
    plt.show()

    plt.scatter(lengths, means)
    
'''Function Call'''

#plot_data()
