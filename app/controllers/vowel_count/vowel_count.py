from fastapi import APIRouter
from app.controllers.vowel_count.schemas.vowel_count_schema import VowelCountSchema
from app.domains.words.words_service import WordsService

router = APIRouter()


@router.post(
	path='/vowel_count',
	tags=['Words'],
	responses={
		200: {
			'description': 'Successful response',
			'content': {'application/json': {'example': {'batman': 2, 'robin': 2, 'coringa': 3}}},
		}
	},
)
def vowel_count(body: VowelCountSchema):
	"""
	Vowel Count endpoint.
	> Endpoint responsável por contabilizar a quantidade de vogais que as palavras enviadas possuem
	e retornar a palavra como chave e o valor a quantidade de vogais.
	"""
	return WordsService.vowel_count(body.words)
