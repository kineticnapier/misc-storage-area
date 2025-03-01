import numpy as np
import scipy.io.wavfile as wav

def replace_strings_in_file(file_path, replacements, encode='utf-8'):
    """
    Reads a file, replaces specified strings, and writes back to the same file.
    
    :param file_path: Path to the file.
    :param replacements: Dictionary where keys are target strings and values are replacement strings.
    :param encode: Encoding to use when reading and writing files. Default is UTF-8.
    """

    # example usage
    #
    # file_path = "test.txt"
    # replacements = {
    #     "old_string": "new_string",
    #     "another_old_string": "another_new_string"
    # }
    # replace_strings_in_file(file_path, replacements)

    try:
        # Read the file content
        with open(file_path, 'r', encoding=encode) as file:
            content = file.read()
        
        # Perform the replacements
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding=encode) as file:
            file.write(content)
        
        print(f"Replacements completed successfully in {file_path}")
    except Exception as e:
        print(f"Error processing file: {e}")

def generate_sine_wave(frequency=440, duration=2, sample_rate=44100, filename="sine_wave.wav"):
    """
    Generate a sine wave of a given frequency and duration, and save it as a WAV file.
    
    :param frequency: Frequency of the sine wave in Hz
    :param duration: Duration of the sine wave in seconds
    :param sample_rate: Sampling rate in Hz
    :param filename: Output WAV file name
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # Time array
    waveform = 0.5 * np.sin(2 * np.pi * frequency * t)  # Generate sine wave
    
    # Convert to 16-bit PCM format
    waveform_int16 = np.int16(waveform * 32767)
    
    # Write to WAV file
    wav.write(filename, sample_rate, waveform_int16)
    print(f"Sine wave of {frequency} Hz saved as {filename}")

if __name__ == "__main__":
    generate_sine_wave(frequency=440)
    generate_sine_wave(frequency=880, filename="sine_wave_880Hz.wav")