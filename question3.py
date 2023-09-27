

def last_num_serial(n):
    serial  = n%3
    if serial == 0:
        return 2
    elif serial == 1:
        return 1
    else:
        return 2



ans=last_num_serial(30)

print(ans)






