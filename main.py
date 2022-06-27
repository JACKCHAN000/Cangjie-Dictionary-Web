import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import cangjie

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse('index.html',
                                      context={
                                          'request': request,
                                          'result': ''
                                      })


@app.post('/')
async def form_post(request: Request, search_query: str = Form(' ')):
    print(search_query)
    if search_query == ' ':
        print('No search query')
        return templates.TemplateResponse('index.html', {
            'request': request,
            'search_query': ' ',
            'result': ''
        })
    else:
        result = cangjie.cangjie(search_query)
        return templates.TemplateResponse('index.html',
                                          context={
                                              'request': request,
                                              'search_query': search_query,
                                              'result': result
                                          })


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)