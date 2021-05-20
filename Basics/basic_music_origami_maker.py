# -*- coding: utf-8 -*-
"""Basic_Music_Origami_Maker.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19OWZC3lT2jCzpnmvyJf6tHweqn42PmuW

# Basic_Music Origami Maker (ver. 1.0)

## Simple, yet powerful MIDI flipper and/or folder

***

### Full deca-octave MIDI transformations and bulk processing support

***

### Powered by TMIDI 2.2 Optimus Processors

***

#### Project Los Angeles

#### Tegridy Code 2021

***

# Setup environment
"""

#@title Install tegridy-tools
!git clone https://github.com/asigalov61/tegridy-tools

#@title Import all needed modules

print('Loading needed modules. Please wait...')
import os
import copy

if not os.path.exists('/content/Dataset'):
    os.makedirs('/content/Dataset')

if not os.path.exists('/content/Output'):
    os.makedirs('/content/Output')

os.chdir('/content/tegridy-tools/tegridy-tools')
import TMIDI

import tqdm
from tqdm import auto

os.chdir('/content/')
print('Loading complete. Enjoy! :)')

"""# Download a Sample MIDI Dataset"""

# Commented out IPython magic to ensure Python compatibility.
#@title Download special Tegridy Piano MIDI dataset (Recommended)

#@markdown Works best stand-alone/as-is for the optimal results
# %cd /content/Dataset/

!wget 'https://github.com/asigalov61/Tegridy-MIDI-Dataset/raw/master/Tegridy-Piano-CC-BY-NC-SA.zip'
!unzip -j '/content/Dataset/Tegridy-Piano-CC-BY-NC-SA.zip'
!rm '/content/Dataset/Tegridy-Piano-CC-BY-NC-SA.zip'

# %cd /content/

"""# Create Musical Origami"""

#@title Run this code to transform your midis

#@markdown NOTES:

#@markdown 0) Files will be written to the "./Output" dir

#@markdown 1) Dataset MIDI file names are used as song names. Feel free to change it to anything you like.

#@markdown 2) Best results are achieved with the single-track, single-channel, single-instrument MIDI 0 files with plain English names (avoid special or sys/foreign chars)

#@markdown 3) MIDI Channel = -1 means all MIDI channels except drums. MIDI Channel = 16 means all channels will be processed. Otherwise, only single indicated MIDI channel will be processed.

desired_MIDI_channel_to_process = 16 #@param {type:"slider", min:-1, max:16, step:1}

flip_only = False #@param {type:"boolean"}

fold_and_flip = False #@param {type:"boolean"}

flip_octave_10 = True #@param {type:"boolean"}
flip_octave_9 = True #@param {type:"boolean"}
flip_octave_8 = True #@param {type:"boolean"}
flip_octave_7 = True #@param {type:"boolean"}
flip_octave_6 = True #@param {type:"boolean"}
flip_octave_5 = True #@param {type:"boolean"}
flip_octave_4 = True #@param {type:"boolean"}
flip_octave_3 = True #@param {type:"boolean"}
flip_octave_2 = True #@param {type:"boolean"}
flip_octave_1 = True #@param {type:"boolean"}

transpose_by_this_number_of_pitches = 0 #@param {type:"slider", min:-30, max:30, step:1}
split_transposition = False #@param {type:"boolean"}

simulate_velocity = True #@param {type:"boolean"}
number_of_ticks_per_quarter = 400 #@param {type:"slider", min:10, max:500, step:10}


encode_velocities = True 
encode_MIDI_channels = True
chordify_input_MIDIs = False
melody_conditioned_chords = True
melody_pitch_baseline = 60
time_denominator = 1
chars_encoding_offset = 33

print('TMIDI Optimus MIDI Processor')
print('Starting up...')
###########

average_note_pitch = 0
min_note = 127
max_note = 0

files_count = 0

TXT = ''
melody = []
chords = []

###########

print('Loading MIDI files...')
print('This may take a while on a large dataset in particular.')

dataset_addr = "/content/Dataset/"
os.chdir(dataset_addr)
filez = os.listdir(dataset_addr)

print('Processing MIDI files. Please wait...')
for f in tqdm.auto.tqdm(filez):
  try:
    fn = os.path.basename(f)
    fn1 = fn.split('.')[0]

    files_count += 1
    TXT, melody, chords = TMIDI.Optimus_MIDI_TXT_Processor(f, chordify_TXT=chordify_input_MIDIs, output_MIDI_channels=encode_MIDI_channels, char_offset=chars_encoding_offset, dataset_MIDI_events_time_denominator=time_denominator, output_velocity=encode_velocities, MIDI_channel=desired_MIDI_channel_to_process, MIDI_patch=range(0, 127), melody_conditioned_encoding=melody_conditioned_chords, melody_pitch_baseline=melody_pitch_baseline, number_of_notes_to_sample=-1)
    
    output = []

    for c in chords:
      for n in c:
        octave = int(n[4] / 12) - 1
        nn = copy.deepcopy(n)
        nn[3] = octave

        output.append(nn)
    
    out = []
    
    for o in output:
      oo = copy.deepcopy(o)
      
      oo[4] = o[4] + transpose_by_this_number_of_pitches 

      if o[4] >= 1:
        if flip_octave_1:
          oo[4] = 12 - o[4] + transpose_by_this_number_of_pitches 

      if o[4] >= 12:
        if flip_octave_2:
          oo[4] = 24 - o[4] + 12 + transpose_by_this_number_of_pitches

      if o[4] >= 24:
        if flip_octave_3:
          oo[4] = 36 - o[4] + 24 + transpose_by_this_number_of_pitches
      
      if o[4] >= 36:
        if flip_octave_4:
          oo[4] = 48 - o[4] + 36 + transpose_by_this_number_of_pitches
           
      if o[4] >= 48:
        if flip_octave_5:
          oo[4] = 60 - o[4] + 48 + transpose_by_this_number_of_pitches
      
      if o[4] >= 60:
        if flip_octave_6:
          oo[4] = 72 - o[4] + 60 + transpose_by_this_number_of_pitches
    
      if o[4] >= 72:
        if flip_octave_7:
          oo[4] = 84 - o[4] + 72 + transpose_by_this_number_of_pitches
      
      if o[4] >= 84:
        if flip_octave_8:
          oo[4] = 96 - o[4] + 84 + transpose_by_this_number_of_pitches
      
      if o[4] >= 96:
        if flip_octave_9:
          oo[4] = 108 - o[4] + 96 + transpose_by_this_number_of_pitches
      
      if o[4] >= 108:
        if flip_octave_10:
          oo[4] = 120 - o[4] + 108 + transpose_by_this_number_of_pitches 

      if fold_and_flip:
        if o[4] >= 60:
          oo[4] = 120 - o[4] + 30 + transpose_by_this_number_of_pitches
        else:
          oo[4] = 60 - o[4] + 30 + transpose_by_this_number_of_pitches

      if flip_only:
          oo[4] = 120 - o[4] + transpose_by_this_number_of_pitches
      
      if split_transposition:
        if o[4] < 60:
          oo[4] = o[4] + 30
        else:
          oo[4] = o[4] - 30

      if simulate_velocity:
        oo[5] = o[4]

      out.append(oo)


    song_name = 'Song: ' + fn1
    fname = '/content/Output/' + fn1

    output_signature = 'MIDI Flipper Folder'

    detailed_stats = TMIDI.Tegridy_SONG_to_MIDI_Converter(out,
                                                          output_signature = output_signature,  
                                                          output_file_name = fname, 
                                                          track_name=song_name, 
                                                          number_of_ticks_per_quarter=number_of_ticks_per_quarter,
                                                          list_of_MIDI_patches=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,])
  except KeyboardInterrupt:
    print('Saving current progress and quitting...')
    break  
  
  except:
    print('Bad MIDI:', f)
    continue

print('Task complete :)')
print('==================================================')
print('Number of processed dataset MIDI files:', files_count)
print('==================================================')
print('Done! Enjoy! :)')

"""# Congrats! You did it! :)"""