from fastapi import FastAPI
import routers


app = FastAPI(
    title='记账系统API接口文档',
    description="记账系统API接口文档，巴拉巴拉",
    version="1.0.0"
)


app.include_router(routers.user, prefix='/user', tags=['用户相关接口'])
app.include_router(routers.account, prefix='/account', tags=['记账相关接口'])
