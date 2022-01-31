import wave

# Create audio file wave object
good_morning = wave.open('good_morning.wav', 'r')

# Read all frames from wave object 
signal_gm = good_morning.readframes(-1)

# View first 10
print(signal_gm[:10])



# de bytes a integer 

"""

para esto usamos numpy

# Para convertir  bytes into integer usamos

signal_gm = np.frombuffer(soundwave_gm, dtype='int16')

Finding the frame rate

* Frequency(Hz) = length of wave object array/duration of audio file (seconds)

Python wave module has a programatic way to do this

* framerate_gm = good_morning.getframerate()

We can use this frame rate variable for one more thing which will be handy for visualizing our sound waves later


T (periodo)/ duration of audio file (seconds) = length of wave object array/frequency(Hz)

con este valor podemos usar np.linspace para figurarnos donde cada sound wave value occurs

np.linspace(start=1, stop=10, num=10)# num cantidad de elementos equiespaciados, esto me devuelve un array

example

# Get the timestamps of the good morning sound wave

time_gm = np.linspace(start=0,
					  stop=len(soundwave_gm)/framerate_gm,
					  num=len(soundwave_gm))

















Each of these values is the time in seconds where each sound wave byte occurred.

we'll be able to use these timestamp values later to see what our sound wave looks like
"""

#-----------------------------------------------------------------------------------
import numpy as np

# Open good morning sound wave and read frames as bytes
good_morning = wave.open('good_morning.wav', 'r')
signal_gm = good_morning.readframes(-1)

# Convert good morning audio bytes to integers
soundwave_gm = np.frombuffer(signal_gm, dtype='int16')

# View the first 10 sound wave values
print(soundwave_gm[:10])




# Read in sound wave and convert from bytes to integers
good_morning = wave.open('good_morning.wav', 'r')
signal_gm = good_morning.readframes(-1)
soundwave_gm = np.frombuffer(signal_gm, dtype='int16')

# Get the sound wave frame rate
framerate_gm = good_morning.getframerate()

# Find the sound wave timestamps
time_gm = np.linspace(start=0,
                      stop=len(soundwave_gm)/framerate_gm,
					  num=len(soundwave_gm))

# Print the first 10 timestamps
print(time_gm[:10])







"""
visualizing sound waves

having your audio files at the same frame rate and ensuring the same data transformations are made on each of them is important

this is because, if they're different, we've got the potential for data mismatches, which will prevent us from further processing

The x-axis will be the timestamps we've calculated, measured in seconds

and the y-axis is the amplitude or how much the sound wave displaces air particles as it moves through the air.

el parametro alpha=0.5 de la funcion plot agrega transparencia


"""


# Setup the title and axis titles
plt.title('Good Afternoon vs. Good Morning')
plt.ylabel('Amplitude')
plt.xlabel('Time (seconds)')

# Add the Good Afternoon data to the plot
plt.plot(time_ga,soundwave_ga, label='Good Afternoon')

# Add the Good Morning data to the plot
plt.plot(time_gm,soundwave_gm, label='Good Morning',
   # Set the alpha variable to 0.5
   alpha=0.5)

plt.legend()
plt.show()




"""

To get started with spoken language recognition, let's check out the SpeechRecognition Python Library

Google's web speech API to transcribe speech to text



Automatic speech recognition is a tough challenge

and there's no shortage of companies and research institutions working on libraries to help solve it.


Some existing python libraries

* CMU Sphnx

* Kaldi

* SpeechRecognition

* Wav2letter++ by facebook

all have the same goal of transcribing audio files to text.


nosotros empezaremos con SpeechRecognition library

pip install SpeechRecognition

# Import the SpeechRecognition library

import speech_recognition as sr


# Create an instance of Recognizer

recognizer = sr.Recognizer()

# Set the energy threshold

recognizer.energy_threshold = 300 


The energy threshold can be thought of as th loudness of audio which is considered speech.

Values below the threshold are considerd silence, values above are considered speech.

A silent room is typically between 0 and 100.

SpeechRecognition's documentation recommends 300 as a starting value which cover most speech files.

The energy threshold value will adjust automatically as the recognizer listens to an audio file


Now we've got a recognizer instance ready, it's time to recognize some speech.


SpeechRecognition has functions built-in to work with many of th best speech recognition APis.


* Recognizer class has buil-in functions which interact with speech APIs

* recognize_bing()#microsoft
* recognize_google()#google free
* recognize_google_cloud()
* recognize_wit()

They all accept an audio file and return text, which is hopefully the transcribed speech from the audio file

Input: audio_file

Output: transcribed speech from audio_file

Speech recognition is still far from perfect.

We'll be using the recognize google function since it's free and doesn't require an API key

However, this limits us to 50 request per day and if our audio files are too long, it may time out

no issues with audio files under 5-minutes.
"""

# import SpeechRecognition library

import speech_recognition as sr

# Instantiate Recognizer class

recognizer = sr.Recognizer()

# Transcribe speech using google web API

recognizer.recognize_google(audio_data=audio_file,
									 language="en-US")




"""
The energy_threshold is a number between 0 and 4000 for how much the Recognizer class should listen to an audio file.

energy_threshold will dynamically adjust whilst the recognizer class listens to audio.

"""


# Create a recognizer class
recognizer = sr.Recognizer()

# Transcribe the support call audio
text = recognizer.recognize_google(
  audio_data=clean_support_call_audio, 
  language="en-US")

print(text)


# audio files require a bit of preprocessing before they can be worked with.

"""
SpeechRecognition library has a built-in class,

AudioFile, along with another handy method in the Recognizer class, record. We can use these to take of the preprocessing for us
"""


import speech_recognition as sr

# Setup recognizer instance

recognizer = sr.Recognizer()

# Read in audio file

clean_support_call = sr.AudioFile("clean-support-call.wav")

# Check type of clean_support_call
type(clean_support_call)

"""
we must passt from AudioFile class to audiodata para poder usar el recognizer de gooogle

para esto usamos el metodo de la clase recognizer llamado record


"""

# Convert from AudioFile to AudioData

with clean_support_call as source:
	# Record the audio
	clean_support_call_audio = recognizer.record(source)

# Check the type

type(clean_support_call_audio)

# Now is AudioData, then i can pass it to the google recognizer

"""
el metodo record tiene 2 parametros

* duration and offset both None by default

The record method records up to duration seconds of audio from source starting at offset.

Thi means that by default, record will record from the beginning of the file until there is no more audio.
(esto en segundos)
the offset parameter can be used to cut off or skip over a specified amount of second at the start of an audio file

"""


"""




"""


# Instantiate Recognizer
recognizer = sr.Recognizer()

# Convert audio to AudioFile
clean_support_call = sr.AudioFile('clean_support_call.wav')

# Convert AudioFile to AudioData
with clean_support_call as source:
    clean_support_call_audio = recognizer.record(source)

# Transcribe AudioData to text
text = recognizer.recognize_google(clean_support_call_audio,
                                   language="en-US")
print(text)



"""

Sometimes you may not want the entire audio file you're working with. The duration and offset parameters of the record() method can help with this.

After exploring your dataset, you find there's one file, imported as nothing_at_end which has 30-seconds of silence at the end and a support call file, imported as out_of_warranty has 3-seconds of static at the front.

Setting duration and offset means the record() method will record up to duration audio starting at offset. They're both measured in seconds.


"""


# Convert AudioFile to AudioData
with static_at_start as source:
    static_art_start_audio = recognizer.record(source,
                                               duration=None,
                                               offset=3)

# Transcribe AudioData to text
text = recognizer.recognize_google(static_art_start_audio,
                                   language="en-US")

print(text)






#---------------------------------------------------------------------------------------------------------

"""

Dealing with different kinds of audio

there are some limitation to the library

challanges you might run into and what you can do about them.


"What language"

SpeechrRecognition library doesn't automatically detect languages
So you'll have to ensure this parameter is set manually and make sure the API you're using has the capability to transribe the language your audio files are in.

Non-speech audio

Nosotros podemos prevenir errores si usamos "show_all= True", parametro del metodo recognize_google

The show all parameter shows a list of all the potential transcriptions the recognize google function came up with.

Multiple speakers

The free Google web APi transcribe speech and returns it as a single block of text no matter how many speakers there are 


A returned single text block can still be useful, however, if your problem requires, knowing who said what, you may want to consider the free API we're using as a proof of a concept

And then use one of the paid version for more complex tasks.

The process of splitting more than one speaker from a single audio file is called speaker diarization, however, it is beyond the scope of this course.


To get around the multiple speakers problem, you could  ensure your audio files are recorded separately for each speaker.

# Import audio files separately

speakers = [sr.AudioFile("s0.wav"),  sr.AudioFile("s1.wav"), sr.AudioFile("s2.wav")]

Then transcribe the individual speakers audio.



"""

# Import audio files separtely

speakers = [sr.AudioFile("s0.wav"), sr.AudioFile("s1.wav"), sr.AudioFile("s2.wav")]

# Transcribe each speaker individually


for i, speaker in enumerate(speakers):
		with speaker  as source:
			speaker_audio = recognizer.record(source)
		print(f"text from speaker" {i}: {recognizer.recognize_google(speaker_audio)})	

"""


Noisy audio

* if you have trouble hearing the speech, so will the APIs

to try and accommodate for background noise, the recognizer class has  a built-intfunction, adjust for ambient noise, which takes a parameter, duration

the recognizer class then listens for duration seconds at the start of the audio file an adjust the energy threshold, or the amount the recognizer class listens, to a level suitable for background noise.

How much space you have at the start of your audio file will dictate what you can set the duration value to.

The SpeechRecognition documentation recommends somewhere between 0.5 to 1 seconds as a good starting point.

"""


# Import audio file with background noise


noisy_support_call = sr.AudioFile(noisy_support_cal.wav)

with noisy_support_call as source:
	# Adjust for ambient noise and record

	recognizer.adjust_for_ambient_noise(source,
													duration=0.5)

	noisy_support_call_audio = recognizer.record(source)

# Recognize the audio

recognizer.recognize_google(noisy_support_call_audio)




"""
Multiple Speakers 2
Deciphering between multiple speakers in one audio file is called speaker diarization. However, you've seen the free function we've been using, recognize_google() doesn't have the ability to transcribe different speakers.

One way around this, without using one of the paid speech to text services, is to ensure your audio files are single speaker.

This means if you were working with phone call data, you would make sure the caller and receiver are recorded separately. Then you could transcribe each file individually.

In this exercise, we'll transcribe each of the speakers in our multiple speakers audio file individually.

"""



recognizer = sr.Recognizer()

# Multiple speakers on different files
speakers = [sr.AudioFile("speaker_0.wav"), 
            sr.AudioFile("speaker_1.wav"), 
            sr.AudioFile("speaker_2.wav")]

# Transcribe each speaker individually
for i, speaker in enumerate(speakers):
    with speaker as source:
        speaker_audio = recognizer.record(source)
    print(f"Text from speaker {i}:")
    print(recognizer.recognize_google(speaker_audio,
         				  language="en-US"))



"""
Working with noisy audio
In this exercise, we'll start by transcribing a clean speech sample to text and then see what happens when we add some background noise.

A clean audio sample has been imported as clean_support_call.

Play clean support call.

We'll then do the same with the noisy audio file saved as noisy_support_call. It has the same speech as clean_support_call but with additional background noise.

Play noisy support call.

To try and negate the background noise, we'll take advantage of Recognizer's adjust_for_ambient_noise() function.



"""


"""



"""

recognizer = sr.Recognizer()

# Record the audio from the noisy support call
with noisy_support_call as source:
	# Adjust the recognizer energy threshold for ambient noise
    recognizer.adjust_for_ambient_noise(source, duration=1)
    noisy_support_call_audio = recognizer.record(noisy_support_call)
 
# Transcribe the speech from the noisy support call
text = recognizer.recognize_google(noisy_support_call_audio,
                                   language="en-US",
                                   show_all=True)

print(text)





# Introduccion to PyDub-------------------------------------------------------------------------------------------------
"""
A big part of working with data, especially audio files, is ensuring it's  all in a consistent format


PyDub is a Python library which provides a gold mine of tools to manipulating audio files.

Becoming familiar with PyDub will give you a programmatic way to ensure your audio files are consistent and
in an ideal format for transcription locally or through an API

pip install pydub

but if using other than .wav, intall ffmpeg via ffmpeg.org

PyDub's main class, AudioSegment

# import pydub main class

from pydub import AudioSegment

# import a audio file
----------------------- path
wav_file = AudioSegment.from_file(file="wav_file.wav", format="wav")



type(wav_file)

#pydub.audio_segment


Playing an audio fil

Let's say you wanted to play an audio file to check it's quality, you can use the play function on any AudioSegment.


The play function requires simpleaudio or pyaudio for wav playback and ffmpeg for all other

then we can do

# import play function

from pydub.playback import play

"""

from pydub.playback import play

# import audio file

wav_file = AudioSegment.from_file(file="wav_file.wav")

# PLay audio file


play(wav_file)




"""
When you import a file with .from_file, PyDub automatically infers number of parameters  about the file

These are stored as attributes in the AudioSegment instance

for example, calling channels on AudioSegment will show you the number of channels, 1 for mono, 2 for stereo audio
Calling frame rate gives you the sample of your AudioSegment in Hertz


sample width tells you the number of bytes per sample, retorna un entero con el numero de bytes

"""

# Import audio files

wav_file = AudioSegment.from_file(file="wav_file.wav")

two_speakers = AudioSegment.from_file(file="two_speakers.wav")


# check number of channels

wav_file.channels, two_speakers.channels



wav_file.frame_rate

# Find the number of bytes per sample

wav_file.sample_width

# Max will tell you the max amplitude of your audio file, 

wav_file.max # this can be considered loudnes and is useful for normalizing sound levels

# finally calling len on any AudioSegment will tell you the duration of the audio file in miliseconds
# Having these parameters readily available is helpful to ensure all of your audio files are consistent.

# You can adjust them using .set_ATTRIBUTENAME(x)

# ejemplo
# esto es usar el settr
wav_file_width_1 = wav_file.sample_width(1)
# esto es consultar un atributo
wav_file_width_1.sample_width


# CHange sample rate

wav_file_16k = wav_file.set_frame_rate(16000)

wav_file_16k.frame_rate

# to alter el number of channels

wav_file_1_channel = wav_file.set_channels(1)

wav_file_1_channel.channels


# Some APIs require your audio files to have certain values for these parameters



"""

A rule of thumb is the higher the values, excluding channels, the better.


Import an audio file with PyDub
PyDub's AudioSegment class makes it easy to import and manipulate audio files with Python.

In this exercise, we'll import an audio file of interest by creating an instance of AudioSegment.

To import an audio file, you can use the from_file() function on AudioSegment and pass it your target audio file's pathname as a string. The format parameter gives you an option to specify the format of your audio file, however, this is optional as PyDub will automatically infer it.

PyDub works with .wav files without any extra dependencies but for other file types like .mp3, you'll need to install ffmpeg.

A sample audio file has been setup as wav_file.wav, you can listen to it here.






Play an audio file with PyDub
If you're working with audio files, chances are you want to listen to them.

PyDub's playback module provides a function called play() which can be passed an AudioSegment. Running the play() function with an AudioSegment passed in will play the AudioSegment out loud.

This can be helpful to check the quality of your audio files and assess any changes you need to make.

In this exercise you'll see how simple it is to use the play() function.

Remember: to use the play() function, you'll need simpleaudio or pyaudio installed for .wav files and ffmpeg for other kinds of files.





"""

# Import AudioSegment and play
from pydub import AudioSegment
from pydub.playback import play

# Create an AudioSegment instance
wav_file = AudioSegment.from_file(file="wav_file.wav", 
                                  format="wav")

# Play the audio file
play(wav_file)


"""
Audio parameters with PyDub
Every audio file you work with will have a number of characteristics associated with them, such as, channels, frame rate (or sample rate), sample width and more.

Knowing these parameters is useful to ensure your audio files are compatible with various API requirements for speech transcription.

For example, many APIs recommend a minimum frame rate (wav_file.frame_rate) of 16,000 Hz.

When you create an instance of AudioSegment, PyDub automatically infers these parameters from your audio files and saves them as attributes.

In this exercise, we'll explore these attributes.

"""


"""
Adjusting audio parameters
During your exploratory data analysis, you may find some of the parameters of your audio files differ or are incompatible with speech recognition APIs.

Don't worry, PyDub has built-in functionality which allows you to change various attributes.

For example, you can set the frame rate of your audio file calling set_frame_rate() on your AudioSegment instance and passing it an integer of the desired frame rate measured in Hertz.

In this exercise, we'll practice altering some audio attributes.

"""
# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Create a new wav file with adjusted frame rate
wav_file_16k = wav_file.set_frame_rate(16000)

# Check the frame rate of the new wav file
print(wav_file_16k.frame_rate)
# # Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Set number of channels to 1
wav_file_1_ch = wav_file.set_channels(1)

# Check the number of channels
print(wav_file_1_ch.channels)
# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Print sample_width
print(f"Old sample width: {wav_file.sample_width}")

# Set sample_width to 1
wav_file_sw_1 = wav_file.set_sample_width(1)

# Check new sample_width
print(f"New sample width: {wav_file_sw_1.sample_width}")





"""

Manipulating audio
files with PyDub


Turning it down to 11

Are your audio files too loud or too quiet?


You can make your AudioSegments louder or quieter by adding or subtrating integers

for example

let's make our wav file 60 decibels quieter


# Import audio file


wav_file = AudioSegment.from_file("wav_file.wav")


# Minus 60 db

quiet_wav_file = wav_file - 60
"""

"""

You'll see if you tried to transcribe audio this quite with
recognize google as we saw in an earlier lesson, it would return an error.


# In practice, you're more likely to want to increase the volume of your AudioSegments

You can do this by adding an integer

This will increase your AudioSegment's average volumne level by th same number of decibels


if your audio files are too quiet or too loud, they may produce transcription erros.


As you could imagine, speech transcription works best on clear, audible speech.

If you can't hear it, chances are, a speech recognition system can't either. 


This all sounds the same



Some audio files might differ in loudness throughout.

They might begin quiet and then increase in sound as a person get comfortable talking or adjusts the microphone

The normalize function is great for taking care of this

it finds the highest level of audio throughout an AudioSegment and then boosts the rest of the audio up to match
# 


"""

# Import AudioSegment and nomralize

from pydub import AudioSegment

from pydub.effects import normalize

from pydub.playback import play


# import uneve sound audio file

loud_quiet = AudioSegment.from_file("loud_quiet.wav")

# Normalize the sound levels

normalized_loud_quiet = normalize(loud_quiet)


# check the sound

play(normalized_loud_quiet)

"""
Ensuring your audio files  is the same loudness throughout can help with transcription.



Another handy feature of AudioSegments is that they are sliceable and combinable


This is helpful if you need to cut your audio file down or combine them in some way

por ejemplo

let's say you knew your audio files had 5-seconds of static at the beginning and you didn'te want to waste compute power trying to transribe the static.


You could use slicing to remove the first 5-seconds of audio. Since AudioSegment are measure in miliseconds, you would do this by only keeping
everything after 5000

And then the new AudioSegment won't contain the 5-seconds of static
"""

# Import audio with static at start

static_at_start = AudiSegment.from_file("static_at_start.wav")

# Remove the static via slicing

no_static_at_start = static_at_start[5000:]


# check the new sound


play(no_static_at_start)




"""


Remixing your audio files


What if your audio file came in separate parts?
Due to length issues or a broken recording?


You can easily add two AudioSegmenets together using the addition operator



# Import two audio files


wav_file_1 = AudioSegment.from_file("wav_file_1.wav")

wav_file_2 = AudioSegment.from_file("wav_file_2.wav")

# Combine the two audio files

wav_file_3 = wav_file_1 + wav_file_2



# check the sound

play(wav_file_3)

"""


"""
Operators on AudioSegments work in order of Operation


# Combine two wav files and make the combination louder

louder_wav_file_3 = wav_file_1 + wav_file_2 + 10

wav file 1 plus wav file 2 plus 10, will combine wav file 1 and 2 and increase th combination by 10 decibels

If your audio files have different characteristics, combining them like this automatically scales parameters such as frame rate to be equal to the higher quality audio file




"""


"""
Splitting your audio

In the previous lesson, we saw the issue of transcribing multiple speakers on one audio file

Well, let's say you were trying to transcribe phone calls and using PyDub, you found your audio files are recorded in stereo format, Two channels

PyDub allows for a stereo AudionSegment to split into two mono single chanel Audio segments using the split to mono function

Calling this returns a list containing each channel



"""

# Import phone call audio

phone_call = AudioSegment.from_file("phone_call.wav")

# Find number of channels

phone_call.channels


# Split stereo to mono


phone_call_channels = phone_call.split_to_mono()

phono_call_chanels # me regresa una lista


"""
Because each of these is an AudioSegment, you can use all of th functionality you've seen previously on them


And as long as your speakers have been recorded on separate channels, you can now transcribe their audio individually.





"""



# Find number of channels of first list item

phone_call_channels[0].channels


# Recognize the first channel

recognizer.recognize_google(phone_call_channel_1)


"""
Turning it down... then up
Speech recognition works best on clean, audible speech. If your audio files are too quiet or too loud, it can hinder transcription.

In this exercise, you'll see how to make an AudioSegment quieter or louder.

Since the play() function won't play your changes in the DataCamp classroom.

The baseline audio file, volume_adjusted.wav can be heard here.

"""


from pydub import AudioSegment

# Import audio file
volume_adjusted = AudioSegment.from_file("volume_adjusted.wav")

# Increase the volume by 15 dB
louder_volume_adjusted = volume_adjusted + 15



"""
Normalizing an audio file with PyDub
Sometimes you'll have audio files where the speech is loud in some portions and quiet in others. Having this variance in volume can hinder transcription.

Luckily, PyDub's effects module has a function called normalize() which finds the maximum volume of an AudioSegment, then adjusts the rest of the AudioSegment to be in proportion. This means the quiet parts will get a volume boost.

You can listen to an example of an audio file which starts as loud then goes quiet, loud_then_quiet.wav, here.

In this exercise, you'll use normalize() to normalize the volume of our file, making it sound more like this.


"""
# Import AudioSegment and normalize
from pydub import AudioSegment
from pydub.effects import normalize

# Import target audio file
loud_then_quiet = AudioSegment.from_file("loud_then_quiet.wav")

# Normalize target audio file
normalized_loud_then_quiet = normalize(loud_then_quiet)






"""
Chopping and changing audio files
Some of your audio files may have sections of redundancy. For example, you might find at the beginning of each file, there's a few seconds of static.

Instead of wasting compute trying to transcribe static, you can remove it.

Since an AudioSegment is iterable, and measured in milliseconds, you can use slicing to alter the length.

To get the first 3-seconds of wav_file, you'd use wav_file[:3000].

You can also add two AudioSegment's together using the addition operator. This is helpful if you need to combine several audio files.

To practice both of these, we're going to remove the first four seconds of part1.wav, and add the remainder to part2.wav. Leaving the end result sounding like part_3.wav.


"""



from pydub import AudioSegment

# Import part 1 and part 2 audio files
part_1 = AudioSegment.from_file("part_1.wav")
part_2 = AudioSegment.from_file("part_2.wav")

# Remove the first four seconds of part 1
part_1_removed = part_1[4000:]

# Add the remainder of part 1 and part 2 together
part_3 = part_1_removed + part_2




"""
Splitting stereo audio to mono with PyDub
If you're trying to transcribe phone calls, there's a chance they've been recorded in stereo format, with one speaker on each channel.

As you've seen, it's hard to transcribe an audio file with more than one speaker. One solution is to split the audio file with multiple speakers into single files with individual speakers.

PyDub's split_to_mono() function can help with this. When called on an AudioSegment recorded in stereo, it returns a list of two separate AudioSegment's in mono format, one for each channel.

In this exercise, you'll practice this by splitting this stereo phone call (stereo_phone_call.wav) recording into channel 1 and channel 2. This separates the two speakers, allowing for easier transcription.
"""


"""
Now you've seen how feature rich PyDub is for manipulating audio and you've

and you made some changes to your files, how do you gt access to your altered audio files

PyDub has a built-in method for exporting AudioSegments.

"""

from pydub import AudioSegment


# Import audio file


wav_file = AudioSegment.from_file("wav_file.wav")


# Increase by 10 decibels

louder_wav_file = wav_file + 10

# Export louder audio file
#----------------------out-path, format
# default format es mp3
louder_wav_file.export(out_f="louder_wav_file.wav", format="wav") 




# Reformatting and explorting multiple audio files

"""
You'll likely want to work with and manipulate many audio files at once

"""


def make_wav(wrong_folder_path, righ_folder_path):
	# Loop through wrongly formatted files

	for file in os.scandir(wrong_folder_path):

		if file.path.endswith(".mp3") or file.path.endswith(".flac"):

			# Create the new .wav filename
			
			out_file = right_folder_path + os.path.splitext(os.path.basename(file.path))[0]	 + ".wav"
		# Read in the audio file and export it in wav format

		AudioSegment.from_file(file.path).export(out_file,
															  format="wav")


		print(f"Creating {out_file}")





"""
You could expand upon this function to manipulate the audio files as you go before exporting them

Manipulating aand exporting


During your exploratory data analysis, you find each of your audio files has 3-seconds of static at the start and are quieter than you'd like

The workflow is much the same as the previous function
"""

def make_no_static_louder(static_quiet, louder_no_static):
	# Loop through files with static and quiet(already in wav format)
	for file in os.scandir(static_quiet):

		# Create new file path
	
		out_file = louder_no_static + os.path.splitext(os.path.basename(file.path))[0] + ".wav"

		# Read the audio file

		audio_file = AudioSegment.from_file(file.path)

		# Remove first thre seconds and add 10 decibels and export

		audio_file = (audio_file[3100:] + 10).export(out_file, format="wav")

		print(f"Creating {out_file}")





# Remove static and make louder


make_no_static_louder("data/static_quiet", "data/louder_no_static/")






"""
Exporting and reformatting audio files
If you've made some changes to your audio files, or if they've got the wrong file extension, you can use PyDub to export and save them as new audio files.

You can do this by using the .export() function on any instance of an AudioSegment you've created. The export() function takes two parameters, out_f, or the destination file path of your audio file and format, the format you'd like your new audio file to be. Both of these are strings. format is "mp3" by default so be sure to change it if you need.

In this exercise, you'll import this .mp3 file (mp3_file.mp3) and then export it with the .wav extension using .export().

Remember, to work with files other than .wav, you'll need ffmpeg.


"""


from pydub import AudioSegment

# Import the .mp3 file
mp3_file = AudioSegment.from_file("mp3_file.mp3")

# Export the .mp3 file as wav
mp3_file.export(out_f="mp3_file.wav",
                format="wav")





# Loop through the files in the folder
for audio_file in folder:
    
	# Create the new .wav filename
    print("que hace esto")
    print(os.path.basename(audio_file))
    a = os.path.basename(audio_file) #good_afternoon_aac.aac
    
    print(os.path.splitext(a))
    b = os.path.splitext(a)# ('good_afternoon_aac', '.aac')

    print(b[0]) # good_afternoon_aac

    
    wav_filename = os.path.splitext(os.path.basename(audio_file))[0] + ".wav"
        
    # Read audio_file and export it in wav format
    AudioSegment.from_file(audio_file).export(out_f=wav_filename, 
                                      format="wav")
        
    print(f"Creating {wav_filename}...")



"""
An audio processing workflow
You've seen how to import and manipulate a single audio file using PyDub. But what if you had a folder with multiple audio files you needed to convert?

In this exercise we'll use PyDub to format a folder of files to be ready to use with speech_recognition.

You've found your customer call files all have 3-seconds of static at the start and are quieter than they could be.

To fix this, we'll use PyDub to cut the static, increase the sound level and convert them to the .wav extension.

You can listen to an unformatted example here.

"""


for audio_file in folder:
    file_with_static = AudioSegment.from_file(audio_file)

    # Cut the 3-seconds of static off
    file_without_static = file_with_static[3000:]

    # Increase the volume by 10dB
    louder_file_without_static = file_without_static + 10
    
    # Create the .wav filename for export
    wav_filename = os.path.splitext(os.path.basename(audio_file))[0] + ".wav"
    
    # Export the louder file without static as .wav
    louder_file_without_static.export(wav_filename, format="wav")
    print(f"Creating {wav_filename}...")




















   # ------------------------------------------------------------------------------------------------

   """

	Creating 
	Transcription helper funtions

	Spoken language processing in python

   
	Together by building a proof of concept spoken language processing pipeline.

	"Acme Studios, a technology company, has approached you to use your speech processing skills to gain insights on their customer support calls, They've sent you a handful of audio samples to explore and to see what you can find"

	"they let you know they're not quite sure of the quality of the files of the format they're recorded in"

	"You open the folder of audio files Acme have sent through using the os module's listdir function and notice they're in the mp3 format"

   
	# import os module

	import os

	# check the folder of audio files

	os.listdir("acme_audio_files") # (['call_1.mp3', 'call_2.mp3', 'call_3.mp3', 'call_4.mp3'])


	Before continuing you decide to write down list of things you're goint to do prepare for building the proof of concept
   
	Preparing for the proof of concept

	The first thing will be to listen to a few of the files using your media player o pydub's play function, to get an understanding of what you're working with, and then transcribe one as soon as possible using recognize google so you have a baseline to work off

	you convert the first file to wav and transcribe but you know from previous work, doing this for every file is tedios





   """


import speech_recognition as speech_recognition

from pydub import AudioSegment

# Import call 1 and convert to .wav

call_1 = AudioSegment.from_file("acme_audio_files/call_1.mp3")

call_1.export("acme_audio_files/call_1.wav", format="wav")


# Transcribe call 1


recognizer = sr.Recognizer()


call_1_file = sr.Audiofile("acme_audio_files/call_1.wav")


with call_1_file as source:
	call_1_audio = recognizer.record(call_1_file)

recognizer.recognize_google(call_1_audio)


"""
You decide it's a good idea to create functions which will help you for the rest of the proof of concept
"""



"""
Functions we'll create

* convert_to_wav() converts non- .wav files to  .wav files

* show_pydub_stats() shows the audio attributes of a .wav file

* transcribe_audio() usdes recognize_google() to transcribe a .wav file.


"""


"""
Creating a file format conversion function

"""


def convert_to_wav(filename):
	"Takes an audio file of non .wav format and converts to .wav"

	# Import audio file

	audio = AudioSegment.from_file(filename)

	# Create new filename

	new_filename = filename.split(".")[0] + ".wav"


	# Export file as .wav

	audio.export(new_filename, format="wav")

	print(f"Converting {filename} to {new_filename}"....)


	Now you can convert audio files without repeating yourself.path

	convert_to_wav("acme_studios_audio/call_1.mp3")



"""
Now let's make one to find an audio files attributes using Pydub

Creating an attribute showing function



"""


def show_pydub_stats(filename):
	"Return different audio attributes related to an audio file."

	# Create AudioSegment instance


	audio_segment = AudioSegment.from_file(filename)

	# Print attributes


	print(f"Channels: {audio_segment.channels}" )

	print(f"Sample width: {audio_segment.sample_width}")

	print(f"Frame rate (sample rate): {audio_segment.frame_rate}")

	print(f"Frame width: {audio_segment.frame_width}")

	print(f"Length (ms): {len(audio_segment)}" )

	print(f"Frame count: {audio_segment.frame_count()}")




show_pydub_stats("acme_audio_files/call_1.wav")

"""
Since you're working with customer support calls, this will help especially with files with different numbers of channels., if there are two channels, you might be abel to split them  and transcribe each speaker separately.
"""

"""
Finally, since you could be transcribing many audio files, you create a function to transcribe an audio file and returns transcribed text

"""



# Create a function to transcribre audio


def transcribe_audio(filename):
	"Takes a .wav format audio file and transcribes it to text."

	# Setup a recognizer instance

	recognizer = sr.Recognizer()




	# Import the audio file and convert to audio data

	audio_file = sr.AudioFile(filename)

	with audio_file as source:
		audio_data = recognizer.record(audio_file)


	# Return the transcribed text

	return recognizer.recognize_google(audio_data)


	transcribe_audio("acme_audio_files/call_1.wav")


	"""
	Setting up helper  functions like this at the start of a project

	may seem time-consuming but they'll help save time in the long run

	
	Once you've got these ready to go, you'll be able to use some of your natural language processing skills on the transcribed text

	"""


"""
Converting audio to the right format
Acme Studios have asked you to do a proof of concept to find out more about their audio files.

After exploring them briefly, you find there's a few calls but they're in the wrong file format for transcription.

As you'll be interacting with many audio files, you decide to begin by creating some helper functions.

The first one, convert_to_wav(filename) takes a file path and uses PyDub to convert it from a non-wav format to .wav format.

Once it's built, we'll use the function to convert Acme's first call, call_1.mp3, from .mp3 format to .wav.

PyDub's AudioSegment class has already been imported. Remember, to work with non-wav files, you'll need ffmpeg.


"""





"""
example:

"""


# Create function to convert audio file to wav
def convert_to_wav(filename):
  """Takes an audio file of non .wav format and converts to .wav"""
  # Import audio file
  audio = AudioSegment.from_file(filename)
  
  # Create new filename
  new_filename = filename.split(".")[0] + ".wav"
  
  # Export file as .wav
  audio.export(new_filename, format="wav")
  print(f"Converting {filename} to {new_filename}...")
 
# Test the function
convert_to_wav("call_1.mp3")



"""Finding PyDub stats
You decide it'll be helpful to know the audio attributes of any given file easily. This will be especially helpful for finding out how many channels an audio file has or if the frame rate is adequate for transcription.

In this exercise, we'll create show_pydub_stats() which takes a filename of an audio file as input. It then imports the audio as a PyDub AudioSegment instance and prints attributes such as number of channels, length and more.

It then returns the AudioSegment instance so it can be used later on.

We'll use our function on the newly converted .wav file, call_1.wav

AudioSegment has already imported from PyDub."""


def show_pydub_stats(filename):
  """Returns different audio attributes related to an audio file."""
  # Create AudioSegment instance
  audio_segment = AudioSegment.from_file(filename)
  
  # Print audio attributes and return AudioSegment instance
  print(f"Channels: {audio_segment.channels}")
  print(f"Sample width: {audio_segment.sample_width}")
  print(f"Frame rate (sample rate): {audio_segment.frame_rate}")
  print(f"Frame width: {audio_segment.frame_width}")
  print(f"Length (ms): {len(audio_segment)}")
  return audio_segment

# Try the function
call_1_audio_segment = show_pydub_stats("call_1.wav")






"""
Transcribing audio with one line
Alright, now you've got functions to convert audio files and find out their attributes, it's time to build one to transcribe them.

In this exercise, you'll build transcribe_audio() which takes a filename as input, imports the filename using speech_recognition's AudioFile class and then transcribes it using recognize_google().

You've seen these functions before but now we'll put them together so they're accessible in a function.

To test it out, we'll transcribe Acme's first call, "call_1.wav".

speech_recognition has been imported as sr.

"""



def transcribe_audio(filename):
  """Takes a .wav format audio file and transcribes it to text."""
  # Setup a recognizer instance
  recognizer = sr.Recognizer()
  
  # Import the audio file and convert to audio data
  audio_file = sr.AudioFile(filename)
  with audio_file as source:
    audio_data = recognizer.record(source)
  
  # Return the transcribed text
  return recognizer.recognize_google(audio_data)

# Test the function
print(transcribe_audio("call_1.wav"))




"""
üsando todas las funciones creadas

"""

# Check the stats of new file
call_1 = show_pydub_stats("call_1.wav")

# Split call_1 to mono
call_1_split = call_1.split_to_mono()
print(len(call_1_split))
print(call_1_split[0].channels)
print(call_1_split[1].channels)

# Export channel 2 (the customer channel)
call_1_split[1].export("call_1_channel_2.wav",
                       format="wav")

# Transcribe the single channel
print(transcribe_audio("call_1_channel_2.wav"))







"""



Sentiment analysis on spoken language text


Now you've got some helper functions ready, it's time to start extacting information from the transcribed text

"""

"""
Your proposal to Acme Studios suggested sentiment analysis, the process to figuring out if text if positive, neutral or negative, would be helpful and they agreed.

Knowing the sentiment of different calls may help them figure out where customers are having the most trouble.



To do sentiment analysis, you decide on using the NLTK Python library


to begin, you install NLTK using pip.

Then you download the necessary NLTK packages for sentiment analysis, punkt and vader lexicon using NLTK's donwload function



pip install nltk

# Download requiered NLTK packages


import nltk

nltk.download("punkt")
nltk.download("vader_lexicon")

Since we don't have a large enough dataset to train our own sentimen analysis model, we'll use NLTKs VADER or Valance Aware Dictionary and sentiment analyzer as it has pretrained sentiment analysis model in it


VADER works by analyzin each word in a pice of text of text and giving it a sentiment score. It was pretrained on social media text passages but will lend itself well for our proof of concepts

"""


"""
Sentiment analysis with VADER

"""


# Import sentiment analysis class

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create sentiment analysis instance

sid = SentimentIntensityAnalyzer()

# Test sentiment analysis on negative text

print(sid.polarity_scores("This customer service is terrible."))

# Running the function will return four values

{'neg': 0.437, 'neu': 0.563, 'pos':0.0, 'compound': -0.4767}


# neg-- negative, neu--- neutral, pos---positive and compound --- as on overall


"""
You try out the sentiment analysis on one of your transcribed phone calls using only the customer channel






"""

# Transcribe customer channel of call_3


call_3_channel_2_text = transcribe_audio("call_3_channel_2.wav")

print(call_3_channel_2_text)


# Sentiment analysis on customer channel of call_3


sid.polarity_scores(call_3_channel_2_text)

#{'neg': 0.0, 'neu': 0.892, 'pos': 0.108, 'compound': 0.4404}

# The sentiment is fairly neutral since the customer hasn't received their product yet.


"""
From your experience with sentiment anlysis, you know the sentiment can change sentence by sentence

but your current transcription function does'nt return sentences, only a large block of text


In your proposal, you mentioned this to Acme and they allocated budget for you to try a paid transcription API}


You try transcribing the same audio files using a paid API service and find it returns sentences

Using NLTK' sent tokenize, you break te transcription into sentences and analyze the sentiment sentence by sentence

"""



call_3_paid_api_text = "OKay. Yeah. Hi, Diane. This is paid on this call and obi........"
# Import sent tokenizer

from nltk.tokenize import sent_tokenize

# Find sentiment on each sentence

for sentence in sent_tokenize(call_3_paid_api_text):
	print(sentence)
	print(sid.polarity_scores(sentence))

# THis is helpful beause it allows you tu figure out which  parts of the conversation the customr may be most displeasd with



"""
Analyzing sentiment of a phone call
Once you've transcribed the text from an audio file, it's possible to perform natural language processing on the text.

In this exercise, we'll use NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) to analyze the sentiment of the transcribed text of call_2.wav.

To transcribe the text, we'll use the transcribe_audio() function we created earlier.

Once we have the text, we'll use NLTK's SentimentIntensityAnalyzer() class to obtain a sentiment polarity score.

.polarity_scores(text) returns a value for pos (positive), neu (neutral), neg (negative) and compound. Compound is a mixture of the other three values. The higher it is, the more positive the text. Lower means more negative.

"""


"""





"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create SentimentIntensityAnalyzer instance
sid = SentimentIntensityAnalyzer()

# Let's try it on one of our phone calls
call_2_text = transcribe_audio("call_2.wav")

# Display text and sentiment polarity scores
print(call_2_text)
print(sid.polarity_scores(call_2_text))


"""
Sentiment analysis on formatted text
In this exercise, you'll calculate the sentiment on the customer channel of call_2.wav.

You've split the customer channel and saved it to call_2_channel_2.wav.

But from your experience with sentiment analysis, you know it can change sentence to sentence.

To calculate it sentence to sentence, you split the split using NLTK's sent_tokenize() module.

But transcribe_audio() doesn't return sentences. To try sentiment anaylsis with sentences, you've tried a paid API service to get call_2_channel_2_paid_api_text which has sentences.
"""


from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create SentimentIntensityAnalyzer instance
sid = SentimentIntensityAnalyzer()

# Let's try it on one of our phone calls
call_2_text = transcribe_audio("call_2.wav")

# Display text and sentiment polarity scores
print(call_2_text)
print(sid.polarity_scores(call_2_text))



"""
Sentiment analysis on formatted text
In this exercise, you'll calculate the sentiment on the customer channel of call_2.wav.

You've split the customer channel and saved it to call_2_channel_2.wav.

But from your experience with sentiment analysis, you know it can change sentence to sentence.

To calculate it sentence to sentence, you split the split using NLTK's sent_tokenize() module.

But transcribe_audio() doesn't return sentences. To try sentiment anaylsis with sentences, you've tried a paid API service to get call_2_channel_2_paid_api_text which has sentences.

"""


# Import sent_tokenize from nltk
from nltk import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create SentimentIntensityAnalyzer instance
sid = SentimentIntensityAnalyzer()
print(call_2_channel_2_paid_api_text)
# Split channel 2 paid text into sentences and score each
for sentence in sent_tokenize(call_2_channel_2_paid_api_text):
    print(sentence)
    print(sid.polarity_scores(sentence))







"""

Named entity recognition on transcribed text
Spoken language  processing in Python




Now you've done some sentiment analysis on Acme's transcribed

yo decide named entity recognition is a good next step


Entity recognition is the process of extracting objects of interest from text 

to do this, you turn to spaCy, the natural language processing library


to get started with spaCy you can instal it using pip

pip install spacy

# Download spaCy language model

python -m spacy download en_core_web_sm


Spacy works by turning blocks of text into docs

Docs are made up of tokens and spans

you can think of tokens as individual words and groups of tokens or sentences as spans.

to create a spacy doc, we pass the string of text we want to use to NLP

Now we've got a spacy doc, we van use Spacy built-int features to find out more

You can see what tokens a doc contains and the index where they start using dot text and dot idx on objects in your doc

"""


# Show different tokens and positions

for token in doc:
	print(token.text, token.idx)




"""
You can see where the sentences are with dot sents.

# Show sentences in doc



"""

for sentences in doc.sents:
	print(sentence)

"""
SpaCy named entities

Some of spaCy's built-in named entities:


* PERSON People, including fictional.


* ORG Companies, agencies, intitutions, etc

* GPE Countries, cities, states.

* PRODUCT Objects, vehicles, food, etc(Not services)

* DATE Absolute or relative dates or periods.

* TIME TImes smaller than a day

* MONEY Monetary values, including unit.

* CARDINAL Numerals that do not fall under another type
"""


# FInd named entities in doc


for entity in doc.ents:
	print(entity.text, entity.label_)

"""

Custom named entities



puedo crear mis propiaas


# import EntityRuler class

from spacy.pipeline import EntityRuler


A pipeline is what spaCy uses to parse text into a doc


you can see the current pipeline you're using by calling pipeline on nlp.


# check spaCy pipeline

print(nlp.pipeline)



[('tagger', <spacy.pipelines.pipes.Tagger>),
 ('parser',...),
 ('ner', ...)]


The entityRuler class allows us to create another step in the pipeline



# Create EntityRuler instance

ruler = EntityRuler(nlp)


# Add token pattern to ruler

ruler.add_patterns([{"label":"PRODUCT", "pattern": "smartphone"}])


# Add new rule to pipeline before ner

nlp.add_pipe(ruler, before="ner")


# check updated pipeline

nlp.pipeline
"""


"""
Named entity recognition in spaCy
Named entities are real-world objects which have names, such as, cities, people, dates or times. We can use spaCy to find named entities in our transcribed text.

In this exercise, you'll transcribe call_4_channel_2.wav using transcribe_audio() and then use spaCy's language model, en_core_web_sm to convert the transcribed text to a spaCy doc.

Transforming text to a spaCy doc allows us to leverage spaCy's built-in features for analyzing text, such as, .text for tokens (single words), .sents for sentences and .ents for named entities.

"""



# Transcribe call 4 channel 2
call_4_channel_2_text = transcribe_audio("call_4_channel_2.wav")

# Create a spaCy language model instance
nlp = spacy.load("en_core_web_sm")

# Create a spaCy doc with call 4 channel 2 text
doc = nlp(call_4_channel_2_text)

# Check the type of do


"""
Named entity recognition in spaCy
Named entities are real-world objects which have names, such as, cities, people, dates or times. We can use spaCy to find named entities in our transcribed text.

In this exercise, you'll transcribe call_4_channel_2.wav using transcribe_audio() and then use spaCy's language model, en_core_web_sm to convert the transcribed text to a spaCy doc.

Transforming text to a spaCy doc allows us to leverage spaCy's built-in features for analyzing text, such as, .text for tokens (single words), .sents for sentences and .ents for named entities.


"""

import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Create a spaCy doc with call 4 channel 2 text
doc = nlp(call_4_channel_2_text)

# Show tokens in doc
for token in doc:
    print(token.text, token.idx)


    import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Create a spaCy doc with call 4 channel 2 text
doc = nlp(call_4_channel_2_text)

# Show sentences in doc
for sentence in doc.sents:
    print(sentence)



    import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Create a spaCy doc with call 4 channel 2 text
doc = nlp(call_4_channel_2_text)

# Show named entities and their labels
for entity in doc.ents:
    print(entity.text, entity.label_)




 """
	Creating a custom named entity in spaCy
If spaCy's built-in named entities aren't enough, you can make your own using spaCy's EntityRuler() class.

EntityRuler() allows you to create your own entities to add to a spaCy pipeline.

You start by creating an instance of EntityRuler() and passing it the current pipeline, nlp.

You can then call add_patterns() on the instance and pass it a dictionary of the text pattern you'd like to label with an entity.

Once you've setup a pattern you can add it the nlp pipeline using add_pipe().

Since Acme is a technology company, you decide to tag the pattern "smartphone" with the "PRODUCT" entity tag.

spaCy has been imported and a doc already exists containing the transcribed text from call_4_channel_2.wav.

 """

 # Create EntityRuler instance
ruler = EntityRuler(nlp)

# Define pattern for new entity
ruler.add_patterns([{"label": "PRODUCT", "pattern":"smartphone"}])

# Update existing pipeline
nlp.add_pipe(ruler, before="ner")

# Test new entity
for entity in doc.ents:
  print(entity.text, entity.label_)


















  """
Classifying transcribed speech

with Sklearn

'Acme are impressed with your work so far and have sent over two folders full of phone call audio snippets'
  
And they've manually labelled them with pre-purchase if the customer was calling before a purchase o post-purchase if the customer was calling after making a purchase.
  

They said the process of labeling audio files was labor intensive and wanto to know if machine learning can help
  
You inmediately start to think of building an sklearn text classifier, and that's what we'll be doing in this lesson


# Inspect post purchase audio folder
  """


import os 

post_purchase_audio = os.listdir("post_purchase")

print(post_purchase_audio[:5])


#  yo notice there's about 50 files in each but they're in the mp3 format, luckily you build a function to handle this earlier

"""



Using your convert_to_wav function you built earlier, you convert all the files from mp3 to wav 


























"""

# Loop through mp3 files

for file in post_purchase_audio:
	print(f"Converting {file} to .wav....")

	# Use previously made function to conver to .wav

	convert_to_wav(file)


	"""
	ahora crearemos una nueva funcion  'create_text_list, to transcribe all of the files in a folder to text


	'

	"""

def create_text_list(folder):
	text_list = []
	# Loop through folder

	for file in folder:
		# check for .wav  extension
		if file.endswith(".wav"):
			# Transcribe audio
			text = transcribe_audio(file)
			text_list.append(text)

		return text_list
		
		


"""
Transcribing all phone call excerpts

"""

# Convert post purchase audio to text

post_purchase_text = create_text_list(post_purchase_audio)

print(post_purchase_text[:5])


# to make building your text classifier easier, you decide to put all the text into a pandas dataframe.


import pandas as pd

# Create post purchase dataframe


post_purchase_df = pd.DataFrame({"label": "post_purchase", "text": post_purchase_text})


# Create pre purchase dataframe

pre_purchase_df = pd.DataFrame({"label:" "pre_purchase", "text:" pre_purchase_text})

"""
And to have everything in on place, you combine two dataframes with pd.concat
"""

# Combine pre purchase and post purchase


df = pd.concat([post_purchase_df, pre_purchase_df])

# View th combineed dataframe


df.head()


"""
Now  you've got your data in a dataframe, you can use it to build a text classifier with Sklearn



We'll start by importanting the necessary packages

# Import text classification packages




"""

import numpy as np 

from sklearn.pipeline import Pipeline

from sklearn.naive_bayes import MultinomialNB

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sklearn.model_selection import train_test_split

# Split data into train and test sets


X_train, X_test, y_train, y_test = train_test_split(
	X = df["text"],
	y = df["label"],
	test_size = 0.3)												
	
# Naive Bayes Pipeline

# Create text classifier pipeline

text_classfier = Pipeline([("vectorizer", CountVectorizer()),
	("tfidf", TfidfTransformer()),
	("classifier", MultinomialNB())

	])


# Fit the classifier pipeline on the training data


text_classifier.fit(X_train, y_train)


# Not so Naive

predictions = text_classifier.predict(X_test)


accuracy = 100 * np.mean(predictions == y_test.label)

print(f"The model is {accuracy:.2f}% accurate")




"""

Preparing audio files for text classification
Acme are very impressed with your work so far. So they've sent over two more folders of audio files.

One folder is called pre_purchase and contains audio snippets from customers who are pre-purchase, like pre_purchase_audio_25.mp3.

And the other is called post_purchase and contains audio snippets from customers who have made a purchase (post-purchase), like post_purchase_audio_27.mp3.

Upon inspecting the files you find there's about 50 in each and they're in the .mp3 format.

Acme want to know if you can build a classifier to classify future calls. You tell them you sure can.

So in this exercise, you'll go through each folder and convert the audio files to .wav format using convert_to_wav() so you can transcribe them.

"""

# Convert post purchase
for file in post_purchase:
    print(f"Converting {file} to .wav...")
    convert_to_wav(file)

# Convert pre purchase
for file in pre_purchase:
    print(f"Converting {file} to .wav...")
    convert_to_wav(file)



 """
Transcribing phone call excerpts
In this exercise, we'll transcribe the audio files we converted to .wav format to text using transcribe_audio().

Since there's lots of them and there could be more, we'll build a function create_test_list() which takes a list of filenames of audio files as input and goes through each file transcribing the text.

create_test_list() uses our transcribe_audio() function we created earlier and returns a list of strings containing the transcribed text from each audio file.

pre_purchase_wav_files and post_purchase_wav_files are lists of audio snippet filenames.


 """

def create_text_list(folder):
  # Create empty list
  text_list = []
  
  # Go through each file
  for file in folder:
    # Make sure the file is .wav
    if file.endswith(".wav"):
      print(f"Transcribing file: {file}...")
      
      # Transcribe audio and append text to list
      text_list.append(transcribe_audio(file))   
  return text_list

create_text_list(folder)



"""


"""

# Transcribe post and pre purchase text
post_purchase_text = create_text_list(post_purchase_wav_files)
pre_purchase_text = create_text_list(pre_purchase_wav_files)

# Inspect the first transcription of post purchase
print(post_purchase_text[0])




"""
Organizing transcribed phone call data
We're almost ready to build a text classifier. But right now, all of our transcribed text data is in two lists, pre_purchase_text and post_purchase_text.

To organize it better for building a text classifier as well as for future use, we'll put it together into a pandas DataFrame.

To start we'll import pandas as pd then we'll create a post purchase dataframe, post_purchase_df using pd.DataFrame().

We'll pass pd.DataFrame() a dictionary containing a "label" key with a value of "post_purchase" and a "text" key with a value of our post_purchase_text list.

We'll do the same for pre_purchase_df except with pre_purchase_text.

To have all the data in one place, we'll use pd.concat() and pass it the pre and post purchase DataFrames.


"""



import pandas as pd

# Make dataframes with the text
post_purchase_df = pd.DataFrame({"label": "post_purchase",
                                 "text": post_purchase_text})
pre_purchase_df = pd.DataFrame({"label": "pre_purchase",
                                "text": pre_purchase_text})

# Combine DataFrames
df = pd.concat([post_purchase_df, pre_purchase_df])

# Print the combined DataFrame
print(df.head())



"""
Create a spoken language text classifier
Now you've transcribed some customer call audio data, we'll build a model to classify whether the text from the customer call is pre_purchase or post_purchase.

We've got 45 examples of pre_purchase calls and 57 examples of post_purchase calls.

The data the model will train on is stored in train_df and the data the model will predict on is stored in test_df.

Try printing the .head() of each of these to the console.

We'll build an sklearn pipeline using CountVectorizer() and TfidfTransformer() to convert our text samples to numbers and then use a MultinomialNB() classifier to learn what category each sample belongs to.

This model will work well on our small example here but for larger amounts of text, you may want to consider something more sophisticated.

"""


# Build the text_classifier as an sklearn pipeline
text_classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])

# Fit the classifier pipeline on the training data
text_classifier.fit(train_df.text, train_df.label)







# Build the text_classifier as an sklearn pipeline
text_classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])

# Fit the classifier pipeline on the training data
text_classifier.fit(train_df.text, train_df.label)

# Evaluate the MultinomialNB model
predicted = text_classifier.predict(test_df.text)
accuracy = 100 * np.mean(predicted == test_df.label )
print(f'The model is {accuracy}% accurate')