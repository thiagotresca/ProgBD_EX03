from matplotlib import pyplot as plt
from collections import Counter
import sys

users = [
    {"id": 0, "name": "Hero", "sex": "M", "interest": "F", "interest2": "Git"},
    {"id": 1, "name": "Dunn", "sex": "M", "interest": "F", "interest2": "Python"},
    {"id": 2, "name": "Sue", "sex": "F", "interest": "M", "interest2": "Java"},
    {"id": 3, "name": "Chi", "sex": "F", "interest": "M", "interest2": "Git"},
    {"id": 4, "name": "Thor", "sex": "M", "interest": "F", "interest2": "Python"},
    {"id": 5, "name": "Clive", "sex": "M", "interest": "F", "interest2": "Java"},
    {"id": 6, "name": "Hicks", "sex": "M", "interest": "F", "interest2": "Git"},
    {"id": 7, "name": "Devin", "sex": "M", "interest": "F", "interest2": "Git"},
    {"id": 8, "name": "Kate", "sex": "F", "interest": "M", "interest2": "Python"},
    {"id": 9, "name": "Klein", "sex": "F", "interest": "M", "interest2": "Java"}
]

# lista = [1, 2, 3, 4, 5]
# lista[2] = 7
# lista = [1, 2]


# tupla = (1, 2, 3, 4, 5)
# print (tupla[2])
# tupla[2] = 3
# tupla = (9, 9, 1)

# tupla = 2

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5),
    (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

for user in users:
    user["friends"] = []


for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

# print(users)

# int numero (int a, int b){
#  return a + b;
# }


# def soma(a, b):
#     c = a + b


# resultado = soma (2, 3)

# print(soma(2, 3))


def number_of_friends(user):
    return len(user['friends'])


# print(number_of_friends(users[0]))

def number_of_female_friends(indexf):
    rfem = 0
    for aux in range(12):
        if friendships[aux][0] == indexf:
            if users[friendships[aux][1]]['sex'] == 'F':
                rfem = rfem + 1
        if friendships[aux][0] == indexf:
            if users[friendships[aux][0]]['sex'] == 'F':
                rfem = rfem + 1
    return rfem

def number_of_male_friends(indexm):
    rmasc = 0
    for aux in range(12):
        if friendships[aux][0] == indexm:
            if users[friendships[aux][1]]['sex'] == 'M':
                rmasc = rmasc + 1
        if friendships[aux][0] == indexm:
            if users[friendships[aux][0]]['sex'] == 'M':
                rmasc = rmasc + 1
    return rmasc

friendsCountBySex = [
    {"0": (number_of_male_friends(0), number_of_female_friends(0))},
    {"1": (number_of_male_friends(1), number_of_female_friends(1))},
    {"2": (number_of_male_friends(2), number_of_female_friends(2))},
    {"3": (number_of_male_friends(3), number_of_female_friends(3))},
    {"4": (number_of_male_friends(4), number_of_female_friends(4))},
    {"5": (number_of_male_friends(5), number_of_female_friends(5))},
    {"6": (number_of_male_friends(6), number_of_female_friends(6))},
    {"7": (number_of_male_friends(7), number_of_female_friends(7))},
    {"8": (number_of_male_friends(8), number_of_female_friends(8))},
    {"9": (number_of_male_friends(9), number_of_female_friends(9))},
]

def suggest_friend():
    for aux in range(10):
        for aux2 in range(10):
            if users[aux]['id'] != users[aux2]['id']:
                if users[aux]['sex'] == users[aux2]['interest']:
                    print("Sugestão de amizade para o usuário", users[aux]["name"], ":", users[aux2]["name"])

def suggest_friend2():
    for aux in range(10):
        for aux2 in range(10):
            if users[aux]['id'] != users[aux2]['id']:
                if (users[aux]['sex'] == users[aux2]['interest']) and (users[aux]['interest2']==users[aux2]['interest2']):
                    print("Sugestão de amizade para o usuário", users[aux]["name"], ":", users[aux2]["name"])

friendsCount = [
    {users[0]['name']: (number_of_male_friends(0) + number_of_female_friends(0))},
    {users[1]['name']: (number_of_male_friends(1) + number_of_female_friends(1))},
    {users[2]['name']: (number_of_male_friends(2) + number_of_female_friends(2))},
    {users[3]['name']: (number_of_male_friends(3) + number_of_female_friends(3))},
    {users[4]['name']: (number_of_male_friends(4) + number_of_female_friends(4))},
    {users[5]['name']: (number_of_male_friends(5) + number_of_female_friends(5))},
    {users[6]['name']: (number_of_male_friends(6) + number_of_female_friends(6))},
    {users[7]['name']: (number_of_male_friends(7) + number_of_female_friends(7))},
    {users[8]['name']: (number_of_male_friends(8) + number_of_female_friends(8))},
    {users[9]['name']: (number_of_male_friends(9) + number_of_female_friends(9))},
]

print(friendsCount[5][users[5]['name']])
def grafico_linha ():
  name = [users[0]['name'], users[1]['name'], users[2]['name'], users[3]['name'], users[4]['name'], users[5]['name'], users[6]['name'], users[7]['name'], users[8]['name'], users[9]['name']]
  friends = [friendsCount[0][users[0]['name']], friendsCount[1][users[1]['name']], friendsCount[2][users[2]['name']], friendsCount[3][users[3]['name']], friendsCount[4][users[4]['name']], friendsCount[5][users[5]['name']], friendsCount[6][users[6]['name']], friendsCount[7][users[7]['name']], friendsCount[8][users[8]['name']], friendsCount[9][users[9]['name']]]
  plt.plot (name, friends, color='green', marker='o', linestyle='solid')
  plt.title ("Amigos por Usuário")
  plt.show()


#suggest_friend()
#suggest_friend2()
#print(friendsCountBySex)
#print(friendsCount)
#print(friendships[0][0])
#print(sys.getsizeof(friendships))
#print(users[0]['sex'])