# �������� ���������� ����� �� �����
total_apples = int(input("������� ���������� ��������� �����: "))

# ����� ������ ������� ����� 4 ������� �����
apples_per_person = total_apples // 4  # ������������� �������
total_for_trip = apples_per_person * 4  # ����� ���������� ����� ��� ������
apples_to_leave = total_apples % 4      # ������� �����

# ������� ����������
print(f"����� ������� �����: {total_apples}")
print(f"�� ������� ����� ����� ����������: {apples_per_person} �����")
print(f"����� ����� � �����: {total_for_trip} �����")
print(f"����� �������� ����: {apples_to_leave} �����")
