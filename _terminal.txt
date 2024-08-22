# A sense of location

# print working directory
pwd
# change directory
cd
cd ~/Desktop
cd /etc
d ..


# Creating folders and files

# mkdir	make directory
mkdir /tmp/tutorial
mkdir dir1 dir2 dir3
# list
ls
ls > output.txt
# concatenate
cat output.txt
echo "This is a test"
echo "This is a test" > test_1.txt
less combined.txt


# Moving and manipulating files

# move
mv combined.txt dir1
# copy
cp combined.txt backup_combined.txt


# Deleting files and folders

# remove
rm folder_*
rmdir folder_*
rm -r folder_6


# The command line and the superuser

# Substitute User and do
sudo cat /etc/shadow
sudo apt install tree


# Hidden files

# .dot
mv combined.txt .combined.txt
cat .combined.txt
ls .hidden
