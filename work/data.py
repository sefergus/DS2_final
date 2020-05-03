#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:35:54 2020

@author: sarafergus
"""
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics as stats
import os


def load_wine_data():
    '''Read in wine data. Create list of countries who have more than 1000
    observations, and the corresponding scores of those observations'''

    countries = {}
    with open('../data/winemag-data_first150k.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            break  #header
        for row in reader:
            if row[1] not in countries and row[1] != '' and row[1] != 'US-France':
                countries[row[1]] = [int(row[4])]
            elif row[1] != '' and row[1] != 'US-France':
                countries[row[1]].append(int(row[4]))

    #throw out countries with less than 1000 observations
    final_countries = {}
    for item in countries.keys():
        if len(countries[item]) > 1000:
            final_countries[item] = countries[item]

    final_countries_list = []
    for item in final_countries.keys():
        final_countries_list.append(final_countries[item])
    return final_countries_list, final_countries


def load_president_data():
    '''maximize (maximum - item) in order to minimize nat'l debt increase. 
    Return lists of years for each party and corresponding list of data. Data
    is the distance from the all time maximum debt increase'''
    democrat = []
    republican = []
    dem_years = []
    rep_years = []
    #first data set
    with open('../data/by_date.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            break
        for row in reader:
            if row[2] == 'Democratic':
                democrat.append(float(row[3]))
                dem_years.append(int(row[0]))
            elif row[2] == 'Republican':
                republican.append(float(row[3]))
                rep_years.append(int(row[0]))

    #second data set
    with open('../data/pres2.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            prev = float(row[1].replace(',', ''))
            break
        for row in reader:
            if row[2] == 'Democrat':
                percent = float(row[1].replace(',', '')) / prev
                prev = float(row[1].replace(',', ''))
                if int(row[0]) in dem_years:
                    loc = dem_years.index(int(row[0]))
                    democrat[loc] = (democrat[loc] + percent) / 2
                else:
                    dem_years.append(int(row[0]))
                    democrat.append(percent)
            elif row[2] == 'Republican':
                percent = float(row[1].replace(',', '')) / prev
                prev = float(row[1].replace(',', ''))
                if int(row[0]) in rep_years:
                    loc = rep_years.index(int(row[0]))
                    republican[loc] = (republican[loc] + percent) / 2
                else:
                    rep_years.append(int(row[0]))
                    republican.append(percent)

    #determine maximum in order to minimize debt increase
    all_percents = democrat + republican
    maximum = max(all_percents)
    dem = [maximum - x for x in democrat]
    rep = [maximum - x for x in republican]

    return democrat, republican, dem_years, rep_years, dem, rep


def load_university_data():
    '''maximize (maximum - item) in order to minimize time.
    Returns list of lists, each list is data for one
    website'''
    lists = []
    labs = []
    with open('../data/univ-latencies.txt') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for i in range(len(row)):
                lists.append([])
                labs.append(row[i])
            break
        for row in reader:
            for i in range(len(row)):
                lists[i].append(int(row[i]))

    #determine maximum to minimize
    maximum = 0
    means = []
    for l in lists:
        m = max(l)
        if m > maximum:
            maximum = m
    for item in lists:
        item = [maximum - i for i in item]
        means.append(stats.mean(item))

    #print(stats.mean(means))
    return lists, labs


def load_click_data():
    '''Load click bait data. Return list of articles and their corresponding
    click data'''
    clicks = {}
    final_clicks = []
    for item in os.listdir('../data/click_bait'):
        with open('../data/click_bait/' + item) as csvfile:
            reader = csv.reader(csvfile, delimiter='|')
            for row in reader:
                row_list = row[0].split()
                if row_list[1] not in clicks.keys():
                    clicks[row_list[1]] = [int(row_list[2])]
                else:
                    clicks[row_list[1]].append(int(row_list[2]))
            break
    for item in list(clicks.values()):
        final_clicks.append(item)
    return final_clicks, clicks


def get_outliers(lists, labels):
    '''Used in initial data analysis. Determine outliers of data set'''
    high1 = labels[lists.index(max(lists))]
    new_list = list(lists)
    new_list2 = list(labels)
    new_list.remove(max(lists))
    new_list2.remove(high1)
    high2 = new_list2[new_list.index(max(new_list))]

    new_list3 = new_list
    new_list4 = new_list2
    new_list3.remove(max(new_list))
    new_list4.remove(high2)
    high3 = new_list4[new_list3.index(max(new_list3))]

    low1 = labels[lists.index(min(lists))]
    lnew_list = list(lists)
    lnew_list2 = list(labels)
    lnew_list.remove(min(lists))
    lnew_list2.remove(low1)
    low2 = lnew_list2[lnew_list.index(min(lnew_list))]

    lnew_list3 = lnew_list
    lnew_list4 = lnew_list2
    lnew_list3.remove(min(lnew_list))
    lnew_list4.remove(low2)
    low3 = lnew_list4[lnew_list3.index(min(lnew_list3))]

    return high1, high2, high3, low1, low2, low3


def ccdf(data, title):
    '''plot CCDF'''
    X = sorted(data)
    N = len(data)
    Y = 1.0 * np.arange(N) / N

    Y = 1 - 1.0 * np.arange(N) / N  # CCDF
    plt.plot(X, Y, '.', markersize=8)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Log of Latency')
    plt.ylabel("Log $P_>(x)$")
    plt.title("CCDF - " + title)


#    plt.show()
