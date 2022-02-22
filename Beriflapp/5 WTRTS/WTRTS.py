# Write the result to STDOUT.

import sys

# Stdout assigned to a variable
var = sys.stdout
arr = ['Beriflapp', 'is', 'a', 'great', 'Company']

# Printing everything in the same line
for i in arr:
	var.write(i)
 
# Printing everything in a new line
for j in arr:
	var.write('\n'+j)
