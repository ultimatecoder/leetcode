# [LeetCode][leetcode]

![LeetCodeLogo](assets/images/leetcode_logo.png)


## Description

This repository is a collection of solutions for [LeetCode][leetcode] problems.


## Dependencies

* [Pipenv][pipenv]

### Test

#### Type checker

* [Mypy][mypy]

#### End to End

* [RubyGem][rubygem]
* [Bundler][bundler]
* [Cucumber][cucumber]
* [Aruba][aruba]


## Build

### Solutions

```pipenv shell```

This command will create and activate a virtualenvironment wrapper. Make sure
[Pipenv][pipenv] tool is installed.

``` pipenv install ```

This command will install all the expected Python dependencies. Make sure the
virtualenvironment is already activated.


### Testing

#### Static Type checker


#### End to End test

``` bundle ```

This command will install the [Cucumber][cucumber] and [Aruba][aruba]
dependencies. Make sure [RubyGem][rubygem] and [Bundler][bundler] are installed.


## Commands


``` make end-to-end-test ```

This command will run all the end to end tests. Make sure you have performed the
build step for End to end tests.

``` make lint ```

Performs multiple checks. First it runs a static type checker [Mypy][mypy] which
will perform the type checking for given code. Make sure the [Mypy][mypy] is
installed.


[leetcode]: https://leetcode.com
[cucumber]: https://cucumber.io
[aruba]: https://app.cucumber.pro/projects/aruba
[rubygem]: https://rubygems.org/
[pipenv]: https://pipenv.readthedocs.io/en/latest/
[bundler]: https://bundler.io/
[mypy]: http://mypy-lang.org/
