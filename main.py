
import openai
from moviepy.editor import VideoFileClip, AudioFileClip
import os
video_file = "./pexels-matthias-groeneveld-5692323 (1080p) (1).mp4"
audio_file = "./Jux Ft Diamond Platnumz - Enjoy (Official Video).mp3"
video_clip = VideoFileClip(video_file)
audio_clip = AudioFileClip(audio_file)
video_clip = video_clip.set_audio(audio_clip)
current_directory = os.getcwd()
output_file = os.path.join(current_directory, "combined_video.mp4")
video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
print(f"Combined video saved as {output_file}")
api_key="api_key"
openai.api_key=api_key
def transcribe(audio):
    transcript = openai.Audio.transcribe("whisper-1", audio)
    print(transcript)

transcribe(audio_clip)