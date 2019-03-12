from sys import stdout, stderr, argv, exit
from raw2wav import raw2wav
import argparse

def count(a=0):
    while True:
        a += 1; yield a

ap = argparse.ArgumentParser(
    description="bytebeats in python!"
)
ap.add_argument('module',
    nargs='*', default=None,
    help="the py bytebeat module to render")
ap.add_argument('--exec', '-e',
    type=str, default=None,
    help="executes a function of t passed as a parameter (overrides module)")

ap.add_argument('--render',
    type=str, nargs='?', default=False,
    help="renders to a file (default: prints raw bytes indefinitely)")
ren_def = 'out.wav'
ap.add_argument('--freq', '-f',
    type=int, default=8000,
    help="sample rate for render (default: 8000)")
ap.add_argument('--len', '-l',
    type=int, default=30,
    help="length in seconds (default: 30)")

args = ap.parse_args()
print(args)
render = args.render
if render is None: render = ren_def

# where are the bytes gonna come from
if args.exec:
    update = eval("lambda t: (%s)"%args.exec)
elif args.module:
    mod, params = args.module[0], args.module[1:]
    update = __import__(mod).setup(*params)
else:
    stderr.write("please include either a module name or --exec\n")
    exit(1)

print(update)

play_stream = map(lambda t: (int(update(t))&0xff).to_bytes(1,'big'), count())

# where are the bytes gonna go
if render is False:
    while True:
        stdout.buffer.write(next(play_stream))
else:
    buf = b''.join(next(play_stream) for _ in range(args.freq*args.len))
    raw2wav(buf, args.len, render, args.freq)
