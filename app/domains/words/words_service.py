import re
from typing import List, Dict


class WordsService:
	@staticmethod
	def vowel_count(words: List[str]) -> Dict[str, int]:
		vowels_result: Dict[str, int] = {}

		vowel_patterns = re.compile(r'[aeiou]')

		for word in words:
			vowels_result[word] = len(vowel_patterns.findall(word.lower()))

		return vowels_result
