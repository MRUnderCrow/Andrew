temperature=20
is_rainy=True
is_raining_heavily=False
if 20 < temperature < 30:
	if is_rainy:
		print("��������, ����� � ��������")
	else:
		print("�������� � �����")
elif temperature > 0:
	if is_rainy:
		if is_raining_heavily:
			print("������, ��������� ������ � ����")
		else:
			print ("������ � ��������")
	else:
		print ("������")
else:
	print ("�������")