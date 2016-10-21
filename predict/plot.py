from matplotlib import pyplot
def pp():
    path = "/usr/data/ccf_data/um-1020-online"

    result = open(path, "r")

    seq = []
    height = []
    for x in result:
        conts = x.split(":")
        seq.append(float(conts[2].rstrip()))
        height.append(1)

    result.close()
    print len(seq)
    pyplot.scatter(seq, height)
    pyplot.show()

pp()