import random
import time

tensuu = 0
counter = [1,2,3,4,5,6,7,8,9,10]
# 時間測定開始
start = time.time()

for number in counter:
    a = random.randrange(1,30)
    b = random.randrange(1,30)
    print()
    print(f"{number}.もんだいだよ：{a}+{b}=")
    c = input()
    ans = int(c)
    if ans==a+b:
        tensuu = tensuu + 1
        print("せいかい！")
    else:
        print("まちがいだよ。")
        print(f"こたえは{a+b}です。")
print()
print(f"{tensuu * 10}てん でした")
print()
if tensuu == 10:
    print("すごい！\nよくできました！")
elif tensuu < 8:
    print("もっとがんばろう")
else:
    print("おしい！\nもうすこしだったね")
# 時間測定終了
endtime = time.time()
print(f"かかった時間は{round(endtime - start)}秒でした")
