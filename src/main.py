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
    plt.plot(time_slot_1, traff_rate_1)
    plt.legend()
    plt.title(file_name)
    plt.show()

def draw_rate_date(file_name, interval):
    [time_slot, traff_rate, packet_length] = traffic_rate_data(file_name, interval)
    traff_rate = np.array(traff_rate)
    traff_rate = (traff_rate - traff_rate.min()) / (traff_rate.max() - traff_rate.min())
    plt.plot(time_slot, traff_rate)
    plt.title(file_name)
    # plt.legend()
    plt.show()

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
    




if __name__ == '__main__':
    main()
