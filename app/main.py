import os

from http import HTTPStatus
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from app.controllers.vowel_count import vowel_count
from app.config.middlewares import middleware_validate_content_type

load_dotenv()

app = FastAPI(title=os.getenv('APP_NAME', 'Pilar API'))
app.include_router(vowel_count.router)


@app.middleware('http')
async def middleware_wrapper(request: Request, call_next):
	if request.method not in ['GET']:
		return await middleware_validate_content_type(request, call_next)
	else:
		response = await call_next(request)
		return response


@app.exception_handler(HTTPStatus.NOT_FOUND)
async def not_found_exception_handler(request, exc):
	return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={'message': 'Route not found'})


@app.exception_handler(HTTPStatus.METHOD_NOT_ALLOWED)
async def method_not_allowed_exception_handler(request, exc):
	return JSONResponse(status_code=HTTPStatus.METHOD_NOT_ALLOWED, content={'message': 'Method not allowed'})


@app.get('/', include_in_schema=False)
def root():
	return RedirectResponse(url='/docs')
