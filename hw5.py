import numpy as np
import scr.SamplePathClass as PathCls
import scr.StatisticalClasses as Stat
import scr.FigureSupport as Fig


class Game(object):
    def __init__(self,id, prob_head):
        self._id=id
        self._rnd=np.random
        self._rnd.seed(id)
        self._probHead = prob_head
        self._countWins=0

    def simulate(self, n_of_flips):
        count_tails=0
        for i in range(n_of_flips):

            if self._rnd.random_sample() < self._probHead:
                if count_tails>=2:
                    self._countWins+=1
                count_tails=0
            else:
                count_tails +=1
    def get_reward(self):
        return 100*self._countWins-250


class SetOfGames:
    def __init__(self, prob_head, n_games):
        self._gameRewards = []

        for n in range(n_games):
            game=Game(id=n, prob_head=prob_head)
            game.simulate(20)
            self._gameRewards.append(game.get_reward())
    def get_ave_reward(self):
        return sum(self._gameRewards) / len(self._gameRewards)

    #min reward
    def min(self):
        return min(self._gameRewards)
    #max reward
    def max(self):
        return max(self._gameRewards)

    #prob that you lose money in the games
    def prob_loss(self, total_games):
        loss=0
        for i in self._gameRewards:
            if i<250:
                loss+=1
        return loss/total_games

    def count_rewards(self):
        return self._gameRewards


games = SetOfGames(prob_head=0.5, n_games=1000)

Fig.graph_histogram\
    (observations=games.count_rewards(),
    title='Histogram of Rewards',
    x_label='Rewards',
    y_label='Frequency')

print('Minimum Expected reward is:', games.min())
print('Maximum Expected reward is:', games.max())

#problem2
print('The probability of loosing is:', games.prob_loss(1000))



