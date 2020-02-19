import random
import string


def random_string(minlen=1, maxlen=255, spaces=False, whitespases=False):
    length = random.randint(minlen, maxlen)
    symbols = string.ascii_letters + string.digits + string.punctuation
    if spaces:
        symbols += ' ' * 10
    if whitespases:
        symbols += string.whitespace[:-2]
    result = ''.join(random.choices(symbols, k=length))
    return result


if __name__ == "__main__":
    print(random_string(spaces=True))
