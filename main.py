# import ทั้งหมดทุกฟังชั่นใน Module
#import numbers

#import มาบางฟังชั่น
#from numbers import factorial, fibonacci
#import ทุกฟังชั่น
#from numbers import*

# import และเปลี่ยนชื่อฟังชั่น (นามแฝง) alias
from numbers import factorial as fa, fibonacci as fi

# เรียกใช้งาน
# print(numbers.factorial(5))
# print(numbers.fibonacci(100))

print(fa(5))
print(fi(100))
