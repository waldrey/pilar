import pytest
import random

from http import HTTPStatus
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_words_sort_content_type_different_app_json():
	content_types = [
		'application/xml',
		'text/plain',
		'multipart/form-data',
		'application/x-www-form-urlencoded',
		'application/pdf',
	]

	content_type = random.choice(content_types)

	response = client.post(url='/sort/', json={}, headers={'Content-Type': content_type})
	assert response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE
	assert response.json() == {'message': 'Use application/json as Content-Type'}


def test_count_vowels_without_words():
	response = client.post('/sort/', json={})
	assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_words_sort_without_order():
	response = client.post('/sort/', json={'words': []})
	assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
	assert response.json() == {
		'detail': [{'type': 'missing', 'loc': ['body', 'order'], 'msg': 'Field required', 'input': {'words': []}}]
	}


@pytest.mark.parametrize(
	'payload_words, expected',
	[
		({'words': ['batman', 'robin', 'coringa'], 'order': 'asc'}, ['batman', 'coringa', 'robin']),
		({'words': ['batman', 'robin', 'coringa'], 'order': 'desc'}, ['robin', 'coringa', 'batman']),
		({'words': ['banana', 'onibus', 'poste'], 'order': 'asc'}, ['banana', 'onibus', 'poste']),
		({'words': ['tv', 'sapato', 'rato', 'lado'], 'order': 'asc'}, ['lado', 'rato', 'sapato', 'tv']),
	],
)
def test_words_sort(payload_words, expected):
	response = client.post('/sort/', json=payload_words)
	assert response.status_code == HTTPStatus.OK
	assert response.json() == expected
