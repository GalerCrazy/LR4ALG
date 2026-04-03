import pandas as pd
def calculus(a : str, b : str, n: int):
    result = None
    # Извлечение данных из файлов по пути a и b
    # print(pd.ExcelFile(a).sheet_names)
    dataframe_a = pd.read_excel(a, sheet_name='Лист1')
    dataframe_b = pd.read_excel(b, sheet_name="Лист1")
    # Выделение списков из таблиц
    series_a = set(dataframe_a['A'])
    series_b = set(dataframe_b["A"])
    # Выбор действия
    match n:
        # логический оператор множеств И
        case 0:
            # result = series_a[series_a.isin(series_b)].tolist()
            result = series_a & series_b
        # логический оператор множеств ИЛИ
        case 1:
            result = series_a | series_b
        # логический оператор множеств РАЗНОСТЬ
        case 2:
            result = series_a - series_b
        # логический оператор множеств СИММЕТРИЧНАЯ РАЗНОСТЬ
        case 3:
            result = series_a ^ series_b
    return result