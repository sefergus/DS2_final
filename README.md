The MAB project builds an adjustable multi-armed bandit that can make predictions using a number of algorithms, measures, and data sets or theoretical distributions. It is set up to run on four specific data sets. Created by Sara Fergus. Last Updated May 3, 2020.

# Data 
*data/by_date.csv* : by_date.csv contains U.S. national debt information including year, percent debt increase, and the party which had control of the white house in that year. From macrotrends.net.

*data/pres2.csv*: pres2.csv also contains U.S. national debt information. This file includes the year, the party which had control of the white house in that year, and the total national debt in dollars. This data set was adjusted within data.py to show percent increase. From U.S. Department of Treasury.

*data/univ-latencies.txt* : unit-latencies.txt includes universities (the first line) and trials (subsequent lines). Trials represent the time in milliseconds required to retrieve specific content. From Vermorel & Mohri, 2005. 

*SOMEWHERE wine data*
*SOMEWHERE Yahoo! Data*

# Data Reading
These files exist directly in the work directory

*data.py* : this file reads in four specific data sets and performs data cleaning. It also provides helper functions for data visualization. No changes necessary.

*click_bait.py* : Using tidy data from data.py, this gives a preliminary data analysis of the online advertising dataset. To see visualizations, uncomment the last line that calls the plotting function.

*presidents_data.py* : Using tidy data from data.py, this gives a preliminary data analysis of the national debt datasets. To see visualizations, uncomment the last line that calls the plotting function.

*wine_data.py* : Using tidy data from data.py, this gives a preliminary data analysis of the wine ratings dataset. To see visualizations, uncomment the last line that calls the plotting function.

*network_data.py* : Using tidy data from data.py, this gives a preliminary data analysis of the content distribution network dataset. To see visualizations, uncomment the last line that calls the plotting function.

# MAB Creation
*MAB.py* : the MAB class creates an MAB object. This stores information about a specific instance of a multiarmed bandit including: the bandit’s arms, characteristics of the bandit (e.g. whether it is “faulty”), the number of gambles to be run on it and the number of plays per gamble, all plays on that MAB in a particular gamble, and the data set or distribution that the MAB is based on. Methods include reseting the arms of the MAB between gambles and gamble() which calls a particular algorithm x times, where x is the number of gambles being tested. To change the measures included, add to the gamble loop measures included in measures.py.

*arm_class.py* : the arm class creates arm objects which are included in an MAB. Arms hold information like the MAB instance it is a part of, the data or distribution from which the arm pulls, whether any faulty information will be returned, a true and estimated mean, a list of rewards earned in a particular gamble, whether it is the best arm of an MAB, and a list of upper confidence bounds. Methods allow the arms to return a random value based on its data or distribution, append the reward to a list of plays and update the estimated mean. There are also setters for the estimated mean and whether it is the best arm. No changes necessary. 

# Gambling
*measures.py* : measures.py contains functions which calculate external regret, internal regret, the optimal pull percentage, the cumulative reward, and the average reward. Requires an MAB instance to calculate measures. No changes necessary. 

*algorithms.py* : algorithms.py contains functions which take one “pull” of an MAB, including random, greedy, epsilon-first, epsilon-greedy, UCB1, and elimination. Helper functions determine the best arm based on various measures (not the true best arm), or determine how long the epsilon-methods exploration will last. No changes necessary.

*gamble.py* : gamble.py gambles on the MAB and plots the results. It has 8 pre-set gambles, corresponding with the theoretical and data-driven versions of the pre-set data sets. Most changes will be in the map_stratgey() function, where it calls one_strategy(). In one strategy, a hard - coded change in the first parameter will change the number of gambles, the second changes the initial number of pulls (before increasing), and  the third the number of arms. Initialization of the greedy algorithm can be changed in the function calls, as the first parameter of choose_trial().

# Sources

Li, L., Chu, W., Langford, J., \& Wang, X. (2011). Unbiased offline evaluation of contextual-bandit-based news article recommendation algorithms. Proceedings of the Fourth ACM International Conference on Web Search and Data Mining - WSDM 11. doi: 10.1145/1935826.1935878

macrotrends.net (2019, December). National Debt By President. Macrotrends.net. Retrieved from https:// www.macrotrends.net/2023/national-debt-by-president.

Thoutt, Z. (2018). Wine Reviews, Version 4. Retrieved from https://www.kaggle.com/zynicide/wine-reviews.

US Department of the Treasury. (2019). Public Debt of the United States from 1990 to 2019. Treasury.gov. Retrieved from https://www.statista.com/statistics/187867/public-debt-of-the-united-states-since-1990/

Vermorel J., Mohri M. (2005) Multi-armed Bandit Algorithms and Empirical Evaluation. In: Gama J., Camacho R., Brazdil P.B., Jorge A.M., Torgo L. (eds) Machine Learning: ECML 2005. ECML 2005. Lecture Notes in Computer Science, vol 3720. Springer, Berlin, Heidelberg

