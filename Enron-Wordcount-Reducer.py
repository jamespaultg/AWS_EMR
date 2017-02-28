#!/usr/bin/env python
import sys
# initialize variables
current_count = 0
current_word = ""
# line-wise iterate over standard input (stdin)
# (recall, each line is expected to consist of a tab-('\t')-separated
# (key,value) pair)
for line in sys.stdin:
	# split line (after stripping off any leading/trailing whitespace)
	# on tab ('\t') into key & value
	line = line.strip().split('\t')
	# sanity check: did we indeed get exactly two parts (key & value)?
	# if not, skip line and continue with next line
	if len(line) != 2:
		continue

	# extract key
	key = line[0]
	# new (next) key
	# (recall, keys are expected to arrive in sorted order)
	if (key != current_word):
		if (current_count > 1):
			# print previous key and aggregated count
			# as tab-('\t')-separated (key,value) pair
			print(current_word + '\t' + str(current_count))
		# reset counter to 0 and recall new key
		current_count = 0
		current_word = key
	# increment count by 1
	current_count += 1

if (current_count > 1):
	# print last key and its aggregated count
	# as tab-('\t')-separated (key,value) pair
	print(current_word + '\t' + str(current_count))
