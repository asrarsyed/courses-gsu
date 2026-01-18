from utils import ArrayStack


def is_matched_html(html):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = html.find("<")  # find first '<' character (if any)
    while j != -1:
        k = html.find(">", j + 1)  # find next '>' character
        if k == -1:
            return False  # invalid tag
        tag = html[j + 1 : k]  # strip away < >
        if not tag.startswith("/"):  # this is opening tag
            S.push(tag)
        else:  # this is closing tag
            if S.is_empty():
                return False  # nothing to match with
            if tag[1:] != S.pop():
                return False  # mismatched delimiter
        j = html.find("<", k + 1)  # find next '<' character (if any)
    return S.is_empty()  # were all opening tags matched?


html = """<html>
    <h1>
        Stacks
    </h1>
    <body>
        CSC2720 - Data Structures
        <p>
            Problem solving using stack. List of problems:
        </p>
        <ol>
            <li>Convert Decimal to Binary</li>
            <li>Postfix expression evaluation</li>
            <li>Balanced Symbols</li>
        </ol>
    </body>
</html>"""

print(is_matched_html(html))
