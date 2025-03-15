height = input('請輸入身高(cm): ')
weight = input('請輸入體重(kg): ')
bmi = int(weight) / (int(height) / 100)**2
print('您的 BMI 值為:', bmi)
print("your weight:"+str(weight))
print("your bmi:"+str(round(bmi,2)))
