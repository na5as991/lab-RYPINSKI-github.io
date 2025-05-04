# 1й вариант Рыпинский
birth=int(input('ввердите сколько кроликов рождает 1 пара репродуктивных особей  '))
month=int(input('введите на каком месяце вы хотите отследить популяцию  '))
rep=1 #репродуктивные
not_rep=birth #не репродуктиные
for i in range(2,month):
     rep,not_rep = rep + not_rep,rep * birth
print(not_rep+rep,end=' ')