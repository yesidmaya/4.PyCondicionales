# -*- coding: utf-8 -*-

def say_hello(age):
    if age > 18:
        result = print('La edad es de un SEÑOR')
    else:
        result = print('La edad es de un NIÑO')

    return result

def main():
    age = int(input('Cual es tu edad? -> '))
    print('')
    respuesta = say_hello(age)

if __name__ == "__main__":
    main()