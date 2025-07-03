temperature = float(input("ป้อนอุณหภูมิ (หน่วย °C): "))

if temperature < 0:
    print("หนาวจัด")
elif 0 <= temperature <= 15:
    print("หนาว")
elif 16 <= temperature <= 30:
    print("ปกติ")
elif 31 <= temperature <= 39:
    print("ร้อน")
else:
    print("ร้อนมาก")