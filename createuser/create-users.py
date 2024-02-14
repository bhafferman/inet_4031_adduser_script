#!/usr/bin/env python3
import os
import re
import sys

# TO RUN CODE: 
# sudo ./create-users.py < create-users.input or
# cat create-users.input | sudo ./create-users.py
def main():
	# take in input from shell
	for line in sys.stdin:
		# Add a line of code here. Use re.match and create a regular expression to 
		# check for the presence of a # at the start of a line. We want to skip any 
		# lines in the file that start with a hashtag: #
		match = re.match('^#', line)

		fields = line.strip().split(':')  # strip any whitespace and split into an array
		# explain what this is checking for and why
		# checking to make sure there is no # and the length of the line is good. If either of thoses
		# two things are true then the user account should not be created.

		# the continue here is for the FOR loop. So if the line
		# starts with a # or does NOT have five fields, we skip it
		# again the question to answer is why? 
		if match or len(fields) != 5:
			continue

		username = fields[0]
		password = fields[1]

		# first name and last name
		gecos = "%s %s,,," % (fields[3], fields[2])

		# add comment - what does this do and why?
		# user could/can be apart of more than one group, this code splits the groups they are 
		# appart of at the , 
		groups = fields[4].split(',')

		print("==> Creating account for %s..." % username)
		cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
		# print(cmd)
		os.system(cmd)  # what does this line do?
		# ^ (above line) actually executes the code, it passes the string cmd to the shell to run the 
		# line of code
		print("==> Setting the password for %s..." % username)
		cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
		# print(cmd)
		os.system(cmd)
		# add comment - what is this FOR loop doing and why?
		# user can be apart of more than one group, this loop adds all the groups that a user is apart of.
		for group in groups:
			if group != '-':
				print("==> Assigning %s to the %s group..." % (username, group))
				cmd = f"/usr/sbin/adduser {username} {group}"
				# print(cmd)
				os.system(cmd)

if __name__ == '__main__':
	main()
