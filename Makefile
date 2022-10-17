SOURCE_FILE ?= "input/russian.txt"

all: create_temp_folder generate_audio_file translate_audio clean
	
create_temp_folder:
	- $(eval TMP := $(shell mktemp -d))

generate_audio_file:
	python src/generate_audio_file.py --input $(SOURCE_FILE) --output $(TMP)/output.mp3

translate_audio:
# TODO: Handle audio generation failure
	whisper  -o output/ --task translate --model large $(TMP)/output.mp3

clean: 
	rm -rf $(TMP)
