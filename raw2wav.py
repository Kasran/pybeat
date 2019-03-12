# raw2wav.py
from sys import stdin

i2b = lambda i: i.to_bytes(4,'little')

def raw2wav(buf=None, wlen=30, outf="out.wav", hz=8000):
    if buf is None:
        buf = stdin.buffer.read(wlen * hz)
    with open(outf, 'wb') as f:
        # header stuff
        r = i2b(hz)
        f.write(
            b'RIFF' +
            i2b(len(buf) + 0x24) +
            b'WAVEfmt ' +
            i2b(0x00000010) +
            i2b(0x00010001) +
            r + r +
            i2b(0x00010008) +
            b'data' +
            i2b(len(buf)) +
            buf
        )

if __name__ == "__main__":
    from sys import argv
    raw2wav(None, *argv[1:])
