import re
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f} sec")
        return result
    return wrapper



def read_logs(file):
    with open(file, 'r') as f:
        for line in f:
            yield line.strip()



def error_counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner


# Iterator → custom iterable class
class LogIterator:
    def __init__(self, logs):
        self.logs = logs
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.logs):
            raise StopIteration
        value = self.logs[self.index]
        self.index += 1
        return value


@timer
def analyze_logs(file):
    logs = []

   
    for line in read_logs(file):
        logs.append(line)

    
    log_iter = LogIterator(logs)

    
    count_error = error_counter()

    
    pattern = r'ERROR: (.*)'

    for log in log_iter:
        match = re.search(pattern, log)
        if match:
            print("Error Found:", match.group(1))
            print("Error Count:", count_error())



analyze_logs("log.txt")
