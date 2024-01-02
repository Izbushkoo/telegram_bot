from typing import List
import unittest


def handle_response_text(full_response: str) -> List[str]:

    max_length = 4096
    chunks = []
    while full_response:
        split_index = full_response[:max_length].rfind('.')
        if split_index == -1 or len(full_response) <= max_length:
            split_index = max_length if len(full_response) > max_length else len(full_response)
        else:
            split_index += 1

        chunks.append(full_response[:split_index])
        full_response = full_response[split_index:]

    return chunks


class TestHandleResponseText(unittest.TestCase):

    def test_short_string_no_dots(self):
        self.assertEqual(handle_response_text('Hello'), ['Hello'])

    def test_exact_length_string_no_dots(self):
        self.assertEqual(handle_response_text('a' * 4096), ['a' * 4096])

    def test_long_string_no_dots(self):
        text = 'a' * 5000
        expected = ['a' * 4096, 'a' * (5000 - 4096)]
        self.assertEqual(handle_response_text(text), expected)

    def test_string_with_dots(self):
        text = 'a.' * 3000
        expected = ['a.' * 2048, 'a.' * (3000 - 2048)]
        self.assertEqual(handle_response_text(text), expected)

    def test_string_no_dots_until_after_limit(self):
        text = 'a' * 4095 + '.'
        expected = ['a' * 4095 + '.']
        self.assertEqual(handle_response_text(text), expected)

    def test_empty_string(self):
        self.assertEqual(handle_response_text(''), [])


text_handler = handle_response_text


if __name__ == '__main__':
    unittest.main()
