import PySimpleGUI as sg
import pandas as pd
import sys

def TL(text): return sg.Text(text+':', justification='r', size=(80,1))
def TI(text): return sg.InputText(text, size=(10,1))

sg.theme('Default1')

def create_data_window():
    layout = [[TL('Введите путь к таблице')],
              [sg.Text( justification='r', size=(40,1)),sg.InputText(justification='r'), sg.FileBrowse("Поиск",file_types=(("Excel Files", "*.xl*"),))],
              [TL("Введите данные")],
              [TL('Допуск на фотозону'), TI(0.02)],
              [TL('Координаты круглого отверстия'), TI(0.02)],
              [TL('Координаты овального отверстия'), TI(0.02)],
              [TL('Толщина защитного стекла'), TI(0.02)],
              [TL('если защитного измерения проводятся без крышки с защитным стеклом, то значение должно быть 0.')],
              [TL('Толщина светофильтра'), TI(0.02)],
              [TL('для ПХ блоков значение должно быть 0.')],
              [TL('Поправка на толщину стекла (n-1)/n'), TI(0.02)],
              [TL('Поправка на толщину светофильтра (n-1)/n'), TI(0.02)],
              [TL('От установочной до фотоприёмной по ГЧ"'), TI(0.02)],
              [TL('Расстояние от оси блока до первого репера вдоль OY по результатам измерений'), TI(0.02)],
              [TL('Расстояние между двумя первыми реперами четных и нечетных матриц по результатам измерений'), TI(0.02)],
              [TL('Расстояние от оси блока до первого репера нечётной матрицы вдоль OY по КД'), TI(0.02)],
              [TL('Расстояние от оси блока до первого репера чётной матрицы вдоль OY по КД'), TI(0.02)],
              [TL('Ширина планки для юстировки'),TI(0.02)],
              [TL('Длина планки для юстировки'),TI(0.02)],

              [ sg.Text( justification='r', size=(70,1)),sg.Button('Далее', ), sg.B('Выход')]]
    return sg.Window('Данные', layout)


def create_subres_window():
    pass


def main():
    window = None

    while True:             # Event Loop
        if window is None:
            window = create_data_window()

        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Выход'):
            break


        if event == 'Далее':
            try:
                df = pd.read_excel(values[0])
                print(df,"/n")
                df1 = pd.read_excel(values[0],sheet_name=1)
                print(df1,"/n")
                df2 = pd.read_excel(values[0],sheet_name=2)
                print(df2,"/n")
            except Exception:
                sg.popup("Не введен путь к таблице")
            # window = create_subres_window()
        event, values = window.read()
    window.close()
main()