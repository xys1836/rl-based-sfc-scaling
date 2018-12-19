
path = 'C:\Users\Yansen XU\Documents\programs\skype_trace\skype_e2e_trace'
import matplotlib.pyplot as plt
# "No.","Time","Source","Destination","Protocol","Length","Info"

src_ip_list = []
def test():
    with open(path, 'r') as trace_file:
        line = trace_file.readline()
        print line
        while line:
            line = trace_file.readline()
            # print float(line.split(',')[2][1:-1])
            src_ip = line.split(',')[2][1:-1]
            if src_ip not in src_ip_list:
                src_ip_list.append(src_ip)
                print src_ip






def main():
    test()




if __name__ == '__main__':
    main()