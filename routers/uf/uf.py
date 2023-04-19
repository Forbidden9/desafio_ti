import datetime
from datetime import date

from fastapi import APIRouter, HTTPException, status


from utils.scrape import get_value_x_date

uf = APIRouter()


@uf.get('/search_value_x_date/')
async def search_value_x_date(date: date):
    new_date = datetime.date(2013, 1, 1)
    if date < new_date:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La fecha mínima que se puede consultar es el 01-01-2013")

    year = date.year
    month = date.month
    day = date.day

    value_x_date = get_value_x_date(year, month - 1, day - 1)

    return {'status': status.HTTP_200_OK, 'date': date, 'unidad de fomento': value_x_date}

