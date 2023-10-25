import datetime


spreadsheet_body = {
    'properties': {'title': f'Отчет на {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
                   'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист1',
                               'gridProperties': {'rowCount': 100,
                                                  'columnCount': 11}}}]
}