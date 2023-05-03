def num_input_val(message):
    while True:
        try:
            num = int(input(message))
            assert 0 < num <= 3, 'Число превышает диапазон чисел координат'
        except AssertionError as msg:
            print(msg)
        except:
            print('Введите целое число')
        else:
            return num
