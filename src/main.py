import matplotlib.pyplot as plt
import numpy as np
import time
import os
import path_config
from processing_capacity import processing_capacity


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
                traff_rate.append(sum_length/(time-base_time))
                packet_length.append(sum_length)
                base_time = time
                sum_length = 0
                t = t + 1
            else:
                sum_length = sum_length + length
            line = flow.readline()
    return time_slot, traff_rate, packet_length


def traffic_rate_data_test():
    [time_slot_1, traff_rate_1, packet_length_1] = traffic_rate_data('192.0.96.1-128.0.0.128.csv', 300)
    [time_slot_2, traff_rate_2, packet_length_2] = traffic_rate_data('1.0.0.2-128.0.0.2.csv', 10)
    time_slot_2 = [x * 10 for x in time_slot_2]
    # plt.plot(time_slot_1, traff_rate_1, 'r-', time_slot_2, traff_rate_2, 'b-')
    plt.plot(time_slot_1, traff_rate_1)
    plt.legend()
    plt.show()

def processing_capacity_test():
    capacity = processing_capacity(100, 200, 1024)
    print(capacity)


def main():
    # processing_capacity_test()
    traffic_rate_data_test()
    




if __name__ == '__main__':
    main()
