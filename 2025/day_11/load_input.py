from typing import NamedTuple

test_dat = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out

"""


class Device(NamedTuple):
    name: str
    connections: list[str]


def load_input(test: bool = False) -> dict[str, Device]:
    if test:
        data = test_dat.strip().splitlines()
    else:
        with open("2025/input/day_11.txt") as f:
            data = f.read().strip().splitlines()

    devices = {}
    for line in data:
        name, conns = line.split(": ")
        connections = conns.split(" ")
        devices[name] = Device(name=name, connections=connections)

    return devices
