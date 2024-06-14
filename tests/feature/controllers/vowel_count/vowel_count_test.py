import pytest
import random

from http import HTTPStatus
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_count_vowels_content_type_different_app_json():
	content_types = [
		'application/xml',
		'text/plain',
		'multipart/form-data',
		'application/x-www-form-urlencoded',
		'application/pdf',
	]

	content_type = random.choice(content_types)

	response = client.post(url='/vowel_count/', json={}, headers={'Content-Type': content_type})
	assert response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE
	assert response.json() == {'message': 'Use application/json as Content-Type'}


def test_count_vowels_without_words():
	response = client.post('/vowel_count/', json={})
	assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_count_vowels_words_empty():
	response = client.post('/vowel_count/', json={'words': []})
	assert response.status_code == HTTPStatus.OK
	assert response.json() == {}


@pytest.mark.parametrize(
	'words, expected',
	[
		({'words': ['batman', 'robin', 'coringa']}, {'batman': 2, 'robin': 2, 'coringa': 3}),
		({'words': ['banana', 'onibus', 'poste']}, {'banana': 3, 'onibus': 3, 'poste': 2}),
		({'words': ['tv', 'sapato', 'rato', 'lado']}, {'tv': 0, 'sapato': 3, 'rato': 2, 'lado': 2}),
	],
)
def test_count_vowels(words, expected):
	response = client.post('/vowel_count/', json=words)
	assert response.status_code == HTTPStatus.OK
	assert response.json() == expected
