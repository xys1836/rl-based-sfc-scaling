import matplotlib.pyplot as plt
import numpy as np
import time
import preprecess_data
import os
import path_config

flow_file_path = path_config.flow_file_path


def traffic_rate_data(file_name, interval=1):
    """Read traffic data and calculate traffic rate in interval.
    """
    x = []
    y = []
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
                x.append(t)
                y.append(sum_length/(time-base_time))
                base_time = time
                sum_length = 0
                t = t + 1
            else:
                sum_length = sum_length + length
            line = flow.readline()
    return x, y


def main():
    [x1, y1] = traffic_rate_data('1.0.0.2-128.0.0.2.csv', 1)
    [x2, y2] = traffic_rate_data('1.0.0.2-128.0.0.2.csv', 10)
    x2 = [x * 10 for x in x2]
    plt.plot(x1, y1, 'r-', x2, y2, 'b-')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
