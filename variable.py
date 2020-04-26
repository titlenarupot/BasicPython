a = 3
b = 4.92
c = "SPEC"

print(a)
print(b)
print(c)

print(a, b, c)

# การสร้างตัวแปรหลายตัวในบรรทัดเดียวกัน
x = y = z = 10
j, k = 5, 15
print(x, y, z)
print(j, k)


# boolean
status = True
msg = False

# ตัวแปรแสดงผลร่วมกับข้อความ
# วิธีแรก concat string
print("ราคาขายต่อชิ้น", b, "บาท มีจำนวน", a, "ชิ้น")

# วิธีที่สอง string interpolation
print("ราคาขายต่อชิ้น %.2f บาท" % b)
print("ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d = ชิ้น" % (b, a))

# วิธีที่ 3 format string
print(f"ราคาขายต่อชิ้น {b} บาท มีจำวน {a} ชิ้น")
