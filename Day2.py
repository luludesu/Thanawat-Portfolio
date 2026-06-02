import random

number = random.randint(1, 100)

guess = None

while guess != number:
    guess = int(input("เดาตัวเลขระหว่าง 1 ถึง 100: "))
    
    if guess < number:
        print("ต่ำเกินไป! ลองอีกครั้ง.")
    elif guess > number:
        print("สูงเกินไป! ลองอีกครั้ง.")
    else:
        print("ยินดีด้วย! คุณเดาถูกแล้ว!")