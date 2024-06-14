from http import HTTPStatus
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_exception_route_not_found():
	response = client.get(url='/fake-route/')
	assert response.status_code == HTTPStatus.NOT_FOUND
	assert response.json() == {'message': 'Route not found'}


def test_exception_method_not_allowed():
	response = client.get(url='/vowel_count/')
	assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
	assert response.json() == {'message': 'Method not allowed'}


def test_redirect_docs():
	response = client.get(url='/')
	assert response.status_code == HTTPStatus.OK
	assert response.request.url.path.endswith('/docs')
