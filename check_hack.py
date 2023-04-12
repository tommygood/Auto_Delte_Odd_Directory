import subprocess
from subprocess import call, PIPE, run
import datetime
import os                                                                                                               
# Define the directory to list directories from
directory = "/home/wang/test"

# Get a list of all items (files and directories) in the directory
items = os.listdir(directory)

# Filter the list to only include directories
dir_list = [os.path.join(directory, item) for item in items if os.path.isdir(os.path.join(directory, item))]

# white list
white_list_directory = [directory, directory + '/test1']

# filter white list
for i in white_list_directory :
    if i in dir_list :
        dir_list.remove(i)

# Print the list of directories
print(dir_list)

# record the odd directory
log_path = '/home/wang/test/test.log'
text_file = open(log_path, "w")

for i in dir_list :
    text_file.write(str(datetime.datetime.now()) + " " + str(i) + "\n")

text_file.close()

# mv the odd directory to temp directory, this directory path do not include in the direcory path
changed_path = '/home/wang/test1'

text_file = open(log_path, "a")
for i in dir_list :
    result = run(["mv", i, changed_path], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    text_file.write(str(datetime.datetime.now()) + " " + str(result) + "\n")

text_file.close()
