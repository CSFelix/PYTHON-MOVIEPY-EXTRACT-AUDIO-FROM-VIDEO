from moviepy.editor import *

def extract(video_path, audio_name, audio_format):
	"""
	Function that extract audio from video
	Assintotic: O(1)
	"""
	video = VideoFileClip(video_path)
	audio = video.audio
	audio.write_audiofile(audio_name + '.' + audio_format)

try:
	video_path = input('Video Path:\n'
					  + 'Example: C:\\Videos\\music.mp4\n')
	audio_name = input('\nAudio File Name:\n')
	audio_option = input('\nChoose a format:\n'
						+ '0 - MP3 (default)\n'
						+ '1 - WAV\n')
	audio_format = 'wav' if audio_option == '1' else 'mp3'

	extract(video_path, audio_name, audio_format)

except Exception as e: print(e)
