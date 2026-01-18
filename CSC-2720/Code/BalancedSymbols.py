from utils import ArrayStack


def isValidSymbolString(str):
    s = ArrayStack()
    balanced = True
    index = 0
    while index < len(str) and balanced:
        symbol = str[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(sym1, sym2):
    opens = "([{"
    closers = ")]}"
    return opens.index(sym1) == closers.index(sym2)


print(isValidSymbolString("{({([][])}())}"))
print(isValidSymbolString("[{()]"))
