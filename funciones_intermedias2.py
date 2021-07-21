x = [ [5,2,3], [10,8,9] ] 
#1.Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x[1][0] = 15
print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#2.Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students[0]['last_name'] = 'Bryant'
print (students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
#3.En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
#4.Cambia el valor 20 en z a 30
z[0]['y'] = 30
print(z)

#2. Itera a través de una lista de diccionarios .Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado.
print('*'*30)
def iterateDictionary(some_list):
    for i in range (len(some_list)):
        for key, value  in some_list[i].items():
            print(f'{key} - {value}')

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)

# Bonus: Hacer que aparezcan exactamente así! first_name - Michael, last_name - Jordan
print('*'*30)
def iterateDictionary(some_list):
    for i in range (len(some_list)):
        a = ''
        for key, value  in some_list[i].items():
            a += f'{key} - {value}  '
        print(a)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)

#3. Obtén valores de una lista de diccionarios. Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario

def iterateDictionary2(key_name, some_list):
    for i in range (len(some_list)):
        print(some_list[i][key_name])

print('*'*30)
iterateDictionary2('first_name', students)
print('*'*30)
iterateDictionary2('last_name', students)

#4. Itera a través de un diccionario con valores de listas. Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave.

def printInfo(some_dict):
    for key, value  in some_dict.items():
        print(f'{len(value)} {key.upper()}')
        for i in value:
            print(i)
        print()

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print('*'*30)
printInfo(dojo)