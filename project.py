'''mp3 to txt'''
import whisper
import sys
from datetime import datetime

def get_path(path):
    if path.endswith(".mp3"):
        return path
    else:
        sys.exit("Invalid file format. Please choose a .mp3 file.")

def set_filename(filename):
    return filename + ".txt"

def get_time():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    return formatted_date


def main():
    model = whisper.load_model("base")
    path = get_path(input("mp3 file path : "))
    result = model.transcribe(path)
    filename = set_filename(input("Output file name : "))
    time = get_time()
    with open(time + filename, "w") as f:
        f.write(result["text"])


if __name__ == "__main__":
    main()
