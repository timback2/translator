SOURCE_FILE ?= "input/russian.txt"
language ?= "russian"

all: create_temp_folder generate_audio_file translate_audio rename_output_file clean
	
create_temp_folder:
	- $(eval TMP := $(shell mktemp -d))

generate_audio_file:
	python src/generate_audio_file.py --input $(SOURCE_FILE) --output $(TMP)/audio.mp3

translate_audio:
# TODO: Handle audio generation failure
	if [ -a $(TMP)/audio.mp3 ] ; \
	then \
		whisper  -o output/ --task translate --model large $(TMP)/audio.mp3; \
	fi;

rename_output_file:
	if [ -a output/audio.mp3.txt ] ; \
	then \
		mv output/audio.mp3.txt translated/$(shell basename $(SOURCE_FILE)); \
	fi;				

clean: 
	rm -rf $(TMP)

process_files:
	echo "Called process_files with $(language) language"
