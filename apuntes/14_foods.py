my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favorite  foods are:")
for food in my_foods:
    print(food, end=" ")

print("\nMy friend's favorite foods are:")
print(friend_foods)

"""
Si las copiaramos usando my_foods = friend_foods, no funcionaria, 
se crearian dos que apuntan al mismo espacio de memoria
lo que ocacionaria es que si agrego un valor a una lista, la otra
tambien lo recibe
"""