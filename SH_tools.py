def noteplayer(note,octave = 4):
    from playsound import playsound
    import numpy as np
    import simpleaudio as sa
    import pandas as pd
    
    note_oct_freq = pd.read_csv('./Datasets/Notes_and_freq.csv')
    frequency = note_oct_freq['Frequency (Hz)'][(note_oct_freq['Note']==note) & 
                                                (note_oct_freq["Octave"]==octave)].iloc[0]
    print(frequency)

    #frequency = note  # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = 0.5  # Note duration of 3 seconds

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    play_obj.wait_done()
