import sys
import math
from pyechonest import song 
import moodgraph_input as mi
from setup_playlist import init_playlist

def main():
	mi.run()
	print mi.freq
	num_swings = int(math.ceil(mi.freq))	# Obtain from mood graph
	num_buckets = num_swings + 1
	playlist = init_playlist(sys.argv[1])	# Todo: create scored and sorted playlist.

	if(len(playlist) < num_buckets):	# There needs to be atleast one song per bucket.
		print 'Not enough songs! Please add more.'
		return

	bucket = []	

	# tag = ['UP', 'DN', 'UP', 'DN']	# Todo: Do this better

	for i in range(0, num_buckets):
		bucket.append([])

	# Swings
	for i in range(0, num_buckets-1):	
		if (i%2 == 0):
			head = playlist.pop(0)
			bucket[i].append(head)
			# bucket[i+1].append(head)
		else:
			tail = playlist.pop()
			bucket[i].append(tail)
			# bucket[i+1].append(tail)
		# print bucket[0]  , ' ', bucket[1] , ' ', bucket[2]  , ' ', bucket[3]  , ' '

	# Anchors
	anchor_start = playlist.pop() # if (tag[0] == 'UP') else playlist.pop() 
	anchor_final = playlist.pop(0) if ((num_buckets-1) % 2 == 1) else playlist.pop()

	# Fillers
	while(1):	
		for i in range(0, num_buckets):
			if(len(playlist)):
				if (i%2 == 0):
					bucket[i].append(playlist.pop(0))
				else:
					bucket[i].append(playlist.pop())
			else:
				bucket[0].append(anchor_start)	# Append anchors
				bucket[num_buckets-1].append(anchor_final)
				# print bucket[0]  , ' ', bucket[1] , ' ', bucket[2]  , ' ', bucket[3]  , ' '
				log_pshuffled_playlist(bucket)
				return
			# print bucket[0]  , ' ', bucket[1] , ' ', bucket[2]  , ' ', bucket[3]  , ' '

def log_pshuffled_playlist(bucket):
	for i in range (0, len(bucket)):
		print 'Logging bucket ', i
		while(len(bucket[i])):
			track = bucket[i].pop()
			print track[1], ':', track[0]
main()