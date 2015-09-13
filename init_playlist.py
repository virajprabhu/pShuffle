import os
from pyechonest import config, track
import operator

config.ECHO_NEST_API_KEY='B343XNJYVWXNUHFQT'

AUDIO_EXTENSIONS = set(['mp3', 'm4a', 'wav', 'ogg', 'au', 'mp4'])

def _bar(val, ref=100, char='='):
	if val:
		num_chars = int(val * float(ref))
		return char * max(1, num_chars)
	else:
		return char

def _is_audio(f):
	_, ext = os.path.splitext(f)
	ext = ext[1:]
	return ext in AUDIO_EXTENSIONS

def score_track(audio_file):
	print 'File: ', audio_file
	pytrack = track.track_from_filename(audio_file)
	# print 'Artist: ', pytrack.artist if hasattr(pytrack, 'artist') else 'Unknown'
	# print 'Title: ', pytrack.title if hasattr(pytrack, 'title') else 'Unknown'
	print 'Track ID: ', pytrack.id
	print 'Tempo: ', pytrack.tempo
	print 'Energy: %1.3f %s' % (pytrack.energy, _bar(pytrack.energy))
	if not pytrack.valence:
		print 'Force uploading...'
		pytrack = track.track_from_filename(audio_file, force_upload=True)
	score = pytrack.energy + pytrack.tempo
	
	# print 'Valence: %1.3f %s' % (pytrack.valence, _bar(pytrack.valence))
	# print 'Acousticness: %1.3f %s' % (pytrack.acousticness, _bar(pytrack.acousticness))
	return score, audio_file

def init_playlist(directory):
	playlist = []
	for f in os.listdir(directory):
		if _is_audio(f):
			path = os.path.join(directory, f)
			playlist.append(score_track(path))
	playlist = sorted(playlist, reverse=True)
	return playlist