def celciusToFah(c):
    f = (c*9/5)+32
    return f

# print(f'{"Celsius":<15}{"Fahrenheit":<15}')
# print('-' * 30)
# for celcius in range(0,100):
#     print(f'{celcius}|{celciusToFah(celcius)}')
#     print(f'_')


#
# c2f = lambda c: ((c*9/5) + 32)
# print(f'{c2f(30)}')

t= [0, 10, 20, 30, 40]
f2 = map(lambda c: ((c*9/5) + 32),t)
print(list(f2))

import pandas as pd

data = {
    'applicantID': ['A432', 'C747', 'C751', 'B716', 'A623', 'B394', 'A294', 'B318', 'B164', 'A126'],
    'eng': [91, 94, 74, 63, 90, 76, 90, 62, 79, 89],
    'math': [97, 94, 55, 89, 73, 91, 86, 57, 57, 82],
    'interview': [83, 58, 89, 93, 81, 90, 94, 55, 89, 85]
}

df = pd.DataFrame(data)
print(df)

df['score_weight'] = df.apply(lambda x: x.eng * 0.5 + x.math * 0.7, axis=1)
df['result'] = df.apply(lambda s: 'pass' if s.score_weight > 100 else 'fail', axis=1 )

print(df)