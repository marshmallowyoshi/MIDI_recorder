import os
from argparse import ArgumentParser

from midi_rec_service.record_loop import rec

def main():
    parser = ArgumentParser()
    parser.add_argument('-d', '--directory', help='Directory to save midi files in', metavar='path', required=True, type=os.path.abspath)
    parser.add_argument('-p', '--port', help='MIDI port to record from', default=0, type=int)
    parser.add_argument('-n', '--note-on-id', help='ID of note on messages', default=144, type=int)
    parser.add_argument('-l', '--length', help='duration of recordings in seconds', default=60, type=int)
    args = parser.parse_args()
    rec(args.directory, args.port, args.note_on_id, args.length)

if __name__ == "__main__":
    main()
