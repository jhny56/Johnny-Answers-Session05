import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/robot/Desktop/Session05/Johnny-Answers-Session05/install/temperature_monitor'
