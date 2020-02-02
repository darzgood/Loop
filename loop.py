# loop.py

from tkinter import *
import pyaudio
import audio

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

isRecording = False

master = Tk()

audioTracks = []

pa = pyaudio.PyAudio()

def record():
    audioTracks.append(startRecord(pa))

def loop():
    audio.play(pa, audioTracks[-1])


def main():

    recordButton = Button(master, text="Record", command=record)
    recordButton.pack()

    stopButton = Button(master, text="Stop", command=stopRecord)
    stopButton.pack()

    loopButton = Button(master, text="Loop", command=loop)
    loopButton.pack()

    mainloop()
    # Close PyAudio.
    pa.terminate()

def startRecord(pa, RECORD_SECONDS=RECORD_SECONDS):
    isRecording = True;
    audio = pa

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("recording...")
    frames = []

    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #     data = stream.read(CHUNK)
    #     frames.append(data)
    # print("finished recording")
    while isRecording:
        data = stream.read(CHUNK)
        frames.append(data)
        yield frames



    # stop Recording
    stream.stop_stream()
    stream.close()

    yield frames

def stopRecord():
    isRecording = False


def play(pa, frames):

    audio = pa
    # Open playback stream.
    stream = audio.open(format=FORMAT,
        channels=CHANNELS,
        rate=RATE,output=True)

    for frame in frames:
        stream.write(frame)
    # data = wf.readframes(chunk_size)
    # while len(data) > 0:
    #     stream.write(data)
    #     data = wf.readframes(chunk_size)

    # Stop stream.
    stream.stop_stream()
    stream.close()


if __name__ == '__main__':
    main()
