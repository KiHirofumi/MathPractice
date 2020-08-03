import random
tensuu = 0
counter = [1,2,3,4,5]
for number in counter:
    kbn = random.randrange(1,5)
    a = random.randrange(-10,10)
    b = random.randrange(-10,10)
    c = random.randrange(-10,10)
    print()
    if kbn == 1:
        print(f"{number}問目：")
        print(f"{a}x+{b}x=")
        ans = f"{a+b}x"
        ans2 = f"{a+b}x"
        answer = input()
    elif kbn == 2:
        print(f"{number}問目：")
        print(f"{a}x+({b})+{c}x=")
        ans = f"{a+c}x+({b})"
        ans2 = f"{a+c}x+{b}"
        answer = input()
    elif kbn == 3:
        print(f"{number}問目：")
        print(f"{a}x-({b}x+({c}))=")
        ans = f"{a-b}x+({-c})"
        ans2 = f"{a-b}x+{-c}"
        answer = input()
    elif kbn == 4:
        print(f"{number}問目：")
        print(f"{a}({b}x+{c})=")
        ans = f"{a*b}x+{a*c}"
        ans2 = f"{a*b}x+({a*c})"
        answer = input()
    else:
        print(f"{number}問目：")
        print(f"{a}x×({b})=")
        ans = f"{a*b}x"
        ans2 = f"{a*b}x"
        answer = input()
    if answer == ans:
        print("Good") 
        tensuu += 1
    elif answer == ans2:
        print("Good")
        tensuu += 1
    else:
        print("No Good")
        print(f"答えは {ans} や {ans2} です")
print()
print(f"{tensuu * 20}点 でした")
print()
if tensuu == 5:
    print("すごい！\nよくできました！")
elif tensuu < 2:
    print("もっとがんばろう")
else:
    print("おしい！\nもうすこしだったね")