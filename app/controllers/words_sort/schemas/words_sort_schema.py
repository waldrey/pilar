from pydantic import BaseModel
from typing import List, Literal


class WordsSortSchema(BaseModel):
	words: List[str]
	order: Literal['asc', 'desc']
