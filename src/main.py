import matplotlib.pyplot as plt
import numpy as np
import time
import preprecess_data
import os
import path_config

flow_file_path = path_config.flow_file_path

def main():
    x = []
    y = []

    with open(flow_file_path + '1.0.0.1-128.0.0.1.csv', 'r') as flow:
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
            if (time - base_time) >= 100:
                x.append(t)
                y.append(sum_length/(time-base_time))
                base_time = time
                sum_length = 0
                t = t + 1
            else:
                sum_length = sum_length + length

            line = flow.readline()

    plt.plot(x, y, label="traffic rate")

    plt.legend()

    plt.show()

if __name__ == '__main__':
    main()
