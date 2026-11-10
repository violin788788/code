import subprocess

def restart_windows_8():
    """
    Initiates an immediate restart on a Windows 8 system.
    /r - Restarts the computer.
    /t 0 - Sets the time-out period before shutdown to 0 seconds (immediate).
    """
    try:
        print("Initiating system restart...")
        subprocess.call(["shutdown", "/r", "/t", "0"])
    except Exception as e:
        print(f"Failed to execute restart command: {e}")

if __name__ == "__main__":
    # Ensure all your work is saved before running this script
    restart_windows_8()