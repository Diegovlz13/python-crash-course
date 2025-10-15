cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)
print(cubes)

# Listas por comprension
cubes = [cube ** 3 for cube in range(1, 11)]
print(cubes)