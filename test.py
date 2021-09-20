import time
import sys

sys.stdout.write("10")
sys.stdout.flush()
sys.stdout.write("\b" * (10+1))
list = [x for x in range(pow(2, 16))]

part = pow(2, 16) / 10
out = []
prev_state = 0

for i in list:
    state = round(i/part)
    if state == prev_state + 1:
        out.append(state)
        prev_state = state
    print(out)


for i in range(pow(2, 16)):
    ip = 'localhost'
    potoc = threading.Thread(target=port_scanner, args=(ip, i))
    potoc.start()

# toolbar_width = 40
#
# # setup toolbar
# sys.stdout.write("[%s]" % (" " * toolbar_width))
# sys.stdout.flush()
# sys.stdout.write("\b" * (toolbar_width+1))  # return to start of line, after '['
#
# for i in range(toolbar_width):
#     time.sleep(0.1) # do real work here
#     # update the bar
#     sys.stdout.write("-")
#     sys.stdout.flush()
#
# sys.stdout.write("]\n") # this ends the progress bar
