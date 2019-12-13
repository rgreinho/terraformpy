# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

* Format the code with `black`.
* Package the application with PBR:
  * Make packaging clearer.
  * Get rid of `VERSION` file and use git tag instead.
  * Separate development and production requirements.
* Use invoke and nox to setup administration and CI tasks.
  * Add linters (flake8, pydocstyle, pylint).
  * Add extra pytest plugins.
* Remove Python 2 support. The new minimum required version is now `3.7`.
* Format the Changelog according to the Keep A Changelog specification.
* Use a `.github` folder to store .github configuration files
  * issues and PR templates
  * label definitions
  * stale bot configuration
  * contributing guidelines
* Generate the documentation using Sphinx and the aiohttp theme

## [1.2.1]

* Add support for HCL modules via the new `Module` object

## [1.2.0]

* Support Python 3.5+

## [1.1.3]

* Fix distribution, we need to include the `VERSION` file

## [1.1.2]

Fix `get_mock_object()` for `ResourceCollection`

## [1.1.1]

Publish via CircleCI

## [1.1.0]

First open source release, no changes from 1.0.8

## [1.0.8]

Update TypedObjecAttr to build dot-separated strings for ${resource-type.resource.attribute.key-name} value access.

## [1.0.7]

Update TypedObjecAttr to build itself recursively.

## [1.0.6]

Update TypedObjecAttr to format for integer-based arrays.

## [1.0.5]

Added OrderedDictionary schema type

## [1.0.4]

Ensure DuplicateKey hash is monotonically increasing for stablesorting purposes

## [1.0.3]

Allow ResourceCollection to be used in ModelType fields

## [1.0.2]

Ensure the TypedObjecAttr class, added in 1.0.1, works as StringType inputs in ResourceCollection

## [1.0.1]

* Add support for map indices access: https://www.terraform.io/docs/configuration/expressions.html#indices-and-attributes

## [1.0.0]

* **BREAKING** - The `Input()` primitive originally shipped with terraformpy is now fully deprecated.
  All inputs must be defined as schematics types.
* `ResourceCollection` is now a specialized subclass of a schematics `Model`

## [0.0.37]

* Support Schematics style field level validation (#33)
* Add a changelog

[//]: # (Release links)
[0.0.37]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v0.0.37
[1.0.0]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.0.0
[1.0.1]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.0.1
[1.0.2]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.0.2
[1.0.3]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.0.3
[1.0.4]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.0.4
[1.0.5]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.0.5
[1.0.6]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.0.6
[1.0.7]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.0.7
[1.0.8]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.0.8
[1.1.0]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.1.0
[1.1.1]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.1.1
[1.1.2]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.1.2
[1.1.3]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.1.3
[1.2.0]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.2.0
[1.2.1]: https://github.com/NerdWalletOSS/terraformpy/releases/tag/v1.2.1

[//]: # (Issue/PR links)
[#33]: https://github.com/NerdWalletOSS/terraformpy/pull/33
