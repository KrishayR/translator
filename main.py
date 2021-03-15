import googletrans as gt
import speech_recognition as sr
import gtts
import playsound as ps
langu = 'es'
recognizer = sr.Recognizer()
translator = gt.Translator()
input_lang = 'es_MX'
output_lang = 'en'
try:
    with sr.Microphone() as source:
        print('Speak now...')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass
translated = translator.translate(text,dest=output_lang)
translated.text
converted_audio = gtts.gTTS(translated.text,lang=output_lang)
converted_audio.save('Desktop/python/Translator/speech.mp3')
ps.playsound('Desktop/python/Translator/speech.mp3')
#print(gt.LANGUAGES)
