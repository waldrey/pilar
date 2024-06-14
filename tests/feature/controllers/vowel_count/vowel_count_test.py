import pytest

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_count_vowels_without_words():
	response = client.post('/vowel_count/', json={})
	assert response.status_code == 404
	assert response.json() == {}


@pytest.mark.parametrize(
	'words, expected',
	[
		({'words': ['batman', 'robin', 'coringa']}, {'batman': 2, 'robin': 2, 'coringa': 3}),
		({'words': ['banana', 'onibus', 'poste']}, {'banana': 3, 'robin': 3, 'coringa': 2}),
		({'words': ['tv', 'sapato', 'rato', 'lado']}, {'tv': 0, 'sapato': 3, 'rato': 2, 'lado': 2}),
	],
)
def test_count_vowels(words, expected):
	response = client.post('/vowel_count/', json=words)
	assert response.status_code == 200
	assert response.json() == expected
