import os
from pydub import AudioSegment

input_dir = 'raw_audio'
output_dir = 'processed'


os.makedirs(output_dir, exist_ok=True)

audio_files = sorted(os.listdir(input_dir))

audio_groups = {}

for file in audio_files:
    if file.endswith('.mp3'):
        prefix1 = file.split('-')[0] 
        prefix2 = file.split('-')[1]
        prefix = prefix1 + '-' + prefix2[:3]
        #prefix = '-'.join(file.split('-')[:2])
        if prefix not in audio_groups:
            audio_groups[prefix] = []
        audio_groups[prefix].append(file)
# Debugging: Print the grouped files
print("Grouped files by prefix:")
for prefix, files in audio_groups.items():
    print(f"{prefix}: {files}")

def concatenate_audio(files, output_file):
    """
    Concatenates a list of audio files into a single audio file.

    Parameters:
    files (list): List of audio file names to concatenate.
    output_file (str): The name of the output concatenated audio file.

    Returns:
    None
    """
    combined = AudioSegment.empty()
    for file in files:
        file_path = os.path.join(input_dir, file)
        print(f"Processing file: {file_path}")  # Debug print to show the current file being processed
        audio = AudioSegment.from_mp3(file_path)
        combined += audio
    output_path = os.path.join(output_dir, output_file)
    combined.export(output_path, format='mp3')
    print(f"Exported concatenated file to: {output_path}")  # Debug print to show the export location

# Process each group and concatenate the files
for prefix, files in audio_groups.items():
    # Create a single output file name based on the prefix
    output_file = f"{prefix}-AR.mp3"
    # Concatenate the audio files in the group
    concatenate_audio(files, output_file)

print("Audio files concatenated successfully.")