import sys
from init_playlist import init_playlist
from pyechonest import song 
import math
import slider_demo

def main():
	slider_demo
	print slider_demo.freq
	num_swings = int(math.ceil(slider_demo.freq))	# obtain from mood graph
	num_buckets = num_swings + 1
	playlist = init_playlist(sys.argv[1])	# todo: create scored and sorted playlist

	# for i in range(0, len(playlist)):
	# 	print playlist[i]
	# print 'END'

	if(len(playlist) < num_buckets):	# there needs to be atleast one song per bucket
		print 'Not enough songs! Please add more.'
		return
	tag, bucket = [], []
	tag.append('UP')	# todo: set using mood graph
	tag.append('DN')
	tag.append('UP')
	tag.append('DN')

	for i in range(0, num_buckets):
		bucket.append([])

	for i in range(0, num_buckets-1):	# for swings
		if tag[i] == 'UP':
			head = playlist.pop(0)
			bucket[i].append(head)
			# bucket[i+1].append(head)
		else:
			tail = playlist.pop()
			bucket[i].append(tail)
			# bucket[i+1].append(tail)
		# print bucket[0]  , ' ', bucket[1] , ' ', bucket[2]  , ' ', bucket[3]  , ' '

	anchor_start = playlist.pop(0) if (tag[1] == 'UP') else playlist.pop() #anchors
	anchor_final = playlist.pop(0) if (tag[num_buckets-1] == 'DN') else playlist.pop()

	while(1):	# fillers
		for i in range(0, num_buckets):
			if(len(playlist)):
				if tag[i] == 'UP':
					bucket[i].append(playlist.pop(0))
				else:
					bucket[i].append(playlist.pop())
			else:
				bucket[0].append(anchor_start)	#append anchors
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
			print track[1]
main()