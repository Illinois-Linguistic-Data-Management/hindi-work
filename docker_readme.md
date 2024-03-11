Usage:

1. Place input files files in a folder of your choice. These should be text files containing Hindi text written in Devanagari script.

2. Run the following command in the directory with the dockerfile and pos_tagging.py:

docker build -t hindi-tagger .

3. Enter the following, replacing <input_dir> and <output_dir> with the desired input/output directories:

docker run -v <output_dir>:/app/tagged_transcripts -v <input_dir>:/app/indicized_transcripts hindi-tagger

The command below is an example of what this looks like:

docker run -v /Users/viyathfernando/Documents/repos/hindi_tagger/tagged_transcripts:/app/tagged_transcripts -v /Users/viyathfernando/Documents/repos/hindi_tagger/indicized_transcripts:/app/indicized_transcripts hindi-tagger

