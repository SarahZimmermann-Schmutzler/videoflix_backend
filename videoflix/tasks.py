import subprocess

# converts uploaded video to 1080p
def convert_1080p(source):
    source_without_ending = source.replace('.mp4', '')
    converted_file_name = source_without_ending + '_1080p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd1080 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, converted_file_name)
    # print(source_without_ending,converted_file_name,cmd)
    subprocess.run(cmd, capture_output=True)

# converts uploaded video to 720p
def convert_720p(source):
    source_without_ending = source.replace('.mp4', '')
    converted_file_name = source_without_ending + '_720p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, converted_file_name)
    # print(source_without_ending,converted_file_name,cmd)
    subprocess.run(cmd, capture_output=True)

# converts uploaded video to 480p
def convert_480p(source):
    source_without_ending = source.replace('.mp4', '')
    converted_file_name = source_without_ending + '_480p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, converted_file_name)
    # print(source_without_ending,converted_file_name,cmd)
    subprocess.run(cmd, capture_output=True)