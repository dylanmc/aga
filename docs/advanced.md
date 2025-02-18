# Advanced Features

## Prizes

If you want finer control over the points allocation of problems, you can add
points prizes to them, which let you run custom functions over the list of
completed tests in order to assign points values:

```python
from aga import problem, test_case
from aga.prize import prize, TcOutput, SubmissionMetadata

def all_correct(
    tests: list[TcOutput], _: SubmissionMetadata
) -> tuple[float, str]:
"""Check that all tests passed."""
    if all(t.is_correct() for t in tests):
        return 1.0, "Good work! You earned these points since all tests passed."
    else:
        return 0.0, "To earn these points, make sure all tests pass."

@prize(all_correct, name="Prize")
@test_case(0)
@test_case(2)
@problem()
def square(x: int) -> int:
    """Square x."""
		return x * x
```

If only one of the `0` or `2` test cases pass, the student will receive 1/3
credit for this problem. If both pass, they will receive full credit.

We provide more details and several pre-written prize functions in the
`prize`(reference.html#module-aga.prize) documentation.
