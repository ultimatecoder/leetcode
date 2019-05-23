# Build

## Dependencies

* [Pipenv][pipenv]

### Test

#### Type checker

* [Mypy][mypy]

#### Unit

* [Pytest][pytest]

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

#### End to End test

``` bundle ```

This command will install the [Cucumber][cucumber] and [Aruba][aruba]
dependencies. Make sure [RubyGem][rubygem] and [Bundler][bundler] are installed.


[cucumber]: https://cucumber.io
[aruba]: https://app.cucumber.pro/projects/aruba
[rubygem]: https://rubygems.org/
[pipenv]: https://pipenv.readthedocs.io/en/latest/
[bundler]: https://bundler.io/
[mypy]: http://mypy-lang.org/
[pytest]: pytest.org
