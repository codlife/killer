from pylab import *
from matplotlib import pyplot
def predict():

    prPath = "/usr/data/ccf_data/predict_offline"

    prf = open(prPath, "r")

    pr = {}

    cc = 0
    for line in prf:
        content = line.split(",")
        temp = content[0]  + ","  + content[1]


        if(len(content) != 3):
            continue
        pr[temp] = content[2].rstrip()
        cc += 1
        print cc

    resultPath = "/usr/data/ccf_data/result.csv"
    rf = open(resultPath, "w")


    seq = []
    height = []
    print len(pr.values())
    i = 0
    for x in pr.values():

        seq.append(float(x))
        height.append(1)
    pyplot.scatter(seq,height)
    pyplot.show()


    for x in pr.keys():

        temp = float(pr[x])

        re = 0.0
        if(temp > 5.5):
            re = 4
        elif(temp > 3.5):
            re = 3.5 + (temp - 3.5)/4
        elif(temp > 0):
            re = temp

        # re -= 0.5
        re /= 4
        if(re > 1.0):
            re = 1.0
        if(re < 0.0):
            re = 0.0
        pr[x] = re

    seq = []
    height = []
    print len(pr.values())
    i = 0
    for x in pr.values():
        seq.append(float(x))
        height.append(1)
    pyplot.scatter(seq, height)
    pyplot.show()

    testData = "/usr/data/ccf_data/ccf_offline_stage1_test_revised.csv"
    td = open(testData, "r")


    i = 0
    count =0
    cc = 0
    for line in td:
        i += 1
        print i
        content = line.split(",")
        temp = content[0] + ":" + content[2]
        # currently we ignore fixed
        if(content[2] == "null" or content[2] == "fixed"):
            continue
        temp = content[0] + "," + content[2]
        if(pr.has_key(temp)):

            if(temp == "0.0"):
                count += 1
            pro = content[0] + "," + content[2] + "," + content[5].rstrip() +"," + "%.5f" % pr[temp] + "\r\n"
        else:
            cc += 1
            count += 1
            pro = content[0] + "," + content[2] + "," + content[5].rstrip() + "," + "0.0" + "\r\n"
        rf.write(pro)

    print cc
    print count
    rf.close()
    td.close()
predict()