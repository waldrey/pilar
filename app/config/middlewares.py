from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.config.routes import validate_content_type


async def middleware_validate_content_type(request: Request, call_next):
	try:
		validate_content_type(request)
	except HTTPException as exc:
		return JSONResponse(
			status_code=exc.status_code,
			content={'message': exc.detail},
		)
	response = await call_next(request)
	return response
