
def div(a):
    return ((a%2==0)and((int(a/10)+a%10)%5==0))


def main():
    n = int(input())
    #result = div(n) # result 는 true/false
    if div(n) is True: print("Yes")
    else: print("No")
    return 0

main()
