def what_to_wear(temperature, is_rainy, is_raining_heavily):
    if 20 < temperature < 30:
        if is_rainy:
            return "��������, ����� � ��������"
        else:
            return "�������� � �����"
    elif temperature > 0:
        if is_rainy:
            if is_raining_heavily:
                return "������, ��������� ������ � ����"
            else:
                return "������ � ��������"
        else:
            return "������"
    else:
        return "�������"
temperature=20
is_rainy=True
is_raining_heavily=False
print(what_to_wear(temperature, is_rainy, is_raining_heavily))