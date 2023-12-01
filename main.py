
def recursion(n):
    if n<=0:
        return
    recursion(n-1)
    print(n*n)



if __name__ == '__main__':
    print(recursion(4))






