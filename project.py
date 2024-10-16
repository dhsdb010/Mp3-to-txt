'''mp3 to txt'''
import whisper
import sys

def get_path(path):
    if path.endswith(".mp3"):
        return path
    else:
        sys.exit("Invalid file format. Please choose a .mp3 file.")

def set_filename(filename):
    return filename + ".txt"


def main():
    model = whisper.load_model("base")
    path = get_path(input("mp3 file path : "))
    result = model.transcribe(path)
    filename = set_filename(input("Output file name : "))
    with open(filename, "w") as f:
        f.write(result["text"])


if __name__ == "__main__":
    main()
