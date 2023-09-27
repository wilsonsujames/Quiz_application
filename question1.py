

a = [35, 46, 57, 91, 29]


def convert_num(num_list):
    return_list=[]
    for convert_num in  num_list :
        ten_num = int(convert_num / 10)
        print(ten_num)
        units_digital = convert_num % 10
        print(units_digital)
        new_num = units_digital * 10 + ten_num
        return_list.append(new_num)

    return  return_list




b= convert_num(a)
print(b)
























