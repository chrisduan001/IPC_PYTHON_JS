from subprocess import Popen, PIPE

inputVal = Popen(['node', '../Sender.js'], stdout=PIPE)
buff = ''

while True:
    out = inputVal.stdout.read(1)

    if out == '' and inputVal.poll() is not None:
        print("Error and exit")
        exit(0)

    if out == '\n':
        print(buff)
        buff = ''
    else:
        buff += out
        print(out)
