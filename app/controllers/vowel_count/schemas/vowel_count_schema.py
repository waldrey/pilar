from pydantic import BaseModel
from typing import List


class VowelCountSchema(BaseModel):
	words: List[str]
