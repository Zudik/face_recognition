import os

dict_action = {
	'1':"os.system('python3 create_dateset.py')",
	'2':"os.system('python3 train_face_recognition.py')",
	'3':"os.system('python3 recognition_face.py')",
	'4':'exit()'
}

while True:
	print('Порядок работы программы')
	print('1 - Создать датасет')
	print('2 - Обучить классификатор')
	print('3 - Распознать лицо')
	print('4 - Выйти из программы')
	option = input('Выберете пункт из списка \t')
	eval(dict_action[option])
