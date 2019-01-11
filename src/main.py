
# path = 'C:\Users\Yansen XU\Documents\programs\skype_trace\skype_e2e_trace.csv'

import matplotlib.pyplot as plt
import numpy as np
import time
import preprecess_data


data_file_path = '/Users/yansenxu/Documents/research/programs/skypetrace/skype_e2e_trace.csv'
# "No.","Time","Source","Destination","Protocol","Length","Info"
flow_files_path = '/Users/yansenxu/Documents/research/programs/rl-based-sfc-scaling/flow_data/'

def main():
    # x = np.linspace(0, 10, 100)
    # y = x + np.random.randn(100) 
    x = []
    y = []

    with open(flow_files_path + '1.0.0.6-128.0.0.1.csv', 'r') as flow:
        line = flow.readline()
        l = line.split(',')
        count = 0
        base_time = float(l[1])
        sum_length = 0
        max_length = 0
        t = 0
        while line:
            count = count + 1
            l = line.split(',')
            time = float(l[1])
            length = int(l[4])
            if (time - base_time) >= 100:
                x.append(t)
                y.append(sum_length/(time-base_time))
                base_time = time
                sum_length = 0
                t = t + 1
            else:
                sum_length = sum_length + length

            line = flow.readline()
    #         print count 
            
    # print x
    # print y

    plt.plot(x, y, label="test")

    plt.legend()

    plt.show()

if __name__ == '__main__':
    main()
