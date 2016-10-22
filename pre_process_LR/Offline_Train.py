
import numpy as np

def getUserMerchantM():
    ccf_offline_train = "/usr/data/ccf_data/ccf_offline_stage1_train.csv"
    um = {}
    offline = open(ccf_offline_train, "r")
    for line in offline:
        content = line.split(",")

        key = content[0] + "," + content[2]

        value = content[1] + "," + content[3] + "," + content[4] + "," + content[5] + "," + content[6].rstrip()

        if(um.has_key(key)):
            um[key].append(value)
        else:
            um[key]=[value]
    offline.close()
    result = []
    for key in um.keys():

        values = um.get(key)
        print key + ":" + values[0]
        rating = 0.0
        av_dis = 0.0
        av_account = 0.0

        dis_count = 0
        account_count = 0

        for value in values:
            kk = key.split(",")
            content = value.split(",")
            if(content[4] == "null" and kk[1] != "null"):
                rating -= 1
            elif(content[4] != "null" and kk[1] != "null" ):
                rating += 1
            try:
                temp_dis = float(content[2])
                av_dis += temp_dis
                dis_count += 1
            except Exception as err:
                 pass
                    # print err
            sc = str(content[1])
            if (content[1] == "null"):
                 pass
            elif (sc.find(":",0,len(sc)) == True):
                try:
                    kv = content[1].split(":")
                    k = float(kv[0])
                    v = float(kv[1])
                    av_account += v / k
                    account_count += 1
                except Exception as err:
                    print err
            else:
                try:
                    temp_account = float(content[1])
                    av_account += temp_account
                    account_count += 1

                except Exception as err:
                    print err
        if(dis_count == 0):
            av_dis = 0
        else:
            av_dis /= dis_count
        if(account_count == 0):
            av_account = 0
        else:
            av_account /= account_count
        result.append(key+"," + str(av_dis) +"," + str(av_account) +"," + str(rating) +"\r\n")
    path = "/usr/data/ccf_data/uc_1021_offline"
    last = open(path,"w")
    for x in result:
        last.write(x)
    last.close()
getUserMerchantM()