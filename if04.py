balance = 5000

summa = int(input("Yechmoqchi bo'lgan summani kiriting: "))

if summa < 0:
    print("Manfiy summa kiritib bo'lmaydi.")
elif summa <= balance:
    balance = balance - summa
    print("Pul yechildi. Qolgan balans:", balance, "so'm")
else:
    print("Mablag' yetarli emas. Sizning balansingiz:", balance, "so'm")
