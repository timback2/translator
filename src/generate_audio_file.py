from gtts import gTTS
from langdetect import detect, DetectorFactory
import argparse
import time


def generate_audio_file(text, language, filename):
    tts = gTTS(text=text, lang=language)
    tts.save(filename)
    print("Generated audio file " + filename)


def get_file_contents(filename):
    with open(filename) as f:
        return f.read()


def detect_language(text):
    try:
        DetectorFactory.seed = 0
        return detect(text)

    except:
        return "unknown"


if __name__ == "__main__":
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=str,
        default="input/data.txt",
        help="Path to the input data file.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output/audio.mp3",
        help="Path to the output audio directory.",
    )
    args = parser.parse_args()

    text = get_file_contents(args.input)
    language = detect_language(text)
    if language == "en":
        print("Detected language is English. Skipping audio generation.")
    elif language != 'unknown':
    # Generate the audio files
        print("Detected language: " + language)
        generate_audio_file(text, language, args.output)
    else:
        print("Language not detected")

    # Print the time taken
    print(f"Time taken: {time.time() - start_time:.2f} seconds")
