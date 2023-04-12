from fastapi import APIRouter
from datetime import date

router = APIRouter()


@router.post('/income', summary='新增收入记录')
def income():
    return '收入接口...'


@router.post('/outlay', summary='新增支出记录')
def outlay():
    return '支出接口...'


@router.post('/list', summary='查询收入支出数据列表')
def query_list():
    return '查询收入支出数据列表'


@router.post('/list_by_day', summary='查询指定某一天的消费记录')
def list_by_day(
    date: date = None
):
    return '获取当天消费记录'



@router.post('/list_by_current_month', summary='获取当前月的数据')
def list_by_current_month():
    return {
        "income": 300,
        "outlay": 400
    }





