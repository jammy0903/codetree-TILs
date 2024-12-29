
def div(a):
    if (a%2==0)and((int(a/10)+a%10)%5==0):
        result = "Yes"
    else: reuslt = "No"
    print(result)
    return 0


def main():
    n = int(input())
    
    div(n)
    return 0

main()
