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

	@staticmethod
	def word_sort(words: List[str], order: str) -> List[str]:
		WordsService.quick_sort(words)

		if order == 'asc':
			return words

		return words[::-1]

	def quick_sort(_list: List, start=0, end=None):
		if end is None:
			end = len(_list) - 1
		if start < end:
			middle_partition = WordsService.middle_list(_list, start, end)
			WordsService.quick_sort(_list, start, middle_partition - 1)
			WordsService.quick_sort(_list, middle_partition + 1, end)

	def middle_list(_list, start, end):
		pivot = _list[end]
		firstNode = start
		for nextNode in range(start, end):
			if _list[nextNode] <= pivot:
				_list[nextNode], _list[firstNode] = _list[firstNode], _list[nextNode]
				firstNode = firstNode + 1
		_list[firstNode], _list[end] = _list[end], _list[firstNode]
		return firstNode
