
from itertools import compress

src_dst_list = []
base_path = '/Users/yansenxu/Documents/research/programs/rl-based-sfc-scaling/'
file_map = {}

def process_data(path, flow_file_path):
    count = 0
    with open(path, 'r') as trace_file:
        line = trace_file.readline()
        while line:
            count = count + 1
            l = get_compressed_info(line, [1, 1, 1, 1, 0, 1, 0])
            process_line(l, flow_file_path)
            line = trace_file.readline()
            if(count % 10000 == 0):
                print count
                # break

def get_compressed_info(line, listPosition):
    return map(remove_quotes, list(compress(line.split(','), listPosition)))

def process_line(line, flow_file_path):
    # src = getSrcIpFromLine(line)
    # dst = getDstIpFromLine(line)
    src = line[2]
    dst = line[3]
    n = src + '-' + dst
    if [src, dst] not in src_dst_list:
        src_dst_list.append([src, dst])
        file_map[n] = open(flow_file_path + n + '.csv', 'a')
    file_map[n].write(', '.join(line) + '\n')

def get_src_ip_from_line(line):
    return line[2]

def get_dst_ip_from_line(line):
    return line[3]

def remove_quotes(word):
    return word[1:-1]

def process(path, flow_file_path):
    process_data(path, flow_file_path)
    for key, item in file_map.items():
        item.close()
