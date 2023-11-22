class StringWrapper():
    def __init__(self, value : str):
        self.value = value

    def length(self):
        count = 0
        for _ in self.value:
            count += 1
        return count

    def reverse(self):
        reversed_str = ""
        for char in self.value:
            reversed_str = char + reversed_str
        return reversed_str

    def is_palindrome(self):
        clean_str = ''.join(c for c in self.value if c.isalnum()).lower()
        return clean_str == clean_str[::-1]

    def count_occurrences(self, substring):
        count = 0
        index = self.value.find(substring)
        while index != -1:
            count += 1
            index = self.value.find(substring, index + 1)
        return count

    def replace_substring(self, old_substring, new_substring):
        result = ""
        index = 0
        while index < len(self.value):
            next_index = self.value.find(old_substring, index)
            if next_index == -1:
                result += self.value[index:]
                break
            result += self.value[index:next_index] + new_substring
            index = next_index + len(old_substring)
        return result