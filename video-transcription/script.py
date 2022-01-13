import speech_recognition as sr
import moviepy.editor as mp
from datetime import datetime,time
import cv2
start_time=datetime.now()
clip = mp.VideoFileClip(r"video_recording.mp4")
#set fps,by default fps=30
fps=int(input("enter a custum fps for a video.."))
clip=clip.set_fps(fps)
clip.audio.write_audiofile(r"converted.wav")
r = sr.Recognizer()
audio = sr.AudioFile("converted.wav")
with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file)
print(result)
end_time=datetime.now()
print(f"fps : {clip.fps},execution time : {end_time-start_time}")
