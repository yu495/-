import random as r
import time

i = 0
j = 0
pcs = {1:4, 2:25, 3:168, 4:1229, 5:9592}
ans = []
facts = []
challenge = 1

print("select difficulty (1 ~ 5)")
print("1 -> Easy\n2 -> Very Hard\n3 -> Lunatic\n4 -> Catastrophe\n5 -> World's End\n")
diff = input(":")

if diff.isdecimal() == False:
    print(":(")

else:
    diff = int(diff)

    if diff < 1:
        print(f"{diff} is out of range Sadge")
    elif diff > 5:
        print("why would you like to go insane???")

    else:
        t1 = time.time()
        print("\n少女祈祷中...\n\tNow Loading...")
        with open("./primes") as f:
            primes = f.readlines()
        primes = list(map(lambda x:int(x.strip()), primes))
        t2 = time.time()
        if t2 - t1 < 1:
            time.sleep(1 - (t2 - t1))
        print("done!")

        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("ご")
        print()

        t1 = time.time()
        while(i < 6 - diff):
            pfc = r.randint(2,4)
            challenge = 1
            j = 0
            facts = []
            while(j < pfc):
                pf = primes[r.randint(0,pcs[diff]-1)]
                challenge *= pf
                facts.append(pf)
                j += 1
            facts.sort()
            ans.append(facts)
            print(f"{i+1}/{6-diff}: {challenge} ({pfc} Prime Factors)")
            i += 1
        input("return to show answers")
        t2 = time.time()
        elapsed_time = round(t2 - t1, 3)

        print()
        print(f"time: {elapsed_time}sec")
        print(f"answer(s): {ans}")
        print()