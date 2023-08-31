# Lucas Gasperin, Renan Pamplona, Renan Czervinski

def operate(operator, arrayOne, arrayTwo):
    setOne = set(arrayOne)
    setTwo = set(arrayTwo)
    operator = str(operator)
    if operator == 'U':
        result = setOne.union(setTwo)
        print(f'União: conjunto 1 {setOne}, conjunto 2 {setTwo}. Resultado: {result}')
    elif operator == 'I':
        result = setOne.intersection(setTwo)
        print(f'Interseção: conjunto 1 {setOne}, conjunto 2 {setTwo}. Resultado: {result}')
    elif operator == 'D':
        result = setOne.difference(setTwo)
        print(f'Diferença: conjunto 1 {setOne}, conjunto 2 {setTwo}. Resultado: {result}')
    elif operator == 'C':
        result = []

        for firstElement in setOne:
            for secondElement in setTwo:
                result.append([firstElement, secondElement])

        resultHashable = map(tuple, result)
        resultSet = set(resultHashable)

        print(f'Produto Cartesiano: conjunto 1 {setOne}, conjunto 2 {setTwo}. Resultado: {resultSet}')
    else:
        print('operador inválido')

with open("entradas3.txt", "r") as arquivo:
    lines = arquivo.readlines()


counter = len(lines) / 3
loopCounter = 0

while counter > 0:
    givenArray = []
    for i in range(3):
        givenArray.append(lines[loopCounter])
        loopCounter += 1

    firstArray = givenArray[1].replace(' ', '').replace('\n', '').split(',')
    firstArray
    secondArray = givenArray[2].replace(' ', '').replace('\n', '').split(',')

    operate(givenArray[0][0], firstArray, secondArray)
    counter -= 1






