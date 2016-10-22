

def getUserMerchantM():
    ccf_online_train = "/usr/data/ccf_data/ccf_online_stage1_train.csv"
    ccf_offline_train = "/usr/data/ccf_data/ccf_offline_stage1_train.csv"

    um = {}


    offline = open(ccf_offline_train, "r")

    count = 0
    for line in offline:
        content = line.split(",")
        temp = content[2]
        if(not um.has_key(temp) and temp != "null"):
            um[temp] = 1

        count += 1

    online = open(ccf_online_train,"r")
    contain = 0
    total = 0
    for line in online:
        content = line.split(",")
        temp = content[3]

        if(um.has_key(temp)):
            contain += 1
        total += 1

    print total
    print contain
    print count
    print len(um)




getUserMerchantM()