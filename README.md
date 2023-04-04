
# Description

**this script helps begginer to play kalimba more easier by feeding the script the song note as text file and will print tab by tab or evern tell you which tab you shoud press**

  

# Dependencies

- colorama
- gtts
 by running the following command `pip install colorama gtts` before running the script or py passing `-i` flag when run the script

  

# Usage

`pyKalimba.py [-h] -p NOTE_PATH [-t INTERSPACE_TIME] [-m] [-i]`

enter your song note for kalimba playing

options:
  -h, --help            show this help message and exit
  -p NOTE_PATH, --note_path NOTE_PATH
                        Path of note text
  -t INTERSPACE_TIME, --interspace_time INTERSPACE_TIME
                        the separation time amonge tunes default value is 1.25 second
  -m, --mute            disable auto play
  -i, --install_dependancies
                        passing this flag means that you want to install gtts and colorama
 
 # Example
`py .\pyKalimba.py -p .\happy_birth_day.txt -t 1.25`