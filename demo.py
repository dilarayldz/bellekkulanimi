import matplotlib.pyplot as plt
import psutil
import time

def plot_memory_usage():
    # Başlangıç zamanı
    start_time = time.time()
    
    # Bellek kullanımı ve zamanı depolamak için boş listeler oluşturun
    memory_usage = []
    timestamps = []

    # Bellek kullanımını izlemek için bir döngü oluşturun
    while True:
        # Mevcut bellek kullanımını al
        mem = psutil.virtual_memory()
        # Toplam bellek kullanımını MB cinsinden alıp listeye ekleyin
        memory_usage.append(mem.used / 1024 / 1024)
        # Geçen zamanı alıp listeye ekleyin
        timestamps.append(time.time() - start_time)
        
        # Grafik çizimi
        plt.plot(timestamps, memory_usage, color='blue')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Memory Usage (MB)')
        plt.title('Memory Usage Over Time')
        plt.grid(True)
        plt.pause(1)

try:
    plot_memory_usage()
except KeyboardInterrupt:
    plt.close()
    print("Demo sonlandırıldı.")