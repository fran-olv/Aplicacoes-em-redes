import psutil
import time

def monitor_memory():
    memory_percentages = []
    start_time = time.time()
    while time.time() - start_time <= 60:
        memory_percentages.append(psutil.virtual_memory().percent)
        time.sleep(1)
    return memory_percentages

if __name__ == '__main__':
    MonitoraCPU = CPUMonitor()
    percentages = MonitoraCPU.monitor_cpu()
    print(percentages)