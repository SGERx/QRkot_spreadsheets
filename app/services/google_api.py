from datetime import datetime

from aiogoogle import Aiogoogle
import copy

from app.core.config import settings
from app.services.my_json import spreadsheet_body


FORMAT = "%Y/%m/%d %H:%M:%S"


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:

    service = await wrapper_services.discover('sheets', 'v4')

    now_date_time = datetime.now()
    current_spreadsheet_body = copy.deepcopy(spreadsheet_body)
    current_spreadsheet_body['properties']['title'] = f'Отчет на {now_date_time}'

    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=current_spreadsheet_body)
    )
    spreadsheetid = response['spreadsheetId']
    return spreadsheetid


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheetid: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')

    table_values = [
        ['Отчет от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]

    for res in projects:
        new_row = [
            res['name'],
            res['delta'],
            res['description']
        ]
        table_values.append(new_row)

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values,
        'range': 'Лист1!A1:E30'
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )