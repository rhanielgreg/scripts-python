import os
import signal
import time
import subprocess

def get_cpu_temperature():
    output = subprocess.check_output(["sensors"])
    output = output.decode("utf-8")
def monitor_temperature():
    lines = output.split("\n")
    for line in lines:
        if "Core" in line:
            parts = line.split(":")
            temperature = float(parts[1].split()[0])
            return temperature
    return None

def close_chrome():
    try:
        chrome_pid = subprocess.check_output(["pgrep", "chrome"]).decode().strip()
        if chrome_pid:
            os.kill(int(chrome_pid), signal.SIGTERM)
    except subprocess.CalledProcessError:
        pass

if __name__ == "__main__":
    while True:
        temperature = monitor_temperature()
        time.sleep(1)
        if temperature is not None and temperature > 85:
            close_chrome()
        # Aguarda 1 segundo antes de verificar a temperatura novamente
        time.sleep(1)