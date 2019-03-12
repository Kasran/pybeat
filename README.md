# Pybeat
Python tool for bytebeat compositions, by Kasran

**This tool requires Python 3. It won't work with Python 2.**


## What on earth is bytebeat?
[This website](http://canonical.org/~kragen/bytebeat/) explains it better than
I ever could in a little readme, but the gist is that bytebeat is a genre of
computer music made with a program that outputs a stream of bytes that's
interpreted as a soundwave. Tiny programs can make very interesting (albeit
perhaps somewhat harsh) musical patterns!


## Usage
Here are some examples for using this tool.

### Printing bytes to stdout
```
python pybeat.py test
```
Opens `test.py` (see that file for an explanation of how it's structured) and
runs the bytebeat code therein, printing the raw bytes to stdout forever. Use
this if your bytebeat toolchain uses other tools that need to do things with
the byte stream.

### Passing arguments to your module
```
python pybeat.py test 400
```
You can optionally pass additional arguments into your bytebeat module from the
command line. The included example module allows you to change the tuning of A4
to, for example, 400Hz.

### Rendering to .wav
```
python pybeat.py test --render test.wav
```
Opens `test.py` and runs the bytebeat code therein, rendering the first 30
seconds worth of bytes (at an 8000Hz sampling rate) to the file `test.wav`. (If
no filename is provided, it will default to `out.wav`.)

Using `--freq x` will change the sampling rate to x Hz (substitute your
desired sampling rate, e.g. 44100). Using `--len y` will render y seconds
worth of audio.

### Inline expressions
```
python pybeat.py -e "(t*5)&t>>7"
```
You can use `--eval` or `-e` instead of a module name, providing a Python
expression that uses `t` for the current time step, and pybeat will use that
to generate a bytestream.


## raw2wav
`raw2wav.py` is an auxiliary tool used by pybeat to render .wav files. It's a
Python module, but can also be run standalone, in which case it accepts a stream
of bytes from stdin and renders using those. Here's how to use it standalone:
```
python raw2wav.py (wlen) (filename) (sample rate)
```
e.g.:
```
python raw2wav.py 30 out.wav 8000
```
If arguments are not provided it will default to 30 seconds at 8000Hz to
`out.wav`.

Feel free to use it to render bytebeat programs of other kinds if you think it's
useful!


## Oh god please help
This tool is very new and is under construction! It will probably break if
you're not kind to it. Please submit an issue if you find something awry.
