import time
#根据地址码，出生日期码，性别生成身份证号码字典函数。性别可以为空
def generator(address_code,birthday_code,sex=""):
    id_list=[]
    #如果性别为空的话则不对顺序码进行奇偶判断
    if sex == "":
        for i in range(1,1000):
            i = repair_i(str(i))
            id = address_code + birthday_code + i + cheak(address_code + birthday_code + i)
            id_list.append(id)
    #如果性别位男，则对顺序码进行奇偶判断，如果顺序码为偶则跳过
    elif sex == "m":
        for i in range(1,1000):
            if i%2 == 0:
                pass
            else:
                i = repair_i(str(i))
                id = address_code + birthday_code + i + cheak(address_code + birthday_code + i)
                id_list.append(id)
    #如果性别位女，则对顺序码进行奇偶判断，如果顺序码为奇则跳过
    elif sex == "f":
        for i in range(1,1000):
            if i%2 != 0:
                pass
            else:
                i = repair_i(str(i))
                #if cheak(address_code + birthday_code + i) == "X":
                    #continue
                id = address_code + birthday_code + i + cheak(address_code + birthday_code + i)
                id_list.append(id)
    return id_list

#进行校验位计算的方法
def cheak(s):
    sum = int(s[0]) * 7 + int(s[1]) * 9 + int(s[2]) * 10 + int(s[3]) * 5 + int(s[4]) * 8 + int(s[5]) * 4 + int(s[6]) * 2 + int(s[7]) * 1 + int(s[8]) * 6 + int(s[9]) * 3 + int(s[10]) * 7 + int(s[11]) * 9 + int(s[12]) * 10 + int(s[13]) * 5 + int(s[14]) * 8 + int(s[15]) * 4 + int(s[16]) * 2
    return '10X98765432'[sum % 11]

#对顺序码进行补全
def repair_i(i):
    #如果顺序码长度为1，则在左边补“00”
    if len(i) == 1:
        i = "00" + i
    #如果顺序码长度为2，则在左边补“0”
    elif len(i) == 2:
        i = "0" + i
    return i



# 生成出生当年所有日期
def dateRange(str1,str2):
    #     时间格式
    fmt = '%Y-%m-%d'
    #     Python time strptime() 函数根据指定的格式把一个时间字符串解析为时间元组。
    # Python time mktime() 函数执行与gmtime(), localtime()相反的操作，它接收struct_time对象作为参数，返回用秒数来表示时间的浮点数。
    bgn = int(time.mktime(time.strptime(str1, fmt)))
    end = int(time.mktime(time.strptime(str2, fmt)))
    list_date = [time.strftime(fmt, time.localtime(i)) for i in range(bgn, end + 1, 3600 * 24)]
    return [i.replace('-', '') for i in list_date]

def main():
    f = open(r"C:\Users\Arnoliu\PycharmProjects\IDgen\result.txt", "w+")
    address = "310225"
    data_time = dateRange('2001-09-01','2002-08-31')#地址码
    for y in range(len(data_time)):
        birthday=data_time[y]
        #birthday = "20011015"                       #出生日期码
        sex = "f"                                #性别
        id_list = generator(address,birthday,sex)

        for i in range(len(id_list)):
            print(id_list[i],file=f)
    f.close()

if __name__ == "__main__":
    main()