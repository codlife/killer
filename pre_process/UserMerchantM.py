
import numpy as np
def getUserMerchantM():
    ccf_online_train = "/usr/data/ccf_data/ccf_online_stage1_train.csv"
    ccf_offline_train = "/usr/data/ccf_data/ccf_offline_stage1_train.csv"
    online = open(ccf_online_train, "r")
    um = {}
    # for line in online:
    #     content = line.split(",")
    #     if(content[3] ==  "null" or content[3] == "fixed"):
    #         continue
    #
    #     temp = content[0]+":"+content[3]
    #     content[6] = content[6].rstrip()
    #     if(um.has_key(temp)):
    #         if(content[6] == "null" and content[3] != "null"):
    #             um[temp] = um[temp] - 1
    #         elif(content[6] != "null" and content[3] != "null" ):
    #             try:
    #                 a = float(content[6])
    #                 b = float(content[5])
    #                 if((a - b) < 15):
    #                     um[temp] = um[temp] + 1
    #                 else:
    #                     um[temp] += 0.2
    #             except Exception as err:
    #                 print err
    #                 print content[6]
    #
    #     else:
    #         um[temp] = 0.0
    #         if (content[6] == "null" and content[3] != "null"):
    #             um[temp] = um[temp] - 1
    #         elif (content[6] != "null" and content[3] != "null"):
    #             try:
    #                 a = float(content[6])
    #                 b = float(content[5])
    #                 if ((a - b) < 15):
    #                     um[temp] = um[temp] + 1
    #                 else:
    #                     um[temp] += 0.2
    #             except Exception as err:
    #                 print err
    #                 print content[6]
    #
    #
    #
    # online.close()

    offline = open(ccf_offline_train, "r")

    for line in offline:
        content = line.split(",")
        if(content[2] ==  "null" or content[2] == "fixed"):
            continue

        temp = content[0]+":"+content[2]
        content[6] = content[6].rstrip()
        if(um.has_key(temp)):
            if(content[6] == "null" and content[2] != "null"):
                um[temp] = um[temp] - 1
            elif(content[6] != "null" and content[2] != "null" ):
                try:
                    a = float(content[6])
                    b = float(content[5])
                    if((a - b) < 15):
                        um[temp] = um[temp] + 1
                    #must be in with spark
                    # else:
                        # um[temp] += 0.2
                except Exception as err:
                    print err
                    print content[6]

        else:
            um[temp] = 0.0
            if (content[6] == "null" and content[2] != "null"):
                um[temp] = um[temp] - 1
            elif (content[6] != "null" and content[2] != "null"):
                try:
                    a = float(content[6])
                    b = float(content[5])
                    if ((a - b) < 15):
                        um[temp] = um[temp] + 1
                    # else:
                    #     um[temp] += 0.2
                except Exception as err:
                    print err
                    print content[6]


    path = "/usr/data/ccf_data/um-1020-offline"

    result = open(path,"w")

    for x in um.keys():
        result.write(x + ":" + str(um.get(x)) +"\r\n")

    result.close()
getUserMerchantM()