
def getTestUserMerchantM():
    ccf_offline_train = "/usr/data/ccf_data/ccf_offline_stage1_test_revised.csv"
    online = open(ccf_offline_train, "r")
    um = {}

    offline = open(ccf_offline_train, "r")
    for line in offline:
        content = line.split(",")
        temp = content[0] + ":" + content[2]
        # currently we ignore fixed
        if(content[2] == "null" or content[2] == "fixed"):
            continue

        if (not um.has_key(temp)):
            um[temp] = 0.0

    offline.close()

    path = "/usr/data/ccf_data/um_test-1019"

    result = open(path,"w")

    for x in um.keys():
        result.write(x + "\r\n")

    result.close()
getTestUserMerchantM()