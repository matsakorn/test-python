score = int(input("ป้อนคะแนนของคุณ (0-100): "))

if score >= 80:
    print("เกรด A")
elif score >= 70:
    print("เกรด B")
elif score >= 60:
    print("เกรด C")
elif score >= 50:
    print("เกรด D")
else:
    print("เกรด F")