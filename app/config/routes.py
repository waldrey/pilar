from fastapi import HTTPException, Request


def validate_content_type(request: Request):
	if request.headers.get('Content-Type') != 'application/json':
		raise HTTPException(status_code=415, detail='Use application/json as Content-Type')
