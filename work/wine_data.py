#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:50:03 2020

@author: sarafergus
"""

import data as d
import matplotlib.pyplot as plt
import statistics as stats

countries, final = d.load_wine_data()


def plot_data():

    #plot countries boxplots
    plt.boxplot(countries)
    plt.title('Wine Rating by Country')
    plt.xticks(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        list(final.keys()),
        rotation=90)
    plt.savefig(
        '../figures/initial_data/wine4',
        dpi=300,
        bbox_inches='tight',
        pad_inches=0.5)
    '''plot info for all ratings'''
    plt.figure(figsize=(12, 4))
    plt.suptitle('All Ratings (True)')
    plt.subplot(121)
    all_ratings = []
    for item in final.values():
        all_ratings = all_ratings + item
    plt.hist(all_ratings)
    plt.axvline(stats.mean(all_ratings), ls='--', color='C1')
    plt.legend(['Mean = ' + str(round(stats.mean(all_ratings), 2))])
    plt.subplot(122)
    plt.boxplot(all_ratings)
    plt.annotate(
        'Scores of 100: \n US : 10 \n France : 4 \n Italy : 7 \n Australia : 3',
        (0.7, 95))
    plt.annotate(
        'Median = ' + str(round(stats.median(all_ratings), 4)), (1.25, 99),
        bbox=dict(boxstyle="round", fc="none", ec="#d3d3d3"))
    plt.savefig('../figures/initial_data/wine3', dpi=300)

    #plot all distributions
    plt.figure(figsize=(11, 6.5))
    plt.suptitle('Wine Rating Distributions (True)')
    plt.tight_layout()
    plt.subplot(231)
    plt.title('Austria')
    plt.hist(final['Austria'], alpha=0.5, density=True)
    plt.axvline(stats.mean(final['Austria']), color='black', ls='--')
    plt.yticks([], [''])
    plt.legend(['Mean:\n' + str(round(stats.mean(final['Austria']), 2))])
    plt.subplot(232)
    plt.title('Germany')
    plt.hist(final['Germany'], alpha=0.5, density=True, color='C1')
    plt.axvline(stats.mean(final['Germany']), color='black', ls='--')
    plt.legend(['Mean:\n' + str(round(stats.mean(final['Germany']), 2))])
    plt.yticks([], [''])
    plt.subplot(233)
    plt.title('France')
    plt.hist(final['France'], alpha=0.5, density=True, color='C2')
    plt.axvline(stats.mean(final['France']), color='black', ls='--')
    plt.legend(['Mean:\n' + str(round(stats.mean(final['France']), 2))])
    plt.yticks([], [''])
    plt.subplot(234)
    plt.title('Italy')
    plt.hist(final['Italy'], alpha=0.5, density=True, color='C3')
    plt.axvline(stats.mean(final['Italy']), color='black', ls='--')
    plt.legend(['Mean:\n' + str(round(stats.mean(final['Italy']), 2))])
    plt.yticks([], [''])
    plt.subplot(235)
    plt.title('Portugal')
    plt.hist(final['Portugal'], alpha=0.5, density=True, color='C4')
    plt.axvline(stats.mean(final['Portugal']), color='black', ls='--')
    plt.legend(['Mean:\n' + str(round(stats.mean(final['Portugal']), 2))])
    plt.yticks([], [''])
    plt.subplot(236)
    plt.title('Australia')
    plt.hist(final['Australia'], alpha=0.5, density=True, color='C5')
    plt.axvline(stats.mean(final['Australia']), color='black', ls='--')
    plt.legend(['Mean:\n' + str(round(stats.mean(final['Australia']), 2))])
    plt.yticks([], [''])
    plt.savefig('../figures/initial_data/wine1', dpi=300)

    plt.figure(figsize=(11, 6.5))
    plt.suptitle('Wine Rating Distributions (True)')
    plt.tight_layout()
    plt.subplot(231)
    plt.title('US')
    plt.hist(final['US'], alpha=0.5, density=True, color='C6')
    plt.axvline(stats.mean(final['US']), color='black', ls='--')
    plt.legend(['Mean:\n' + str(round(stats.mean(final['US']), 2))])
    plt.yticks([], [''])
    plt.subplot(232)
    plt.title('New Zealand')
    plt.hist(final['New Zealand'], alpha=0.5, density=True, color='C7')
    plt.axvline(stats.mean(final['New Zealand']), color='black', ls='--')
    plt.legend(['Mean:\n' + str(round(stats.mean(final['New Zealand']), 2))])
    plt.yticks([], [''])
    plt.subplot(233)
    plt.title('South Africa')
    plt.hist(final['South Africa'], alpha=0.5, density=True, color='C8')
    plt.axvline(stats.mean(final['South Africa']), color='black', ls='--')
    plt.legend(['Mean:\n' + str(round(stats.mean(final['South Africa']), 2))])
    plt.yticks([], [''])
    plt.subplot(234)
    plt.title('Spain')
    plt.hist(final['Spain'], alpha=0.5, density=True, color='C9')
    plt.axvline(stats.mean(final['Spain']), color='black', ls='--')
    plt.legend(['Mean:\n' + str(round(stats.mean(final['Spain']), 2))])
    plt.yticks([], [''])
    plt.subplot(235)
    plt.title('Chile')
    plt.hist(final['Chile'], alpha=0.5, density=True, color='C10')
    plt.axvline(stats.mean(final['Chile']), color='black', ls='--')
    plt.legend(['Mean:\n' + str(round(stats.mean(final['Chile']), 2))])
    plt.yticks([], [''])
    plt.subplot(236)
    plt.title('Argentina')
    plt.hist(final['Argentina'], alpha=0.5, density=True, color='C11')
    plt.axvline(stats.mean(final['Argentina']), color='black', ls='--')
    plt.legend(['Mean:\n' + str(round(stats.mean(final['Argentina']), 2))])
    plt.yticks([], [''])
    plt.savefig('../figures/initial_data/wine2', dpi=300)
    plt.show()

    #determine countries with 100-point bottles
    best = []
    for i in range(len(all_ratings)):
        if all_ratings[i] == 100:
            best.append(i)

    ranges = {}
    total = 0
    for key, value in final.items():
        ranges[key] = list(range(total, total + len(value)))
        total += len(value)

    #means
    lengths = []
    means = []
    for item in countries:
        means.append(stats.mean(item))
        lengths.append(len(item))
    #
    plt.hist(means)
    plt.title('Distribution of Arm Means')
    plt.xlabel('Mean Rating')
    plt.tight_layout()
    plt.savefig('../figures/initial_data/wine_means_hist', dpi=300)

    plt.show()

    plt.boxplot(means)
    plt.show()

    plt.title('Number of Data Points by Country')
    plt.plot(lengths, 'o')
    plt.xticks(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        list(final.keys()),
        rotation=90)
    plt.hlines(
        stats.mean(lengths), xmin=0, xmax=12, linestyles='dashed', colors='C0')
    plt.legend(['Mean = ' + str(int(round(stats.mean(lengths), 0)))])
    plt.annotate('2237', (8.3, plt.xlim()[0]))
    plt.savefig(
        '../figures/initial_data/wine_len',
        dpi=300,
        bbox_inches='tight',
        pad_inches=0.5)

    print(list(final.keys()))
    print(lengths)


'''Function Call'''
#plot_data()
