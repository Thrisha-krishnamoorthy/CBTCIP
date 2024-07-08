import sounddevice as sd
import wavio

def record_voice(filename, duration, samplerate=44100):
    """
    Records audio for a given duration and saves it to a file.
    
    :param filename: The name of the file to save the audio to.
    :param duration: The duration of the recording in seconds.
    :param samplerate: The sampling rate of the recording (default is 44100 Hz).
    """
    print("Recording...")
    # Record audio
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")
    
    # Save the audio data as a WAV file
    wavio.write(filename, audio_data, samplerate, sampwidth=2)
    print(f"Audio saved as {filename}")

if __name__ == "__main__":
    filename = "recorded_audio.wav"
    duration = 5  # Duration of the recording in seconds
    record_voice(filename, duration)
