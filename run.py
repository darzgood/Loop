import sound_recorder as sr
import sound_player as sp

if (__name__ == "__main__"):
    sr.record();
    sp.play_wav("file.wav")
