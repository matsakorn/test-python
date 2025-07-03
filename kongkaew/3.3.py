total_sum = 0

while True:
    try:
        num = float(input("ป้อนตัวเลข (พิมพ์ 0 เพื่อจบ): "))
        if num == 0:
            break
        total_sum += num
    except ValueError:
        print("กรุณาป้อนตัวเลขที่ถูกต้อง.")

print(f"ผลรวมของตัวเลขทั้งหมดคือ: {total_sum}")