import time
import os
from midi_rec_service.CK_rec.setup import Setup
from midi_rec_service.CK_rec.rec_classes import CK_rec

class CK_rec(CK_rec):
    def prepareTrack(self):
        print("RECORDING")
        self.__mid.tracks.append(self.__track)


FILEPATH = None
FILENAME = r'%Y-%m-%d_%H-%M-%S'
PIANO_PORT = 1
ON_ID = 144

FILE_DURATION = 300#seconds

def rec(path: str,
        port: int = 0,
        on_id: int = 144,
        duration: int = 60
        ) -> None:

    if path:
        os.chdir(path)

    try:
        while True:
            code_k = Setup()
            try:
                code_k.open_port(port)
            except IndexError:
                print("MIDI Device not connected, trying again in 10 seconds...")
                time.sleep(10)
                continue
            midi_rec = CK_rec(port, on_id, debug=False)

            code_k.set_callback(midi_rec)

            for _ in range(duration*100):
                time.sleep(0.01)
            midi_rec.saveTrack(time.strftime(FILENAME))
            code_k.end()
            del code_k, midi_rec
    except KeyboardInterrupt:
        midi_rec.saveTrack(time.strftime(FILENAME))
        code_k.end()

if __name__ == "__main__":
    rec(FILEPATH, PIANO_PORT, ON_ID)
