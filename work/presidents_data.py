#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:55:19 2020

@author: sarafergus
"""

import data as d
import matplotlib.pyplot as plt
import statistics as stats

''' COLLECT DATA ''' 


''' presidents ''' 

democrat, republican, dem_y, rep_y, dem, rep = d.load_president_data()

print('lengths: ', len(democrat), len(republican))

plt.figure(figsize=(12, 4))  
plt.subplot(121)
plt.hist(republican, alpha = 0.5, color = 'C3')
plt.hist(democrat, alpha  = 0.5, color = 'C0')
presidents = [democrat, republican]
plt.axvline(stats.mean(democrat), ls = '--', color = 'C0')
plt.axvline(stats.mean(republican), ls = '--', color = 'C3')
plt.legend(['Democrat \nMean= '  + str(round(stats.mean(democrat),2)), 
            'Republican \nMean='  + str(round(stats.mean(republican),2))])
plt.suptitle('Increase in National Debt by President\'s Party (True)')
plt.ylabel('Number of Years')
plt.xlabel('Debt Increase (Percent)')
plt.subplot(122)
plt.boxplot([democrat,republican])
plt.xticks([1,2], ['Democrat','Republican'])
plt.ylabel('Debt Increase (Percent)')
plt.annotate('Democrat\n Median = ' + str(round(stats.median(democrat),4)) + '\n\n Republican\n Median = ' + str(round(stats.median(republican),4)),
             (1.25,15),bbox=dict(boxstyle="round", fc="none", ec="#d3d3d3"))
h1, h2, h3, l1, l2, l3 = d.get_outliers(democrat, dem_y)
plt.annotate(h1, (.85, 12.4))
plt.show()
# plt.savefig('../figures/initial_data/pres', dpi=300)