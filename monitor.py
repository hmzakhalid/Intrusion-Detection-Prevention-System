import os
import time
import psutil


def monitor_network_connections(interval=5, log_file="./logs/network_connections_log.txt"):
    previous_connections = set()

    while True:
        current_connections = set()
        for connection in psutil.net_connections(kind="inet"):
            laddr = connection.laddr
            raddr = connection.raddr
            status = connection.status
            if raddr:
                current_connections.add((laddr, raddr, status))

        new_connections = current_connections - previous_connections
        for connection in new_connections:
            laddr, raddr, status = connection
            with open(log_file, "a") as f:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
                f.write(f"{timestamp} - {laddr} -> {raddr} - {status}\n")

        previous_connections = current_connections
        time.sleep(interval)



def monitor_system_processes(interval=60, cpu_threshold=80, mem_threshold=80, log_file="./logs/processes_log.txt"):
    while True:
        for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
            pid = process.info["pid"]
            name = process.info["name"]
            cpu_percent = process.info["cpu_percent"]
            mem_percent = process.info["memory_percent"]

            if cpu_percent > cpu_threshold or mem_percent > mem_threshold:
                with open(log_file, "a") as f:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
                    f.write(f"{timestamp} - {name} (PID: {pid}) - CPU: {cpu_percent}%, MEM: {mem_percent}%\n")

        time.sleep(interval)