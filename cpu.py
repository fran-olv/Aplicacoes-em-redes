import psutil
import time
class CPUMonitor:
    def monitor_cpu(self):
        cpu_percentages = []
        start_time = time.time()
        while time.time() - start_time <= 60:
            cpu_percentages.append(psutil.cpu_percent(interval=1))
        return cpu_percentages

if __name__ == '__main__':
    MonitoraCPU = CPUMonitor()
    percentages = MonitoraCPU.monitor_cpu()
    print(percentages)
