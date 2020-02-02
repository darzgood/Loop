import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

def main(WAVE_OUTPUT_FILENAME = WAVE_OUTPUT_FILENAME, RECORD_SECONDS=RECORD_SECONDS):
    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")


    # stop Recording
    stream.stop_stream()
    stream.close()

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

    # Close PyAudio.
    audio.terminate()

if __name__ == '__main__':
    main()
