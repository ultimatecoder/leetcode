# Commands


``` make end-to-end-test ```

This command will run all the end to end tests. Make sure you have performed the
build step for End to end tests.

``` make lint ```

Performs multiple checks. First it runs a static type checker [Mypy][mypy] which
will perform the type checking for given code. Make sure the [Mypy][mypy] is
installed.

``` make unit-test ```

It will run all the unit tests for existing solutions. Make sure
[Pytest][pytest] is already installed.


[mypy]: http://mypy-lang.org/
[pytest]: pytest.org
