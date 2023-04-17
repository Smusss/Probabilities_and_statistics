# Задача 4. В университет на факультеты A и B поступило равное количество студентов, 
# а на факультет C студентов поступило столько же, сколько на A и B вместе. 
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. Какова вероятность, что он учится: 
# a). на факультете A б). на факультете B в). на факультете C?


def baies(ab, b, a):
    chance = (ab*b) / a  # P (B_3│A)=(P(A│B_3 ) * P(B_3))/(P(A))
    return chance


print('Сдал сессию - событие А, то, что это студент конкретного факультета - событие В.\n\
Так как одно из событий уже произошло используем формулу Байеса.\n\
Так как нет точного колическтва студентов, принимаем количество студентов факультета А за условную единицу.')


passed_the_session = [0.9, 0.7, 0.9]
faculty_a = 1

faculty_b = faculty_a
faculty_c = faculty_a + faculty_b
amount_of_students = 0
faculty_amount = [faculty_a, faculty_b, faculty_c]
for i in faculty_amount: amount_of_students += i
a = 0  # вероятность события А
for i in range(len(passed_the_session)):
    a += faculty_amount[i] / amount_of_students * passed_the_session[i]
result = []
for i in range(len(passed_the_session)):
    propability = baies(passed_the_session[i], faculty_amount[i] / amount_of_students, a)
    result.append(propability)

print(f'Вероятность что студент факультета А = {result[0]}.')
print(f'Вероятность что студент факультета В = {result[1]}.')
print(f'Вероятность что студент факультета С = {result[2]}.')
