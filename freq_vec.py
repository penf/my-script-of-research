
# arff_path = "D:\\dex_analysis\\check kernal\\weka_fakeplay.arff"
arff_path = r"E:\All learning district as a disk\testdata\arff\weka_boxer.arff"
threshold = 0.5


def list_vec(path):
    with open(path, "r") as f:
        lines = f.readlines()[32773:-1]


    found_index = {}
    apk_num = len(lines)
    print("apk numbers:", apk_num)
    for line in lines:
        end = line.rfind("32768")
        content = line[1:end-1]
        split_c = content.split(",")
        for c in split_c:
            value = c.split(" ")[0]
            if value in found_index.keys():
                found_index[value] += 1
            else:
                found_index[value] = 1
    remove_k = []
    for k, v in found_index.items():
        if v/apk_num < threshold:
            remove_k.append(k)
    for k in remove_k:
        found_index.pop(k)
    return found_index

s=list_vec(arff_path)
print(s)
print(len(s))



