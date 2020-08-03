import random
tensuu = 0
counter = [1,2,3,4,5]
for number in counter:
    kbn = random.randrange(1,4)
    a = random.randrange(1,10)
    b = random.randrange(1,10)
    c = random.randrange(1,10)
    if a >= b >= c:
        x = a
        y = b
        z = c
    elif a >= c >= b:
        x = a
        y = c
        z = b
    elif  b >= a >= c:
        x = b
        y = a
        z = c
    elif b >= c >= a:
        x = b
        y = c
        z = a
    elif c >= a >= b:
        x = c
        y = a
        z = b
    else:
        x = c
        y = b
        z = a
    if kbn == 1:
        print(f"{number}もん目：{x} + {y} + {z} = ")
        ans = input()
        if int(ans) == x + y + z:
            print("せいかい！")
            tensuu += 1
        else:
            print("ざんねん。ちがうよ。")
            print(f"{x+y+z}だよ")
    elif kbn == 2:
        print(f"{number}もん目：{x} - {y} + {z} = ")
        ans = input()
        if int(ans) == x - y + z:
            print("せいかい！")
            tensuu += 1
        else:
            print("ざんねん。ちがうよ。")
            print(f"{x-y+z}だよ")
    elif kbn == 3:
        print(f"{number}もん目：{x} + {y} - {z} = ")
        ans = input()
        if int(ans) == x + y - z:
            print("せいかい！")
            tensuu += 1
        else:
            print("ざんねん。ちがうよ。")
            print(f"{x+y-z}だよ")
print()
print(f"{tensuu * 20}てんでした！")
if tensuu == 5:
    print("すごいね！！よくできました")
elif tensuu == 0:
    print("もっとがんばろう")
else:
    print("もうちょっと。がんばってね。")