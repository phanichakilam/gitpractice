import platform
import psutil
import socket

def get_system_info():
    info = []
    info.append("===== System Information =====")
    info.append(f"System: {platform.system()}")
    info.append(f"Node Name: {platform.node()}")
    info.append(f"Release: {platform.release()}")
    info.append(f"Version: {platform.version()}")
    info.append(f"Machine: {platform.machine()}")
    info.append(f"Processor: {platform.processor()}")
    info.append("")
    return '\n'.join(info)

def get_cpu_info():
    info = []
    info.append("===== CPU Information =====")
    info.append(f"Physical cores: {psutil.cpu_count(logical=False)}")
    info.append(f"Total cores: {psutil.cpu_count(logical=True)}")
    info.append(f"CPU Frequency: {psutil.cpu_freq().current:.2f} MHz")
    info.append(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    info.append("")
    return '\n'.join(info)

def get_memory_info():
    mem = psutil.virtual_memory()
    info = []
    info.append("===== Memory Information =====")
    info.append(f"Total: {get_size(mem.total)}")
    info.append(f"Available: {get_size(mem.available)}")
    info.append(f"Used: {get_size(mem.used)}")
    info.append(f"Percentage: {mem.percent}%")
    info.append("")
    return '\n'.join(info)

def get_disk_info():
    info = []
    total_disk = 0
    total_used = 0
    total_free = 0

    info.append("===== Disk Information =====")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        info.append(f"Device: {partition.device}")
        info.append(f"  Mountpoint: {partition.mountpoint}")
        info.append(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue

        total_disk += partition_usage.total
        total_used += partition_usage.used
        total_free += partition_usage.free

        info.append(f"  Total Size: {get_size(partition_usage.total)}")
        info.append(f"  Used: {get_size(partition_usage.used)}")
        info.append(f"  Free: {get_size(partition_usage.free)}")
        info.append(f"  Percentage Used: {partition_usage.percent}%")
        info.append("")

    info.append("===== Overall Disk Summary =====")
    info.append(f"Total Disk Size: {get_size(total_disk)}")
    info.append(f"Total Used Space: {get_size(total_used)}")
    info.append(f"Total Free Space: {get_size(total_free)}")
    if total_disk > 0:
        overall_used_percent = (total_used / total_disk) * 100
        info.append(f"Overall Used Percentage: {overall_used_percent:.2f}%")
    info.append("")

    return '\n'.join(info)

def get_network_info():
    info = []
    info.append("===== Network Information =====")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    info.append(f"Hostname: {hostname}")
    info.append(f"IP Address: {ip_address}")
    info.append("")
    return '\n'.join(info)

def get_size(bytes, suffix="B"):
    """Scale bytes to human-readable format."""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

if __name__ == "__main__":
    system_info = get_system_info()
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_info()
    network_info = get_network_info()

    full_summary = f"{system_info}\n{cpu_info}\n{memory_info}\n{disk_info}\n{network_info}"

    print("===== Overall System Configuration =====")
    print(full_summary)

    # Save to file
    file_name = 'system_report.txt'
    with open(file_name, 'w') as file:
        file.write(full_summary)

    print(f"\nSystem report saved successfully to {file_name}")
