name = int(input("Enter the time in seconds: "))

sec = name % 60
hours = name // 3600
sec %= 60
minutes = (name - hours * 3600) // 60
print("%02d:%02d:%02d" % (hours, minutes, sec))