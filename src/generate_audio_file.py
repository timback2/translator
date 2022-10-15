import time
from gtts import gTTS
import argparse


def generate_audio_file(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print("Generated audio file " + filename)

def get_file_contents(filename):
    with open(filename) as f:
        return f.read()

if __name__ == '__main__':
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='input/data.txt', help='Path to the input data file.')
    parser.add_argument('--output', type=str, default='output/audio.mp3', help='Path to the output audio directory.')
    args = parser.parse_args()


    # Generate the audio files
    generate_audio_file(get_file_contents(args.input), args.output)


    # Print the time taken
    print(f'Time taken: {time.time() - start_time:.2f} seconds')