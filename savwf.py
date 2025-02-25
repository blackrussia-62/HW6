def divider(a, b):
    if a < b:
        raise ValueError("первое число больше или = второму")
    if b > 100:
        raise IndexError("Второе число не должно превышать 100")
    return a / b
data = [(10, 2), (2, 5), ("123", 4), (18, 0), ([], 15), (8, 4)]
result = []

for key, value in data:
    try:
        if not isinstance(key, (int, float)):
            print(f"элемент потирявся в {key, value}: какой блин стринг")
            continue
        res = divider(key, value)
        result.append(res)
    except ValueError as ve:
        print(f"ValueError для {key, value}: {ve}")
    except IndexError as ie:
        print(f"IndexError для {key, value}: {ie}")
    except ZeroDivisionError:
        print(f"в школе учили же, на 0 не делят {key, value}")
    except Exception as e:
        print(f"гага ошибка олду {key, value}: {e}")
print(result)
