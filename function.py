# การสร้างฟังชั่นแบบไม่มีการ return value
def hello(name):
    print(f"Hello {name}")


# การสร้างฟังชั่นแบบมีการ Return Value
def area(width, height):
    total = width * height
    return total


# เรียกใช้งานฟังชั่น hello()
hello("Title")

# เรียกใช้งานฟังชั่น area()
print("พื้นที่ทั้งหมด", area(5, 8))
print(area(15, 7.5))
print()
# ฟั่งชั่นแบบมีค่าเริ่มต้น


def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name:{name}")
    print(f"Salary:{salary}")
    print(f"Language:{lang}")


# เรียกใช้งานฟังชั่น show_info()
show_info()
print()
show_info('Title', 15000, 'PHP')
