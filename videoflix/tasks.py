import subprocess

def convert_1080p(source):
    """
    converts uploaded video to 1080p
    """
    source_without_ending = source.replace('.mp4', '')
    converted_file_name = source_without_ending + '_1080p.mp4'
    # cmd = 'ffmpeg -i "{}" -s hd1080 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, converted_file_name)
    cmd = 'ffmpeg -i "{}" -s hd1080 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, converted_file_name)
    print(source_without_ending,converted_file_name,cmd)
    result = subprocess.run(cmd, shell=True, capture_output=True)
    
    if result.returncode != 0:
        print("Fehler bei FFmpeg_1080p:", result.stderr)


def convert_720p(source):
    """
    converts uploaded video to 720p
    """
    source_without_ending = source.replace('.mp4', '')
    converted_file_name = source_without_ending + '_720p.mp4'
    # cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, converted_file_name)
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, converted_file_name)
    print(source_without_ending,converted_file_name,cmd)
    result = subprocess.run(cmd, shell=True, capture_output=True)
    
    if result.returncode != 0:
        print("Fehler bei FFmpeg_720p:", result.stderr)


def convert_480p(source):
    """
    converts uploaded video to 480p
    """
    source_without_ending = source.replace('.mp4', '')
    converted_file_name = source_without_ending + '_480p.mp4'
    # cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, converted_file_name)
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, converted_file_name)
    print(source_without_ending,converted_file_name,cmd)
    result = subprocess.run(cmd, shell=True, capture_output=True)

    if result.returncode != 0:
        print("Fehler bei FFmpeg_480p:", result.stderr)