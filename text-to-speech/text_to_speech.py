import os
from gtts import gTTS
import codecs
from dotenv import load_dotenv
load_dotenv()
RATE = os.getenv('RATE')
language=os.getenv('language')
text_file=os.getenv('text_file')

with codecs.open(text_file, encoding='utf-8') as f:
     input=f.read()
     speech = gTTS(text=input, lang=language, slow=False)
     audio_file=f"{text_file.split('.')[0]}"+'.wav'
     speech.save(audio_file)
     os.system(f'start {audio_file}')
