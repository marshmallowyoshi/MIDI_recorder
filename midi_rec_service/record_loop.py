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
                print("MIDI Device not connected")
                break
            midiRec = CK_rec(port, on_id, debug=False)

            code_k.set_callback(midiRec)

            for i in range(duration*100):
                time.sleep(0.01)
            midiRec.saveTrack(time.strftime(FILENAME))
            code_k.end()
            del code_k, midiRec
    except KeyboardInterrupt:
        midiRec.saveTrack(time.strftime(FILENAME))
        code_k.end()

if __name__ == "__main__":
    rec(FILEPATH, PIANO_PORT, ON_ID)
