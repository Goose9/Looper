#import RPi.GPIO as GPIO
import time
import sys
import wave
from Pedal import Pedal

from multiprocessing import Process

import pyaudio

# global variables simulate foot pedals
rec_playback = True
record = False
playback = True
save = False


def inputThread(queue):
    timer = time.time()
    while 1:
        # TODO interrupt when sequencer pressed (http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio)
        #input = GPIO.input()
        queue.put(input)
        if timer - time.time() < 0.5:
            #TODO notice double tap and long tap
            pass


def firstTap():
    # TODO record
    pass


def furtherTap():
    # TODO record + play
    pass


def doubleTap(first):
    # TODO first=true -> stop recording + keep playing
    # TODO first=false -> firstTap() + keep playing
    pass


def longTap():
    # TODO stop
    pass


def testRecording(file_name, channels, format, rate, chunk):
    print("test recording...")
    audio = pyaudio.PyAudio()
    rec_length = 5
    frames = []

    stream = audio.open(format=format, channels=channels,
                        rate=rate, input=True,
                        frames_per_buffer=chunk)

    print("recording...")
    for i in range(0, int(rate / chunk * rec_length)):
        data = stream.read(chunk)
        frames.append(data)
    print "finished recording"

    stream.stop_stream()
    stream.close()

    writeSoundToFile(file_name, channels, format, rate, frames, audio)
    return


def writeSoundToFile(file_name, channels, format, rate, frames, audio):
    waveFile = wave.open(file_name, 'wb')
    waveFile.setnchannels(channels)
    waveFile.setsampwidth(audio.get_sample_size(format))
    waveFile.setframerate(rate)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


def testPlayback(file_name, chunk):
    audio = pyaudio.PyAudio()

    wf = wave.open(file_name, 'rb')

    print("playback...")
    # open stream based on the wave object which has been input.
    stream = audio.open(format=
                    audio.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data (based on the chunk size)
    data = wf.readframes(chunk)

    # play stream (looping from beginning of file to the end)
    while data != '':
        # writing to the stream is what *actually* plays the sound.
        stream.write(data)
        data = wf.readframes(chunk)

    # cleanup stuff.
    stream.close()
    audio.terminate()


def main():
    # TODO record while playback, overwrite same audio file
    # TODO record without playback, different audio files

    format = pyaudio.paInt16
    channels = 2
    rate = 44100
    chunk = 1024

    process_pedal_dict = dict()

    while(1):
        key = raw_input("Press 1, 2, 3 or 4 to simulate Pedal... ");
        if key == "1" or key == "2" or key == "3" or key == "4":
            if process_pedal_dict.has_key(key):
                pass
            else:
                pedal = Pedal()
                pedal.file_name = "pedal_" + key + ".wav"
                process_pedal_dict.update({key: pedal})

        # if (rec_playback or playback) and len(process_pedal_dict) > 0:
        #     new_process = Process(target=testPlayback, args=(process_pedal_dict[pedal], chunk))
        #     new_process.start()

        file = process_pedal_dict[key].file_path + process_pedal_dict[key].file_name

        if rec_playback or record:
            new_process = Process(target=testRecording, args=(file, channels, format, rate, chunk))
            new_process.start()
            new_process.join()

        if playback:
            new_process = Process(target=testPlayback, args=(file, chunk))
            new_process.start()


        # testRecording(file_name, channels, format, rate, audio, chunk)
        # testPlayback(file_name, audio, chunk)


if __name__== "__main__":
    main()