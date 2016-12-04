import subprocess

def getlastline():
    with open('<name_of_log_file') as f:
      last = None
      for last in (line for line in f if line.rstrip('\n')):
        pass

    return last

def nth_line(text, n):
    return text.split()[n]

print getlastline()

while True:
    status = str(nth_line(getlastline(), 3))
    if '0' in status:
        subprocess.call('curl -i http://192.168.1.93:6005/user/0', shell=True)
    elif '1' in status:
        subprocess.call('curl -i http://192.168.1.93:6005/user/1', shell=True)
    else:
        pass
