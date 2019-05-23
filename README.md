# [LeetCode][leetcode]

![LeetCodeLogo](assets/images/leetcode_logo.png)


## Description

This repository is a collection of solutions for [LeetCode][leetcode] problems.


## Dependencies

* [Pipenv][pipenv]

### End to End test

* [RubyGem][rubygem]
* [Bundle][bundle]
* [Cucumber][cucumber]
* [Aruba][aruba]


## Build

### Solutions

```pipenv shell```

This command will create and activate a virtualenvironment wrapper. Make sure
[Pipenv][pipenv] tool is installed.

```pipenv install```

This command will install all the expected Python dependencies. Make sure the
virtualenvironment is already activated.


### Testing

#### End to End test

```bundle```

This command will install the [Cucumber][cucumber] and [Aruba][aruba]
dependencies. Make sure [RubyGem][rubygem] and [Bundle][bundle] are installed.


## Commands


```make end-to-end-test```

This command will run all the end to end tests. Make sure you have performed the
build step for End to end tests.


[leetcode]: https://leetcode.com
[cucumber]: https://cucumber.io
[aruba]: https://app.cucumber.pro/projects/aruba
[pipenv]: https://pipenv.readthedocs.io/en/latest/
