#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:55:27 2020

@author: sarafergus
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:04:53 2020
@author: sarafergus
"""
import random
import numpy
import statistics as stat


class arm():
    def __init__(self,
                 mab,
                 data=None,
                 faulty=False,
                 distribution=None):

        #set means based on data or theory
        if data != None:
            self.r_true = stat.mean(data)
        elif distribution == 'bernoulli':
            self.r_true = numpy.random.normal(0.0417, 0.02)
        elif distribution == 'normal':
            self.r_true = random.uniform(80, 100)
        elif distribution == 'normal_pres':
            self.r_true = random.uniform(8, 20)
            distribution = 'normal'
        elif distribution == 'exponential':
            self.r_true = -1
            while self.r_true < 0:
                self.r_true = numpy.random.normal(682.6163, 1097.1658)

        self.plays = []
        self.counted_plays = []
        self.r_est = 0
        self.best = False
        self.mab = mab
        self.faulty = faulty
        self.distribution = distribution
        self.data = data
        self.UCB_vals = []

    def get_random(self):
        '''return a random number according to a distribution. 
        Add reward to the mab's all_plays list. Used during gamble'''
        if self.faulty == True:
            p = random.random()
            if p > 0.99:
                num = random.uniform(-100, 100)
                self.mab.all_plays.append(num)
                return num
            else:
                pass
        if self.data != None:
            num = random.choice(self.data)
            self.mab.all_plays.append(num)
            return num
        elif self.distribution == 'normal':
            num = numpy.random.normal(self.r_true)
            self.mab.all_plays.append(num)
            return num
        elif self.distribution == 'exponential':
            num = -1
            while num < 0:
                num = numpy.random.exponential(self.r_true)
            self.mab.all_plays.append(num)
            return num
        elif self.distribution == 'bernoulli':
            p = random.random()
            if p > self.r_true:
                self.mab.all_plays.append(0)
                return 0
            else:
                self.mab.all_plays.append(1)
                return 1

    def play(self, update):
        '''Get random number, add to list of arm placec, update mean if requested'''
        val = self.get_random()
        self.plays.append(val)
        if update == True:
            self.counted_plays.append(val)
            self.r_est = sum(self.counted_plays) / len(self.counted_plays)

    def set_est(self, est):
        '''Setter for estimated mean'''
        self.r_est = est

    def set_best(self):
        '''Setter for best arm'''
        self.best = True
