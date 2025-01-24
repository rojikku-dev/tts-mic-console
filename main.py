import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from io import BytesIO

from pygame import mixer
from gtts import gTTS
from pydub import AudioSegment


mixer.init(devicename="CABLE Input(VB-Audio Virtual Cable)")
while True:
    sentence = input("> ").replace("ㅋ", "크")
    tts = gTTS(sentence, lang="ko")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    audio: AudioSegment = AudioSegment.from_file(fp, format="mp3")
    audio = audio.speedup(playback_speed=1.3, chunk_size=150, crossfade=25)
    audio.export("out.mp3")
    mixer.music.load("out.mp3")
    mixer.music.play()

    while mixer.music.get_busy():
        continue
    mixer.music.unload()
