from fastapi import APIRouter
from app.controllers.words_sort.schemas.words_sort_schema import WordsSortSchema
from app.domains.words.words_service import WordsService

router = APIRouter()


@router.post(path='/sort', tags=['Words'])
def sort(body: WordsSortSchema):
	"""
	Sort endpoint.
	> Endpoint responsável por ordenar a listagem de palavras recebida tanto asc quanto desc são aceitos como parâmetros.
	"""
	return WordsService.word_sort(body.words, body.order)
