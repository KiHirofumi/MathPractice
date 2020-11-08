import random
import time
# 点数を初期化
tensuu = 0
# 10問のカウンター
counter = [1,2,3,4,5,6,7,8,9,10]
# 時間計測開始
start = time.time()
for number in counter:
    x = random.randrange(1,5)
    y = random.randrange(1,9)
#    if x>y:
#        a = x
#        b = y
#    else:
#        a = y
#        b = x
    a = x
    b = y
    print()
    print(f"{number}.もんだいだよ：{a} × {b}=")
    c = input()
    try:
        ans = int(c)
    except ValueError:
        print("すうじをいれてね")
        pass
    ans = int(c)
    # 正解したら、点数を＋１
    if ans==a*b:
        tensuu = tensuu + 1
        print("せいかい！")
    else:
        print("まちがいだよ。")
        print(f"こたえは{a*b}です。")
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
