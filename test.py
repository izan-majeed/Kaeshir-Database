from database import data


def find(word: str):
    assert word.isalpha(), "You might be a Haput, else you could have entered a correct word."
    word = word.lower()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        key = data[mid]['title'].lower()
        if key > word:
            end = mid - 1
        elif key < word:
            start = mid + 1
        elif key == word:
            return {k: data[mid][k] for k in ('title', 'pos', 'englishMeaning', 'kashmiriMeaning')}

    return "Not Found"
