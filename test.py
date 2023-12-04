from pydantic import BaseModel
class CookiesItem(BaseModel):
    name:str # cookie名称
    value:str # cookie值
    domain:str # cookie指向的域名
    path:str # cookie指向郁域名路径
    
class CookiesItemDto(BaseModel):
    domain:str # cookie指向的域名
    path:str # cookie指向郁域名路径
    
    