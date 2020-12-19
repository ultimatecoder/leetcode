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


``` pipenv install --dev ```

This command will install required developer level dependencies. If your intent
is to run existing solutions then you are not required to perform this step.
This command is required if you want to run unit tests or verify that existing
code is bug free.


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
