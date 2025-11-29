def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return ValueError("Division by zero")
    else:
        return a/b

def pow(a,b):
    return a**b

if __name__=="__main__":
    print("加法测试：",add(5,3))
    print("减法测试：",sub(5,3))
    print("乘法测试：",mul(5,3))
    print("除法测试：",div(5,3))
    print("幂运算测试：",pow(5,3))

