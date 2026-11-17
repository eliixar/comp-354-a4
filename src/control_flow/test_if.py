"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_conditional_expression():
    """Conditional expressions (the "ternary" if).

    A conditional expression has the form `value_if_true if condition else value_if_false`.
    It lets us choose between two values on a single line instead of writing a full
    if ... else block.
    """

    number = 7

    if number % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'

    assert parity == 'odd'

    assert ('even' if number % 2 == 0 else 'odd') == 'odd'
    assert ('even' if 10 % 2 == 0 else 'odd') == 'even'

    labels = ['even' if n % 2 == 0 else 'odd' for n in range(4)]
    assert labels == ['even', 'odd', 'even', 'odd']
