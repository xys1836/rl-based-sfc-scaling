"""

"""
import numpy as np
import time
import sys
# import math
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

INTERVAL = 3
class Network(tk.Tk, object):
    def __init__(self, traffic_rate):
        super(Network, self).__init__()
        self.action_space = [0+k for k in range(0, 101)]
        self.n_actions = len(self.action_space)
        self.n_features = INTERVAL
        self._build_network(traffic_rate)
        self.count = 0
        self.traffic_rate = traffic_rate
        self.traffic_length = len(traffic_rate)

    def _build_network(self, traffic_rate):
        print self.action_space
        pass

    def reset(self):
        # return observation
        # return first 10 bit rate?
        self.count = 0
        return self.traffic_rate[0:INTERVAL]

    def step(self, action):
        # RL take action and get next observation and reward
        # observation_, reward, done = env.step(action)
        
        # return next bit rate with previous 9 bit rate, 
        # calculate reward according to loss function?
        # if no next bit rate, set done true?
        # print self.count


        done = False
        if self.count + INTERVAL >= self.traffic_length:
            done = True
            
            return [0]*INTERVAL, 0, done
        
        self.count += 1
        s_ = self.traffic_rate[self.count: self.count + INTERVAL]
        real_rate = self.traffic_rate[self.count + INTERVAL - 1]

        ep = 0
        mx = 100

        if -ep <= real_rate - action <= 0:
            reward = - (mx - (action - real_rate) * (mx/ep))
        if real_rate - action > 0:
            reward = - mx
        if real_rate - action < -ep:
            reward = - 0.5 * (action - real_rate - ep)


        # print 'reward: ', reward
        
        return s_, reward, done

    def render(self):
        # time.sleep(0.01)
        # self.update()
        # print self.count
        pass


