from fastapi import APIRouter

router = APIRouter()


@router.post('/login', summary="用户登录接口")
def login(
        username: str = '',
        password: str = ''
):
    return "test..."


@router.post('/register', summary="用户注册接口")
def register(
        username: str = '',
        password: str = '',
        password2: str = ''
):
    return "test..."


@router.post('/info', summary='获取当前登陆的用户信息')
def user_info():
    return '当前登陆的用户信息'
