'''
2. Написати функцію <bank> , яка працює за наступною логікою:
користувач робить вклад у розмірі <a> одиниць строком на <years> років під <percents> відсотків
(кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
Параметр <percents> є необов'язковим і має значення по замовчуванню <10> (10%).
Функція повинна принтануть суму, яка буде на рахунку, а також її повернути (але округлену до копійок).
'''
def bank(a, years, percents=10):
    
    for i in range (years):
        
        a = a + a/100*percents

    return a

a = float(input("User makes a contribution in the amount: "))
years = int(input("For how many years: "))

print(bank(a, years, percents=10))
