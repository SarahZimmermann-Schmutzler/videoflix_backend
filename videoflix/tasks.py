import subprocess

def convert_480p(source):
    new_file_name = source + '_480p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, new_file_name)
    subprocess.run(cmd, capture_output=True)