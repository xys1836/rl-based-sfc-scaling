# import matplotlib.pyplot as plt
import numpy as np
import time
import os
import path_config
from processing_capacity import processing_capacity
from dqn.network_env import Network
# from dqn.RL_brain import DeepQNetwork
from dqn.DQN_modified import DeepQNetwork
from numpy.random import *
import numpy as np
import math

flow_file_path = path_config.flow_file_path


def traffic_rate_data(file_name, interval=1):
    """Read traffic data and calculate traffic rate in interval.
    """
    time_slot = []
    traff_rate = []
    packet_length = []
    with open(flow_file_path + file_name, 'r') as flow:
        line = flow.readline()
        l = line.split(',')
        count = 0
        base_time = float(l[1])
        sum_length = 0
        t = 0
        while line:
            count = count + 1
            l = line.split(',')
            time = float(l[1])
            length = int(l[4])
            if (time - base_time) >= interval:
                time_slot.append(t)
                traff_rate.append(sum_length/(time-base_time)*8)
                packet_length.append(sum_length)
                base_time = time
                sum_length = 0
                t = t + 1
            else:
                sum_length = sum_length + length
            line = flow.readline()
    return time_slot, traff_rate, packet_length



def traffic_rate_data_test(file_name, interval):
    [time_slot_1, traff_rate_1, packet_length_1] = traffic_rate_data(file_name, interval)
    #[time_slot_2, traff_rate_2, packet_length_2] = traffic_rate_data('1.0.0.2-128.0.0.2.csv', 10)
    #time_slot_2 = [x * 10 for x in time_slot_2]
    # plt.plot(time_slot_1, traff_rate_1, 'r-', time_slot_2, traff_rate_2, 'b-')

    traff_rate_1 = np.array(traff_rate_1)
    traff_rate_1 = (traff_rate_1 - traff_rate_1.min()) / (traff_rate_1.max() - traff_rate_1.min())
    # plt.plot(time_slot_1, traff_rate_1)
    # plt.legend()
    # plt.title(file_name)
    # plt.show()

def draw_rate_date(file_name, interval):
    [time_slot, traff_rate, packet_length] = traffic_rate_data(file_name, interval)
    traff_rate = np.array(traff_rate)
    traff_rate = (traff_rate - traff_rate.min()) / (traff_rate.max() - traff_rate.min())
    # plt.plot(time_slot, traff_rate)
    # plt.title(file_name)
    # # plt.legend()
    # plt.show()

def test():
    for file in files(flow_file_path):
        print(file)
        draw_rate_date(file, 1)


def files(directory):
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            yield file


def processing_capacity_test():
    capacity = processing_capacity(100, 200, 1024)
    print(capacity)


def main():
    # # processing_capacity_test()
    file_name = '1.0.0.6-128.0.0.1.csv'
    # file_name = '1.0.0.1-128.0.0.1.csv'
    # # file_name = '128.0.0.1-1.0.0.6.csv'
    # # file_name = '4.0.0.10-128.0.0.2.csv'
    # file_name = '4.0.0.10-128.0.0.2.csv'
    traffic_rate_data_test(file_name, 1)
    # test()
    





#######################################





action_sets = []
actions = [0, 0]
action_set  = [0, 0]
action_test = [0, 0]
def run_network(traffic_rate_test):
    global actions
    global action_test
    count = 0
    step = 0
    for episode in range(10):
        count += 1
        print count
        # initial observation
        observation = env.reset()
        
        action_set  = [0, 0]
        actions = [0, 0]
        while True:
            # fresh env
            env.render()
            # RL choose action based on observation
            action = RL.choose_action(observation)
            action_set.append(action)
            actions.append(action)
            # print "action: ", action
            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)
            RL.store_transition(observation, action, reward, observation_)
            if (step > 200) :#and (step % 5 == 0):
                RL.learn()
            # swap observation
            observation = observation_
            # break while loop when end of this episode
            if done:
                break
            step += 1
        action_sets.append(action_set)
    

    env_test = Network(np.array(traffic_rate_test))
    action_test = [0, 0]
    observation = env_test.reset()
    while True:
            # fresh env
            env_test.render()
            # RL choose action based on observation
            action = RL.choose_action_from_nn(observation)
            # action_set.append(action)
            action_test.append(action)
            # print "action: ", action
            # RL take action and get next observation and reward
            observation_, reward, done = env_test.step(action)
            # RL.store_transition(observation, action, reward, observation_)
            # if (step > 200) and (step % 5 == 0):
            #     RL.learn()
            # swap observation
            observation = observation_
            # break while loop when end of this episode


            if done:
                break
            step += 1









    # end of game
    print('game over')
    env.destroy()
    env_test.destroy()


if __name__ == '__main__':
    # global actions
    file_name = '1.0.0.6-128.0.0.1.csv'
    file_name_test = '1.0.0.1-128.0.0.1.csv'
    # file_name_test = '1.0.0.6-128.0.0.1.csv'
    # file_name = '1.0.0.1-128.0.0.1.csv'
    interval = 90
    [time_slot, traffic_rate, packet_length] = traffic_rate_data(file_name, interval)
    traffic_rate = np.array(traffic_rate)
    traffic_rate = traffic_rate/10000

    [time_slot_test, traffic_rate_test, packet_length_test] = traffic_rate_data(file_name_test, interval)
    traffic_rate_test = np.array(traffic_rate_test)
    traffic_rate_test = traffic_rate_test/10000

    # traffic_rate = (traffic_rate - traffic_rate.min()) / (traffic_rate.max() - traffic_rate.min())
    # traffic_rate = traffic_rate * 100
    # traffic_rate_test = (traffic_rate_test - traffic_rate_test.min()) / (traffic_rate_test.max() - traffic_rate_test.min())
    # traffic_rate_test = traffic_rate_test * 100
    # traffic_rate = np.floor(traffic_rate)
    # plt.plot(np.arange(len(traffic_rate)), traffic_rate)
    # plt.title(file_name)
    # plt.show()


    # traffic_rate = []
    # for i in range(0, 3000):
    #     traffic_rate.append(rand())

    # traffic_rate = traffic_rate[15:131]
    env = Network(np.array(traffic_rate))
    RL = DeepQNetwork(env.action_space, env.n_actions, env.n_features,
                      learning_rate=0.005,
                      reward_decay=0.9,
                      e_greedy=0.95,
                      replace_target_iter=200,
                      memory_size=500000,
                      output_graph=True
                      )
    env.after(100, run_network(traffic_rate_test))
    env.mainloop()
    RL.plot_cost()
    actions = np.array(actions)
    RL.plot(traffic_rate)
    RL.plot2(traffic_rate, actions, 'flow 1')
    RL.plot2(traffic_rate_test, action_test, 'flow 2')
    RL.plot(actions - traffic_rate)
    RL.plot(action_test - traffic_rate_test)

    RL.plot3(action_sets, traffic_rate)

    # RL.plot(traffic_rate)
    # RL.plot(action_set)
    # plt.plot(action_set)
    # plt.show()