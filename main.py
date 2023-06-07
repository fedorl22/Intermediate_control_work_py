notes = []
if len(notes) == 0:
    print("Записная книжка пуста")
else:
    print("\nСписок записей:")
    for note in notes:
        print(note)

def addNote():
    noteToAdd = input("Введите текст новой записи: ")
    notes.append(noteToAdd)
    print("\nЗапись успешно добавлена !")
    return notes

def deleteNote():
    noteToDelete = input("Введите текст записи для удаления: ")
    if noteToDelete in notes:
        notes.remove(noteToDelete)
        print("\nЗапись успешно удалена!")
    else:
        print("\nТакая запись отсутствует!")

def earliestNotes():
        earliestNotes = sorted(notes, key=str or float)
        for note in earliestNotes:
            print(note)

def latestNotes():
    latestNotes = sorted(notes, key=str or float, reverse=True)
    print("\nПоследние записи:")
    for note in latestNotes:
        print(note)



notes = []
while True:
    choice = input("\nВыберите пункт из меню. \n[1] Показать запись \n[2] Добавить запись \n[3] Удалить запись \n[4] Самые ранние записи \n[5] Последние записи \n[q] Выйти из записной книжки \n ")
    if choice == '1':
        print('|'.join(notes))
    elif choice == '2':
        addNote()
    elif choice == '3':
        deleteNote()
    elif choice == '4':
        earliestNotes()
    elif choice == '5':
        latestNotes()
    elif choice == 'q':
        break
    else:
        print("Выберите корректный вариант!")