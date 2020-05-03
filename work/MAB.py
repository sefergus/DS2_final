from arm_class import arm
import measures as m


class mab:
    def __init__(self,
                 num,
                 gambles=100,
                 plays=100,
                 epsilon=0.5,
                 est=True,
                 data=None,
                 dist=None,
                 faulty=False):
        self.arms = []
        self.all_plays = []
        self.data = data
        self.faulty = faulty
        for i in range(num):
            if data != None:
                self.arms.append(arm(self, data=data[i], faulty=self.faulty))
            else:
                self.arms.append(
                    arm(self, distribution=dist, faulty=self.faulty))
        self.est = est
        self.epsilon = epsilon
        self.plays = plays
        self.gambles = gambles
        self.distribution = dist

    def reset(self):
        '''resets arms in mab between gambles'''
        for item in self.arms:
            data = item.data
            distribution = item.distribution
            item.__init__(
                self, data, distribution=distribution, faulty=self.faulty)

    def gamble(self, algorithm):
        '''
        Gamble Loop
        @params: algorithm function, number of gambles, number of plays
                 per gamble, list of arms, epsilon value(various meanings), 
                 difficulty setting
        @return: lists regret and optimal percent values from each gamble
        '''
        regret_list = []
        total_plays = []
        optimal_list = []
        reward_list = []
        average_reward = []
        for i in range(self.gambles):
            self.reset()
            algorithm(self)
            regret_list.append(m.regret(self, self.plays))
            optimal_list.append(m.optimal(self, self.plays))
            reward_list.append(m.cum_reward(self))
            average_reward.append(m.average_reward(self, self.plays))
            total_plays.append(self.all_plays)
            self.all_plays = []
        return regret_list, optimal_list, reward_list, average_reward, total_plays
