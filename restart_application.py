import os
import time
import subprocess

def restart_docker_container():
    try:
        subprocess.run(["sudo", "docker", "restart", "nginx"], check=True)
        print("Docker container restarted.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting Docker container: {e}")

def check_and_restart():
    while True:
        status = os.system("python3 monitor_website.py")
        if status != 0:
            restart_docker_container()
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    check_and_restart()

