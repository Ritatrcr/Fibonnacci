def fibonnacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)
    
def main():
    num=int(input("Enter the number of terms: "))
    print(fibonnacci(num))