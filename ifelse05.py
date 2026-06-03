if vazn < 1 or vazn > 500:
    print("Vazn 1-500 kg oralig'ida bo'lishi kerak!")
elif boy < 0.5 or boy > 3:
    print("Bo'y 0.5-3.0 m oralig'ida bo'lishi kerak!")
else:
    bmi = vazn / (boy * boy)

    print("BMI:", bmi)

    if bmi < 18.5:
        print("Kam vazn")
    elif bmi < 25:
        print("Normal vazn")
    elif bmi < 30:
        print("Ortiqcha vazn")
    else:
        print("Semizlik")
