sec = int(input("Enter time in sec: "))
hh = sec // 3600
mm = (sec % 3600) // 60
ss = sec % 60
print(f"{hh:02}:{mm:02}:{ss:02}")
