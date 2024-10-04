import time
import os
from CK_rec.setup import Setup
from CK_rec.rec_classes import CK_rec

class CK_rec(CK_rec):
    def prepareTrack(self):
        print("RECORDING")
        self.__mid.tracks.append(self.__track)


FILEPATH = None
FILENAME = r'%Y-%m-%d_%H-%M-%S'
PIANO_PORT = 0
ON_ID = 144

FILE_DURATION = 20#seconds

if FILEPATH:
    os.chdir(FILEPATH)

code_k = Setup()
try:
    while True:
        code_k.open_port(PIANO_PORT)
        midiRec = CK_rec(PIANO_PORT, ON_ID, debug=False)

        code_k.set_callback(midiRec)

        for i in range(FILE_DURATION*100):
            time.sleep(0.01)
        midiRec.saveTrack(time.strftime(FILENAME))
        code_k.end()
except KeyboardInterrupt:
    midiRec.saveTrack(time.strftime(FILENAME))
    code_k.end()
