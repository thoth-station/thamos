
## Release 1.27.2 (2022-03-01T16:32:36)
* Increase thamos timeout to 45 minutes
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment

## Release 1.27.1 (2022-02-28T11:58:57)
* Fix thamos venv not printing virtualenv path
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Make mypy happy by not overriding config dict
* Add missing rich-click config file
* Use runtime_environment_name option in the config file
* Remove rm-build-container-image.sh
* Print thamos check results only if any result reported

## Release 1.27.0 (2022-02-21T23:31:30)
* Add rich-click to requirements
* Use rich-click to create stylized help
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment

## Release 1.26.1 (2022-02-15T22:52:17)
* Report if configuration check passes
* Respect runtime environments in commands
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Add myself to reviewers
* Relax verbosity in messages logged in the discover module

## Release 1.26.0 (2022-02-07T11:37:36)
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Introduce pedantic runs

## Release 1.25.1 (2022-02-02T09:15:10)
* Add myself to maintainers
* Fix list_thoth_container_images parameter
* Update thamos/lib.py
* Add missing parameters when querying container images
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Add example to thamos images for retrieving images with a symbol
* Add new query parameters to thamos images
* Update PR template for new module release

## Release 1.25.0 (2022-01-26T10:25:22)
* Handle cases when CPU detection fails
* Provide short help to fit terminal width
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Fix typo in docstring of the parameter
* Add metavar for source path
* Enable TLS verification
* Report import errors for whatprovides and discover too
* Exception chaining and log message on one line
* Reformatting
* Register thamos exception for no matching package and handle json.loads errors
* Raise a Thamos specific error
* Decode response body
* Make error message more concise
* Fix whatprovides output for Not Found Error
* Report can be null when adviser fails on OOM
* Remove config_path property from configuration class

## Release 1.24.0 (2022-01-13T16:27:17)
* Add missing files
* Update swagger-client and documentation
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Check what type of document users ask when performing thamos graph
* Fix message reported
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Do not include std imports and builtins in thamos discover
* Choose spinners, wisely
* Provide more user-friendly reporting of environments available
* Make sure the import reports are unified
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Adjust reporting when `thamos discover' does not find any package
* A minor fix in docstring
* Use dash instead of underscore in options
* Implement translation for table keys and thamos images report
* Unify table reported when `thamos indexes' called
* Fix typo
* Unify table reported when `thamos status' called
* Unify table reported when `thamos check' called
* Introduce thamos verify command to check lockfile hash
* Add a new command to verify that the lock file is up to date
* Parametrize obtaining images
* Add Maya to OWNERS
* Update documentation stating environments and images
* pre-commit
* Make type hint more precise
* Fix type hint for list_thoth_container_images
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Respect nullable values in container-images response
* Update GitHub issue templates

## Release 1.23.0 (2022-01-05T08:32:58)
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Update client library
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Use single char short configuration options

## Release 1.22.0 (2021-12-16T12:32:42)
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Allow specifying labels in Thoth's configuration file
* Provide environments subcommand
* Update swagger client
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Provide metavar to options
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment

## Release 1.21.1 (2021-11-29T13:25:21)
* Show an example with imports with a star

## Release 1.21.0 (2021-11-24T14:36:49)
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* fix type input parameter for print_report method
* Improve error message
* adjust output for what provides and remove fix index
* add kebechet to crossroads in docs
* create method for add requirement
* Add logic to provide verified packages
* Add whatprovides and discover commands
* Corrected return type
* Update command `thamos whatprovides` and `thamos discover`
* create get_package_from_imported packages api call and thamos whatprovides command
* Started creating  command
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Regenerate thamos client library
* Update swagger client
* Provide container images sub-command
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Drop hardware subcommand
* Swagger fixed code generation path
* Swagger codegen dropped branch and created a tag instead
* Aggregate also standard imports from user's code
* Fix support command if no last analysis id is found
* Fix support command that calls discover methods
* Remove examples/ directory, use thoth-station/cli-examples repo
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Use https in pre-commit repo links
* Update the labels of bug/rfe issue templates
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Remove redundant cwd
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Regenerate client to respect API endpoints recently added
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Fold dependency graph shown by default
* :arrow_up: Automatic update of dependencies by Kebechet
* :arrow_up: Automatic update of dependencies by Kebechet

## Release 0.1.0 (2018-12-19T11:47:49)
* Use contoml instead of toml, it has prettier output
* Warn on using insecure network without TLS
* Provide some defaults for runtime environmnet configuration
* Remove no longer relevant TODO
* Perform API discovery when communicating with remote
* Remove unused parameters to CLI commands
* Propagate error in report to process exit code
* Give user guidance on how to configure thamos
* Regenerate thamos swagger client
* Add guards to library functions
* CLI always uses the highest rated software stack
* Serialize into a file correctly
* Remove invalid parameter to TOML
* Automatic update of dependency six from 1.11.0 to 1.12.0
* Automatic update of dependency certifi from 2018.10.15 to 2018.11.29
* Wrong index was on server side
* Fix report indexing
* Fix missing parameter
* Propagate force parameters to bypass server-side cache
* Point to upshift test environment by default
* Add long description for PyPI
* Update to correctly propagate runtime environment
* Update swagger client with hardware info on input
* Make CI happy again
* Adjust library's advise implementation for current implementation
* Update to reflect the current API implementation
* Automatic update of dependency texttable from 1.4.0 to 1.5.0
* Automatic update of dependency urllib3 from 1.24 to 1.24.1
* Do not use trailing slash in url
* Automatic update of dependency python-dateutil from 2.7.4 to 2.7.5
* use thoth-* jobs in pipeline
* added .vscode/
* Automatic update of dependency python-dateutil from 2.7.3 to 2.7.4
* Automatic update of dependency urllib3 from 1.23 to 1.24
* Automatic update of dependency thoth-analyzer from 0.0.7 to 0.1.0
* We use JSON as an output format
* Regenerate client to include dependency monkey API
* Logs can be nullable
* Introduce --no-wait flag for not waiting for analysis to finish
* Automatic update of dependency click from 6.7 to 7.0
* State properties are now model properties
* Regenerate swagger client
* Delete strict checks in nullable values
* Use yaml.safe_load due to security reasons
* Supress details from reports in table output
* Print nested dicts nicely in the provenance report
* Omit redundant findings key in the provenance report
* Omit redundant findings key in the provenance report
* Make runtime environment a parameter to CLI
* Center package name and package version in response
* Initial dependency lock
* Return code 4 is no more missing
* Fix linter complains
* Final bits in initial working implementation
* Initial implementation of CLI
* Regenerate swagger client based on the current state
* Regenerate swagger client with new response models
* removed the markdown bear as it depends on some npm tools
* more linter fixes
* missing newline
* preparing for coala
* added a job for creating releases
* added the missing coala config
* added github and zuul configs
* Initial implementation

## Release 0.2.0 (2019-02-27T13:47:22)
* Fix Coala issues
* Automatic update of dependency texttable from 1.6.0 to 1.6.1
* a basic lockdown example
* Remove redundant parentheses
* Introduce output formats for Thamos
* Automatic update of dependency thoth-analyzer from 0.1.0 to 0.1.2
* Add missing MANIFEST.in
* Perform autodiscovery for host runtime environment
* Use black for formatting
* Explicitly propagate recommendation type if user asked so
* Fix clash of options for CLI
* Submit runtime environments to Thoth
* Re-generate swagger client files
* Make configuration entries minimal
* Automatic update of dependency distro from 1.3.0 to 1.4.0
* Automatic update of dependency python-dateutil from 2.7.5 to 2.8.0
* Adjust configuration file structure based on comments
* Rename configuration to runtime_environments
* Make a list of configurations
* State requirements format in the config file
* Adjust structure of configuration file
* Introduce log and status sub-commands
* Introduce a way how to suppress TLS warnings
* It's already 2019
* Update README with lib/CLI instructions
* Adjust TLS verify property when thamos is used as a lib
* Provide routine for submitting and retrieving image analyses
* Automatic update of dependency yaspin from 0.14.0 to 0.14.1
* Automatic update of dependency texttable from 1.5.0 to 1.6.0
* Add missing requirements
* Fix exception happening if there was an error in analysis
* Release of version 0.1.0
* Use contoml instead of toml, it has prettier output
* Warn on using insecure network without TLS
* Provide some defaults for runtime environmnet configuration
* Remove no longer relevant TODO
* Perform API discovery when communicating with remote
* Remove unused parameters to CLI commands
* Propagate error in report to process exit code
* Give user guidance on how to configure thamos
* Regenerate thamos swagger client
* Add guards to library functions
* CLI always uses the highest rated software stack
* Serialize into a file correctly
* Remove invalid parameter to TOML
* Automatic update of dependency six from 1.11.0 to 1.12.0
* Automatic update of dependency certifi from 2018.10.15 to 2018.11.29
* Wrong index was on server side
* Fix report indexing
* Fix missing parameter
* Propagate force parameters to bypass server-side cache
* Point to upshift test environment by default
* Add long description for PyPI
* Update to correctly propagate runtime environment
* Update swagger client with hardware info on input
* Make CI happy again
* Adjust library's advise implementation for current implementation
* Update to reflect the current API implementation
* Automatic update of dependency texttable from 1.4.0 to 1.5.0
* Automatic update of dependency urllib3 from 1.24 to 1.24.1
* Do not use trailing slash in url
* Automatic update of dependency python-dateutil from 2.7.4 to 2.7.5
* use thoth-* jobs in pipeline
* added .vscode/
* Automatic update of dependency python-dateutil from 2.7.3 to 2.7.4
* Automatic update of dependency urllib3 from 1.23 to 1.24
* Automatic update of dependency thoth-analyzer from 0.0.7 to 0.1.0
* We use JSON as an output format
* Regenerate client to include dependency monkey API
* Logs can be nullable
* Introduce --no-wait flag for not waiting for analysis to finish
* Automatic update of dependency click from 6.7 to 7.0
* State properties are now model properties
* Regenerate swagger client
* Delete strict checks in nullable values
* Use yaml.safe_load due to security reasons
* Supress details from reports in table output
* Print nested dicts nicely in the provenance report
* Omit redundant findings key in the provenance report
* Omit redundant findings key in the provenance report
* Make runtime environment a parameter to CLI
* Center package name and package version in response
* Initial dependency lock
* Return code 4 is no more missing
* Fix linter complains
* Final bits in initial working implementation
* Initial implementation of CLI
* Regenerate swagger client based on the current state
* Regenerate swagger client with new response models

## Release 0.3.0 (2019-02-27T15:49:07)


## Release 0.3.1 (2019-03-18T16:21:21)
* Provide environment type in library adapter
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Regenerate client
* Target coala issues
* Do not write changes in configuration if there are no changes
* Adjust Thoth's configuration based on recommendations
* Regenerate swagger-client, add limit latest versions option
* Fix formatting
* Use safe_dump() instead of dump()
* Automatic dependency re-locking
* Add ability to expand entries in configuration file
* Add ability to create configuration in non-interactive mode
* Demo with lower flask version
* Move resolved stacks to misc repo
* Fix issues reported by coala
* Add files supporting "scoring" scenario
* Fix coala complains
* Add files supporting "scoring" scenario
* Add README for runtime environment scenario
* Remove requires section in example
* Minor improvements in README file
* Minor improvements in README file
* Add README file for lockdown example
* Add example flask application to verify stack works
* fixed the wrong version specifier
* Adjust recommendation type to latest
* all the use cases

## Release 0.4.0 (2019-05-08T17:25:11)
* Regenerate for new implementation
* Use openapi 3 implementation for swagger client generation
* Re-generate swagger client
* Integrate static analysis using Invectio
* :pushpin: Automatic update of dependency urllib3 from 1.24.2 to 1.24.3
* :pushpin: Automatic update of dependency yaspin from 0.14.1 to 0.14.2
* Re-generate for transition to Dgraph
* :pushpin: Automatic update of dependency urllib3 from 1.24.1 to 1.24.2
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* :sparkles: using -stage now, removed some quirks
* :sparkles: added a container build script and adjusted some readmes
* Log Thoth's API URL to show to which instance a user talks to
* bug fix on TLS turned on
* Used urljoin for maintaining semantic version of url
* Correctly handle errors from reports and empty reports
* Make sure configuration changes are propagated to config file
* Match operating system with solver results
* Pin down more dependencies
* Enable limit_latest_versions to be configured from configuration
* Update .thoth.yaml
* Fix Coala complains
* Adjust runtime-environment example to reflect data in Test environment
* Add Thoth's configuration file

## Release 0.4.1 (2019-05-08T18:43:04)
* Use arguments instead of kwargs to be compatible with openapi

## Release 0.4.2 (2019-05-23T18:55:41)
* Add missing Invectio requirement

## Release 0.4.3 (2019-06-14T13:17:14)
* :pushpin: Automatic update of dependency invectio from 0.0.1 to 0.0.3
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* :pushpin: Automatic update of dependency yaspin from 0.14.2 to 0.14.3
* :pushpin: Automatic update of dependency urllib3 from 1.24.3 to 1.25.3
* Include Thoth's configuration file for sdist distribution
* rm trailing white space
* Removed self keyword
* Remove api arg
* Accidental white space
* Forgot to remove arguments
* Forgot to remove arguments
* Manual formatting
* Auto format
* Provenance here lib function
* Use own user-agent for user requests
* Thamos Library advise_here (#159)
* Edit styling
* Edit styling
* python/black styling
* Pipfile.lock is not auto added
* No need to include API client in args
* Created library function for advising current directory
* State configuration option for disabling progressbar
* Adjust default Thoth host to talk to
* Provide ability to supply configuration file template
* Report warning if no library usage was gathered

## Release 0.5.0 (2019-06-24T09:04:03)
* Fix handling based on arguments if no config file is needed
* :pushpin: Automatic update of dependency certifi from 2019.3.9 to 2019.6.16

## Release 0.5.1 (2019-06-24T09:41:35)


## Release 0.5.2 (2019-06-24T10:18:20)


## Release 0.5.3 (2019-06-24T10:57:16)


## Release 0.5.4 (2019-07-03T13:20:37)
* Add `nowrite` parameter to create_default_config
* Remove trailing whitespace
* Added origin option to provenance and advise
* Make sure to follow recomendation type priority
* Fix issue #182
* :pushpin: Automatic update of dependency texttable from 1.6.1 to 1.6.2
* Update docs on how autogenerating code is done
* lib analysis results
* Fix URL to OpenAPI YAML

## Release 0.5.5 (2019-07-17T13:14:56)
* Fix issues with generated swagger client
* Remove trailing whitespace
* Fix propagation of `limit_latest_versions` parameter
* Round up maximum line length allowed for Coala
* Be more verbose about adviser input on debug
* Use test environment as a source for swagger client
* Regenerate swagger client
* Removed unecessary from get_analysis_results
* Duplicate origin param
* Added origin to advise
* Fixed
* auto swagger client generated
* Analysis ID is second argument
* Analysis ID is second argument

## Release 0.6.0 (2019-07-22T20:19:10)
* :boat: updated thamos with latest user-api
* :snail: supporting method for submitting whole build(imagestream and buildlog)
* :pushpin: Automatic update of dependency invectio from 0.0.3 to 0.0.4

## Release 0.7.0 (2019-08-11T16:54:02)
* :pushpin: Automatic update of dependency yaspin from 0.14.3 to 0.15.0
* :pushpin: Automatic update of dependency invectio from 0.0.6 to 0.0.7
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* :pushpin: Automatic update of dependency invectio from 0.0.5 to 0.0.6
* Document environment variables which can be used during s2i
* :pushpin: Automatic dependency re-locking
* Adjust status command to use the last analysis id
* Filter out calls to Python's standard library
* The configuration template can be user supplied
* Provide a way to note last analysis id into a temporary file
* Decrease maximum sleep time to be more responsive
* Propagate environment configuration in advise_here
* Expand configuration with environment variables
* Hot fix for accessing wrong variable
* Propagate library usage for all Python libraries
* Add ability to configure thamos using envvars
* Correctly propagate invectio version to user-api after library usage detection
* Be more descriptive with logged message about library usage
* :pushpin: Automatic update of dependency invectio from 0.0.4 to 0.0.5
* Fix issue if no report is generated by the recommendation engine

## Release 0.7.1 (2019-08-22T08:52:34)
* :sparkles: now using Fedora 30 and Python 3.7
* Use .coafile from adviser
* Add tests for checking serialization
* Switch from contoml to toml
* Adjust the exception message when file is not set
* State Pipfile is required
* We require Python 3.6+
* Always create config from template if template is set explictly

## Release 0.7.2 (2019-08-23T11:04:19)
* Add missing toml in requirements.txt

## Release 0.7.3 (2019-11-11T21:34:58)
* Adjust output visualization according to new adviser output
* save check for the stack-info
* update thamos with latest user-api
* use https protocol to access test user-api
* :pushpin: Automatic update of dependency six from 1.12.0 to 1.13.0
* :pushpin: Automatic update of dependency python-dateutil from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* Update .codeclimate.yml
* Create .codeclimate.yml
* Create .gitattributes
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Print out Thoth backend version on `thamos version'
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.3 to 0.1.4
* :pushpin: Automatic update of dependency urllib3 from 1.25.5 to 1.25.6
* Do not send empty library usage
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.2 to 0.1.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.4 to 1.25.5
* :pushpin: Automatic update of dependency urllib3 from 1.25.3 to 1.25.4
* :pushpin: Automatic update of dependency certifi from 2019.6.16 to 2019.9.11
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* Link to docs for specific node placement

## Release 0.7.4 (2019-11-11T23:22:21)
* Release of version 0.7.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.6 to 1.25.7


## Release 0.7.5 (2019-12-04T12:45:30)
* :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.4 to 0.1.5
* :pushpin: Automatic update of dependency certifi from 2019.9.11 to 2019.11.28
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* Release of version 0.7.4
* Advised runtime environment is now part of recommended product
* Release of version 0.7.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.6 to 1.25.7
* Adjust output visualization according to new adviser output
* save check for the stack-info
* update thamos with latest user-api
* use https protocol to access test user-api
* :pushpin: Automatic update of dependency six from 1.12.0 to 1.13.0
* :pushpin: Automatic update of dependency python-dateutil from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* Update .codeclimate.yml
* Create .codeclimate.yml
* Create .gitattributes
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Print out Thoth backend version on `thamos version'
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.3 to 0.1.4
* :pushpin: Automatic update of dependency urllib3 from 1.25.5 to 1.25.6
* Do not send empty library usage
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.2 to 0.1.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.4 to 1.25.5
* :pushpin: Automatic update of dependency urllib3 from 1.25.3 to 1.25.4
* :pushpin: Automatic update of dependency certifi from 2019.6.16 to 2019.9.11
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* Link to docs for specific node placement
* Release of version 0.7.2
* Add missing toml in requirements.txt
* Release of version 0.7.1
* Add missing test file
* Enable zuul-pytest on this repo
* :sparkles: now using Fedora 30 and Python 3.7
* Use .coafile from adviser
* Add tests for checking serialization
* Switch from contoml to toml
* Adjust the exception message when file is not set
* State Pipfile is required
* We require Python 3.6+
* Always create config from template if template is set explictly
* Release of version 0.7.0
* :pushpin: Automatic update of dependency yaspin from 0.14.3 to 0.15.0
* :pushpin: Automatic update of dependency invectio from 0.0.6 to 0.0.7
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* :pushpin: Automatic update of dependency invectio from 0.0.5 to 0.0.6
* Document environment variables which can be used during s2i
* :pushpin: Automatic dependency re-locking
* Adjust status command to use the last analysis id
* Filter out calls to Python's standard library
* The configuration template can be user supplied
* Provide a way to note last analysis id into a temporary file
* Decrease maximum sleep time to be more responsive
* Propagate environment configuration in advise_here
* Expand configuration with environment variables
* Hot fix for accessing wrong variable
* Propagate library usage for all Python libraries
* Add ability to configure thamos using envvars
* Correctly propagate invectio version to user-api after library usage detection
* Be more descriptive with logged message about library usage
* :pushpin: Automatic update of dependency invectio from 0.0.4 to 0.0.5
* Fix issue if no report is generated by the recommendation engine
* Release of version 0.6.0
* :boat: updated thamos with latest user-api
* :snail: supporting method for submitting whole build(imagestream and buildlog)
* :pushpin: Automatic update of dependency invectio from 0.0.3 to 0.0.4
* Release of version 0.5.5
* Fix issues with generated swagger client
* Remove trailing whitespace
* Fix propagation of `limit_latest_versions` parameter
* Round up maximum line length allowed for Coala
* Be more verbose about adviser input on debug
* Use test environment as a source for swagger client
* Regenerate swagger client
* Removed unecessary from get_analysis_results
* Duplicate origin param
* Added origin to advise
* Fixed
* Release of version 0.5.4
* Add `nowrite` parameter to create_default_config
* auto swagger client generated
* Analysis ID is second argument
* Analysis ID is second argument
* Remove trailing whitespace
* Added origin option to provenance and advise
* Make sure to follow recomendation type priority
* Fix issue #182
* :pushpin: Automatic update of dependency texttable from 1.6.1 to 1.6.2
* Update docs on how autogenerating code is done
* lib analysis results
* Fix URL to OpenAPI YAML
* Release of version 0.5.3
* Release of version 0.5.2
* Release of version 0.5.1
* Release of version 0.5.0
* Fix handling based on arguments if no config file is needed
* :pushpin: Automatic update of dependency certifi from 2019.3.9 to 2019.6.16
* Release of version 0.4.3
* :pushpin: Automatic update of dependency invectio from 0.0.1 to 0.0.3
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* :pushpin: Automatic update of dependency yaspin from 0.14.2 to 0.14.3
* :pushpin: Automatic update of dependency urllib3 from 1.24.3 to 1.25.3
* Include Thoth's configuration file for sdist distribution
* rm trailing white space
* Removed self keyword
* Remove api arg
* Accidental white space
* Forgot to remove arguments
* Forgot to remove arguments
* Manual formatting
* Auto format
* Provenance here lib function
* Use own user-agent for user requests
* Thamos Library advise_here (#159)
* Edit styling
* Edit styling
* python/black styling
* Pipfile.lock is not auto added
* No need to include API client in args
* Created library function for advising current directory
* State configuration option for disabling progressbar
* Adjust default Thoth host to talk to
* Provide ability to supply configuration file template
* Report warning if no library usage was gathered
* Release of version 0.4.2
* Add missing Invectio requirement
* Release of version 0.4.1
* Use arguments instead of kwargs to be compatible with openapi
* Release of version 0.4.0
* Regenerate for new implementation
* Use openapi 3 implementation for swagger client generation
* Re-generate swagger client
* Integrate static analysis using Invectio
* :pushpin: Automatic update of dependency urllib3 from 1.24.2 to 1.24.3
* :pushpin: Automatic update of dependency yaspin from 0.14.1 to 0.14.2
* Re-generate for transition to Dgraph
* :pushpin: Automatic update of dependency urllib3 from 1.24.1 to 1.24.2
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* :sparkles: using -stage now, removed some quirks
* :sparkles: added a container build script and adjusted some readmes
* Log Thoth's API URL to show to which instance a user talks to
* bug fix on TLS turned on
* Used urljoin for maintaining semantic version of url
* Correctly handle errors from reports and empty reports
* Make sure configuration changes are propagated to config file
* Match operating system with solver results
* Pin down more dependencies
* Enable limit_latest_versions to be configured from configuration
* Update .thoth.yaml
* Fix Coala complains
* Adjust runtime-environment example to reflect data in Test environment
* Release of version 0.3.1
* Add Thoth's configuration file
* Provide environment type in library adapter
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Regenerate client
* Target coala issues
* Do not write changes in configuration if there are no changes
* Adjust Thoth's configuration based on recommendations
* Regenerate swagger-client, add limit latest versions option
* Fix formatting
* Use safe_dump() instead of dump()
* Automatic dependency re-locking
* Add ability to expand entries in configuration file
* Add ability to create configuration in non-interactive mode
* Demo with lower flask version
* Move resolved stacks to misc repo
* Fix issues reported by coala
* Add files supporting "scoring" scenario
* Fix coala complains
* Add files supporting "scoring" scenario
* Add README for runtime environment scenario
* Remove requires section in example
* Minor improvements in README file
* Minor improvements in README file
* Add README file for lockdown example
* Add example flask application to verify stack works
* fixed the wrong version specifier
* Adjust recommendation type to latest
* all the use cases
* Release of version 0.3.0
* Release of version 0.2.0
* Fix Coala issues
* Automatic update of dependency texttable from 1.6.0 to 1.6.1
* a basic lockdown example
* Remove redundant parentheses
* Introduce output formats for Thamos
* Automatic update of dependency thoth-analyzer from 0.1.0 to 0.1.2
* Add missing MANIFEST.in
* Perform autodiscovery for host runtime environment
* Use black for formatting
* Explicitly propagate recommendation type if user asked so
* Fix clash of options for CLI
* Submit runtime environments to Thoth
* Re-generate swagger client files
* Make configuration entries minimal
* Automatic update of dependency distro from 1.3.0 to 1.4.0
* Automatic update of dependency python-dateutil from 2.7.5 to 2.8.0
* Adjust configuration file structure based on comments
* Rename configuration to runtime_environments
* Make a list of configurations
* State requirements format in the config file
* Adjust structure of configuration file
* Introduce log and status sub-commands
* Introduce a way how to suppress TLS warnings
* It's already 2019
* Update README with lib/CLI instructions
* Adjust TLS verify property when thamos is used as a lib
* Provide routine for submitting and retrieving image analyses
* Automatic update of dependency yaspin from 0.14.0 to 0.14.1
* Automatic update of dependency texttable from 1.5.0 to 1.6.0
* Add missing requirements
* Fix exception happening if there was an error in analysis
* Release of version 0.1.0
* Use contoml instead of toml, it has prettier output
* Warn on using insecure network without TLS
* Provide some defaults for runtime environmnet configuration
* Remove no longer relevant TODO
* Perform API discovery when communicating with remote
* Remove unused parameters to CLI commands
* Propagate error in report to process exit code
* Give user guidance on how to configure thamos
* Regenerate thamos swagger client
* Add guards to library functions
* CLI always uses the highest rated software stack
* Serialize into a file correctly
* Remove invalid parameter to TOML
* Automatic update of dependency six from 1.11.0 to 1.12.0
* Automatic update of dependency certifi from 2018.10.15 to 2018.11.29
* Wrong index was on server side
* Fix report indexing
* Fix missing parameter
* Propagate force parameters to bypass server-side cache
* Point to upshift test environment by default
* Add long description for PyPI
* Update to correctly propagate runtime environment
* Update swagger client with hardware info on input
* Make CI happy again
* Adjust library's advise implementation for current implementation
* Update to reflect the current API implementation
* Automatic update of dependency texttable from 1.4.0 to 1.5.0
* Automatic update of dependency urllib3 from 1.24 to 1.24.1
* Do not use trailing slash in url
* Automatic update of dependency python-dateutil from 2.7.4 to 2.7.5
* use thoth-* jobs in pipeline
* added .vscode/
* Automatic update of dependency python-dateutil from 2.7.3 to 2.7.4
* Automatic update of dependency urllib3 from 1.23 to 1.24
* Automatic update of dependency thoth-analyzer from 0.0.7 to 0.1.0
* We use JSON as an output format
* Regenerate client to include dependency monkey API
* Logs can be nullable
* Introduce --no-wait flag for not waiting for analysis to finish
* Automatic update of dependency click from 6.7 to 7.0
* State properties are now model properties
* Regenerate swagger client
* Delete strict checks in nullable values
* Use yaml.safe_load due to security reasons
* Supress details from reports in table output
* Print nested dicts nicely in the provenance report
* Omit redundant findings key in the provenance report
* Omit redundant findings key in the provenance report
* Make runtime environment a parameter to CLI
* Center package name and package version in response
* Initial dependency lock
* Return code 4 is no more missing
* Fix linter complains
* Final bits in initial working implementation
* Initial implementation of CLI
* Regenerate swagger client based on the current state
* Regenerate swagger client with new response models
* removed the markdown bear as it depends on some npm tools
* more linter fixes
* missing newline
* preparing for coala
* added a job for creating releases
* added the missing coala config
* added github and zuul configs
* Initial implementation

## Release 0.7.6 (2019-12-04T15:17:26)
* :pencil: there was some ( too much

## Release 0.7.7 (2019-12-13T12:36:52)
* Inform about no justification made
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.6 to 0.1.7
* Add missing bits for documentation
* Generate Thamos documentation
* Regenerate client to support is_s2i flag
* Propagate is_s2i flag based to User API
* minor updates
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.5 to 0.1.6

## Release 0.8.0 (2020-01-29T10:30:44)
* Regenerate client with updated GitHub parameter types
* Fix method name
* Add support for GitHub integration to Thamos lib
* Regenerate client for GitHub support
* :pushpin: Automatic update of dependency urllib3 from 1.25.7 to 1.25.8
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.7 to 0.1.8
* :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* :pushpin: Automatic update of dependency six from 1.13.0 to 1.14.0
* :pushpin: Automatic update of dependency yaspin from 0.15.0 to 0.16.0
* :pushpin: Automatic update of dependency thoth-python from 0.9.0 to 0.9.1
* Adjust testsuite to new response format
* Add pip/pip-compile support
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* Update examples
* Happy new year!
* :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2

## Release 0.8.1 (2020-02-05T15:45:24)
* Regenerate client and docs after modifying GitHubApp parameters
* remove unusued parameter
* Modify parameters for GitHub App
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5

## Release 0.8.2 (2020-03-26T01:03:53)
* Add templates for Kebechet releases
* Fix analusis error detection
* A temporary workaround for workload-operator and analysis propagation
* :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
* Initial dependency lock
* Delete Pipfile.lock
* :pushpin: Automatic update of dependency daiquiri from 2.0.0 to 2.1.0
* Try to detect git origin with request
* :pushpin: Automatic update of dependency requests from 2.22.0 to 2.23.0
* Improve error handling when user-api is not available
* Update .thoth.yaml

## Release 0.9.0 (2020-03-30T09:26:37)
* Introduce thamos advise with --dev switch
* Colorize logs comming from the cluster
* Parse JSON log produced in the cluster on `thamos log`
* Version 0.8.3
* Pin pyyaml and setuptools for pip's resolver
* Fix requirements parsing in setup.py
* Release of version 0.8.2
* :pushpin: Automatic update of dependency pyyaml from 5.3.1 to 3.13
* Add templates for Kebechet releases
* Fix analusis error detection
* A temporary workaround for workload-operator and analysis propagation
* :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
* Initial dependency lock
* Delete Pipfile.lock
* :pushpin: Automatic update of dependency daiquiri from 2.0.0 to 2.1.0
* Try to detect git origin with request
* :pushpin: Automatic update of dependency requests from 2.22.0 to 2.23.0
* Improve error handling when user-api is not available
* Update .thoth.yaml
* Release of version 0.8.1
* Regenerate client and docs after modifying GitHubApp parameters
* remove unusued parameter
* Modify parameters for GitHub App
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
* Release of version 0.8.0
* Regenerate client with updated GitHub parameter types
* Fix method name
* Add support for GitHub integration to Thamos lib
* Regenerate client for GitHub support
* :pushpin: Automatic update of dependency urllib3 from 1.25.7 to 1.25.8
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.7 to 0.1.8
* :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* :pushpin: Automatic update of dependency six from 1.13.0 to 1.14.0
* :pushpin: Automatic update of dependency yaspin from 0.15.0 to 0.16.0
* :pushpin: Automatic update of dependency thoth-python from 0.9.0 to 0.9.1
* Adjust testsuite to new response format
* Add pip/pip-compile support
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* Update examples
* Happy new year!
* :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
* Release of version 0.7.7
* Inform about no justification made
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.6 to 0.1.7
* Add missing bits for documentation
* Generate Thamos documentation
* Regenerate client to support is_s2i flag
* Propagate is_s2i flag based to User API
* minor updates
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.5 to 0.1.6
* Release of version 0.7.6
* Release of version 0.7.5
* :pencil: there was some ( too much
* :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.4 to 0.1.5
* :pushpin: Automatic update of dependency certifi from 2019.9.11 to 2019.11.28
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* Release of version 0.7.4
* Advised runtime environment is now part of recommended product
* Release of version 0.7.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.6 to 1.25.7
* Adjust output visualization according to new adviser output
* save check for the stack-info
* update thamos with latest user-api
* use https protocol to access test user-api
* :pushpin: Automatic update of dependency six from 1.12.0 to 1.13.0
* :pushpin: Automatic update of dependency python-dateutil from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* Update .codeclimate.yml
* Create .codeclimate.yml
* Create .gitattributes
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Print out Thoth backend version on `thamos version'
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.3 to 0.1.4
* :pushpin: Automatic update of dependency urllib3 from 1.25.5 to 1.25.6
* Do not send empty library usage
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.2 to 0.1.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.4 to 1.25.5
* :pushpin: Automatic update of dependency urllib3 from 1.25.3 to 1.25.4
* :pushpin: Automatic update of dependency certifi from 2019.6.16 to 2019.9.11
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* Link to docs for specific node placement
* Release of version 0.7.2
* Add missing toml in requirements.txt
* Release of version 0.7.1
* Add missing test file
* Enable zuul-pytest on this repo
* :sparkles: now using Fedora 30 and Python 3.7
* Use .coafile from adviser
* Add tests for checking serialization
* Switch from contoml to toml
* Adjust the exception message when file is not set
* State Pipfile is required
* We require Python 3.6+
* Always create config from template if template is set explictly
* Release of version 0.7.0
* :pushpin: Automatic update of dependency yaspin from 0.14.3 to 0.15.0
* :pushpin: Automatic update of dependency invectio from 0.0.6 to 0.0.7
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* :pushpin: Automatic update of dependency invectio from 0.0.5 to 0.0.6
* Document environment variables which can be used during s2i
* :pushpin: Automatic dependency re-locking
* Adjust status command to use the last analysis id
* Filter out calls to Python's standard library
* The configuration template can be user supplied
* Provide a way to note last analysis id into a temporary file
* Decrease maximum sleep time to be more responsive
* Propagate environment configuration in advise_here
* Expand configuration with environment variables
* Hot fix for accessing wrong variable
* Propagate library usage for all Python libraries
* Add ability to configure thamos using envvars
* Correctly propagate invectio version to user-api after library usage detection
* Be more descriptive with logged message about library usage
* :pushpin: Automatic update of dependency invectio from 0.0.4 to 0.0.5
* Fix issue if no report is generated by the recommendation engine
* Release of version 0.6.0
* :boat: updated thamos with latest user-api
* :snail: supporting method for submitting whole build(imagestream and buildlog)
* :pushpin: Automatic update of dependency invectio from 0.0.3 to 0.0.4
* Release of version 0.5.5
* Fix issues with generated swagger client
* Remove trailing whitespace
* Fix propagation of `limit_latest_versions` parameter
* Round up maximum line length allowed for Coala
* Be more verbose about adviser input on debug
* Use test environment as a source for swagger client
* Regenerate swagger client
* Removed unecessary from get_analysis_results
* Duplicate origin param
* Added origin to advise
* Fixed
* Release of version 0.5.4
* Add `nowrite` parameter to create_default_config
* auto swagger client generated
* Analysis ID is second argument
* Analysis ID is second argument
* Remove trailing whitespace
* Added origin option to provenance and advise
* Make sure to follow recomendation type priority
* Fix issue #182
* :pushpin: Automatic update of dependency texttable from 1.6.1 to 1.6.2
* Update docs on how autogenerating code is done
* lib analysis results
* Fix URL to OpenAPI YAML
* Release of version 0.5.3
* Release of version 0.5.2
* Release of version 0.5.1
* Release of version 0.5.0
* Fix handling based on arguments if no config file is needed
* :pushpin: Automatic update of dependency certifi from 2019.3.9 to 2019.6.16
* Release of version 0.4.3
* :pushpin: Automatic update of dependency invectio from 0.0.1 to 0.0.3
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* :pushpin: Automatic update of dependency yaspin from 0.14.2 to 0.14.3
* :pushpin: Automatic update of dependency urllib3 from 1.24.3 to 1.25.3
* Include Thoth's configuration file for sdist distribution
* rm trailing white space
* Removed self keyword
* Remove api arg
* Accidental white space
* Forgot to remove arguments
* Forgot to remove arguments
* Manual formatting
* Auto format
* Provenance here lib function
* Use own user-agent for user requests
* Thamos Library advise_here (#159)
* Edit styling
* Edit styling
* python/black styling
* Pipfile.lock is not auto added
* No need to include API client in args
* Created library function for advising current directory
* State configuration option for disabling progressbar
* Adjust default Thoth host to talk to
* Provide ability to supply configuration file template
* Report warning if no library usage was gathered
* Release of version 0.4.2
* Add missing Invectio requirement
* Release of version 0.4.1
* Use arguments instead of kwargs to be compatible with openapi
* Release of version 0.4.0
* Regenerate for new implementation
* Use openapi 3 implementation for swagger client generation
* Re-generate swagger client
* Integrate static analysis using Invectio
* :pushpin: Automatic update of dependency urllib3 from 1.24.2 to 1.24.3
* :pushpin: Automatic update of dependency yaspin from 0.14.1 to 0.14.2
* Re-generate for transition to Dgraph
* :pushpin: Automatic update of dependency urllib3 from 1.24.1 to 1.24.2
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* :sparkles: using -stage now, removed some quirks
* :sparkles: added a container build script and adjusted some readmes
* Log Thoth's API URL to show to which instance a user talks to
* bug fix on TLS turned on
* Used urljoin for maintaining semantic version of url
* Correctly handle errors from reports and empty reports
* Make sure configuration changes are propagated to config file
* Match operating system with solver results
* Pin down more dependencies
* Enable limit_latest_versions to be configured from configuration
* Update .thoth.yaml
* Fix Coala complains
* Adjust runtime-environment example to reflect data in Test environment
* Release of version 0.3.1
* Add Thoth's configuration file
* Provide environment type in library adapter
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Regenerate client
* Target coala issues
* Do not write changes in configuration if there are no changes
* Adjust Thoth's configuration based on recommendations
* Regenerate swagger-client, add limit latest versions option
* Fix formatting
* Use safe_dump() instead of dump()
* Automatic dependency re-locking
* Add ability to expand entries in configuration file
* Add ability to create configuration in non-interactive mode
* Demo with lower flask version
* Move resolved stacks to misc repo
* Fix issues reported by coala
* Add files supporting "scoring" scenario
* Fix coala complains
* Add files supporting "scoring" scenario
* Add README for runtime environment scenario
* Remove requires section in example
* Minor improvements in README file
* Minor improvements in README file
* Add README file for lockdown example
* Add example flask application to verify stack works
* fixed the wrong version specifier
* Adjust recommendation type to latest
* all the use cases
* Release of version 0.3.0
* Release of version 0.2.0
* Fix Coala issues
* Automatic update of dependency texttable from 1.6.0 to 1.6.1
* a basic lockdown example
* Remove redundant parentheses
* Introduce output formats for Thamos
* Automatic update of dependency thoth-analyzer from 0.1.0 to 0.1.2
* Add missing MANIFEST.in
* Perform autodiscovery for host runtime environment
* Use black for formatting
* Explicitly propagate recommendation type if user asked so
* Fix clash of options for CLI
* Submit runtime environments to Thoth
* Re-generate swagger client files
* Make configuration entries minimal
* Automatic update of dependency distro from 1.3.0 to 1.4.0
* Automatic update of dependency python-dateutil from 2.7.5 to 2.8.0
* Adjust configuration file structure based on comments
* Rename configuration to runtime_environments
* Make a list of configurations
* State requirements format in the config file
* Adjust structure of configuration file
* Introduce log and status sub-commands
* Introduce a way how to suppress TLS warnings
* It's already 2019
* Update README with lib/CLI instructions
* Adjust TLS verify property when thamos is used as a lib
* Provide routine for submitting and retrieving image analyses
* Automatic update of dependency yaspin from 0.14.0 to 0.14.1
* Automatic update of dependency texttable from 1.5.0 to 1.6.0
* Add missing requirements
* Fix exception happening if there was an error in analysis
* Release of version 0.1.0
* Use contoml instead of toml, it has prettier output
* Warn on using insecure network without TLS
* Provide some defaults for runtime environmnet configuration
* Remove no longer relevant TODO
* Perform API discovery when communicating with remote
* Remove unused parameters to CLI commands
* Propagate error in report to process exit code
* Give user guidance on how to configure thamos
* Regenerate thamos swagger client
* Add guards to library functions
* CLI always uses the highest rated software stack
* Serialize into a file correctly
* Remove invalid parameter to TOML
* Automatic update of dependency six from 1.11.0 to 1.12.0
* Automatic update of dependency certifi from 2018.10.15 to 2018.11.29
* Wrong index was on server side
* Fix report indexing
* Fix missing parameter
* Propagate force parameters to bypass server-side cache
* Point to upshift test environment by default
* Add long description for PyPI
* Update to correctly propagate runtime environment
* Update swagger client with hardware info on input
* Make CI happy again
* Adjust library's advise implementation for current implementation
* Update to reflect the current API implementation
* Automatic update of dependency texttable from 1.4.0 to 1.5.0
* Automatic update of dependency urllib3 from 1.24 to 1.24.1
* Do not use trailing slash in url
* Automatic update of dependency python-dateutil from 2.7.4 to 2.7.5
* use thoth-* jobs in pipeline
* added .vscode/
* Automatic update of dependency python-dateutil from 2.7.3 to 2.7.4
* Automatic update of dependency urllib3 from 1.23 to 1.24
* Automatic update of dependency thoth-analyzer from 0.0.7 to 0.1.0
* We use JSON as an output format
* Regenerate client to include dependency monkey API
* Logs can be nullable
* Introduce --no-wait flag for not waiting for analysis to finish
* Automatic update of dependency click from 6.7 to 7.0
* State properties are now model properties
* Regenerate swagger client
* Delete strict checks in nullable values
* Use yaml.safe_load due to security reasons
* Supress details from reports in table output
* Print nested dicts nicely in the provenance report
* Omit redundant findings key in the provenance report
* Omit redundant findings key in the provenance report
* Make runtime environment a parameter to CLI
* Center package name and package version in response
* Initial dependency lock
* Return code 4 is no more missing
* Fix linter complains
* Final bits in initial working implementation
* Initial implementation of CLI
* Regenerate swagger client based on the current state
* Regenerate swagger client with new response models
* removed the markdown bear as it depends on some npm tools
* more linter fixes
* missing newline
* preparing for coala
* added a job for creating releases
* added the missing coala config
* added github and zuul configs
* Initial implementation

## Release 0.9.1 (2020-03-30T20:42:00)
* Update client to also include dev flag
* Remove unused imports

## Release 0.9.2 (2020-04-01T20:53:24)
* Do not fail if obtaining origin fails
* :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
* :pushpin: Automatic update of dependency distro from 1.4.0 to 1.5.0
* Release of version 0.9.1
* Update client to also include dev flag
* Release of version 0.9.0
* Introduce thamos advise with --dev switch
* Colorize logs comming from the cluster
* Parse JSON log produced in the cluster on `thamos log`
* Remove unused imports
* Version 0.8.3
* Pin pyyaml and setuptools for pip's resolver
* Fix requirements parsing in setup.py
* Release of version 0.8.2
* :pushpin: Automatic update of dependency pyyaml from 5.3.1 to 3.13
* Add templates for Kebechet releases
* Fix analusis error detection
* A temporary workaround for workload-operator and analysis propagation
* :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
* Initial dependency lock
* Delete Pipfile.lock
* :pushpin: Automatic update of dependency daiquiri from 2.0.0 to 2.1.0
* Try to detect git origin with request
* :pushpin: Automatic update of dependency requests from 2.22.0 to 2.23.0
* Improve error handling when user-api is not available
* Update .thoth.yaml
* Release of version 0.8.1
* Regenerate client and docs after modifying GitHubApp parameters
* remove unusued parameter
* Modify parameters for GitHub App
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
* Release of version 0.8.0
* Regenerate client with updated GitHub parameter types
* Fix method name
* Add support for GitHub integration to Thamos lib
* Regenerate client for GitHub support
* :pushpin: Automatic update of dependency urllib3 from 1.25.7 to 1.25.8
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.7 to 0.1.8
* :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* :pushpin: Automatic update of dependency six from 1.13.0 to 1.14.0
* :pushpin: Automatic update of dependency yaspin from 0.15.0 to 0.16.0
* :pushpin: Automatic update of dependency thoth-python from 0.9.0 to 0.9.1
* Adjust testsuite to new response format
* Add pip/pip-compile support
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* Update examples
* Happy new year!
* :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
* Release of version 0.7.7
* Inform about no justification made
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.6 to 0.1.7
* Add missing bits for documentation
* Generate Thamos documentation
* Regenerate client to support is_s2i flag
* Propagate is_s2i flag based to User API
* minor updates
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.5 to 0.1.6
* Release of version 0.7.6
* Release of version 0.7.5
* :pencil: there was some ( too much
* :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.4 to 0.1.5
* :pushpin: Automatic update of dependency certifi from 2019.9.11 to 2019.11.28
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* Release of version 0.7.4
* Advised runtime environment is now part of recommended product
* Release of version 0.7.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.6 to 1.25.7
* Adjust output visualization according to new adviser output
* save check for the stack-info
* update thamos with latest user-api
* use https protocol to access test user-api
* :pushpin: Automatic update of dependency six from 1.12.0 to 1.13.0
* :pushpin: Automatic update of dependency python-dateutil from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* Update .codeclimate.yml
* Create .codeclimate.yml
* Create .gitattributes
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Print out Thoth backend version on `thamos version'
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.3 to 0.1.4
* :pushpin: Automatic update of dependency urllib3 from 1.25.5 to 1.25.6
* Do not send empty library usage
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.2 to 0.1.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.4 to 1.25.5
* :pushpin: Automatic update of dependency urllib3 from 1.25.3 to 1.25.4
* :pushpin: Automatic update of dependency certifi from 2019.6.16 to 2019.9.11
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* Link to docs for specific node placement
* Release of version 0.7.2
* Add missing toml in requirements.txt
* Release of version 0.7.1
* Add missing test file
* Enable zuul-pytest on this repo
* :sparkles: now using Fedora 30 and Python 3.7
* Use .coafile from adviser
* Add tests for checking serialization
* Switch from contoml to toml
* Adjust the exception message when file is not set
* State Pipfile is required
* We require Python 3.6+
* Always create config from template if template is set explictly
* Release of version 0.7.0
* :pushpin: Automatic update of dependency yaspin from 0.14.3 to 0.15.0
* :pushpin: Automatic update of dependency invectio from 0.0.6 to 0.0.7
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* :pushpin: Automatic update of dependency invectio from 0.0.5 to 0.0.6
* Document environment variables which can be used during s2i
* :pushpin: Automatic dependency re-locking
* Adjust status command to use the last analysis id
* Filter out calls to Python's standard library
* The configuration template can be user supplied
* Provide a way to note last analysis id into a temporary file
* Decrease maximum sleep time to be more responsive
* Propagate environment configuration in advise_here
* Expand configuration with environment variables
* Hot fix for accessing wrong variable
* Propagate library usage for all Python libraries
* Add ability to configure thamos using envvars
* Correctly propagate invectio version to user-api after library usage detection
* Be more descriptive with logged message about library usage
* :pushpin: Automatic update of dependency invectio from 0.0.4 to 0.0.5
* Fix issue if no report is generated by the recommendation engine
* Release of version 0.6.0
* :boat: updated thamos with latest user-api
* :snail: supporting method for submitting whole build(imagestream and buildlog)
* :pushpin: Automatic update of dependency invectio from 0.0.3 to 0.0.4
* Release of version 0.5.5
* Fix issues with generated swagger client
* Remove trailing whitespace
* Fix propagation of `limit_latest_versions` parameter
* Round up maximum line length allowed for Coala
* Be more verbose about adviser input on debug
* Use test environment as a source for swagger client
* Regenerate swagger client
* Removed unecessary from get_analysis_results
* Duplicate origin param
* Added origin to advise
* Fixed
* Release of version 0.5.4
* Add `nowrite` parameter to create_default_config
* auto swagger client generated
* Analysis ID is second argument
* Analysis ID is second argument
* Remove trailing whitespace
* Added origin option to provenance and advise
* Make sure to follow recomendation type priority
* Fix issue #182
* :pushpin: Automatic update of dependency texttable from 1.6.1 to 1.6.2
* Update docs on how autogenerating code is done
* lib analysis results
* Fix URL to OpenAPI YAML
* Release of version 0.5.3
* Release of version 0.5.2
* Release of version 0.5.1
* Release of version 0.5.0
* Fix handling based on arguments if no config file is needed
* :pushpin: Automatic update of dependency certifi from 2019.3.9 to 2019.6.16
* Release of version 0.4.3
* :pushpin: Automatic update of dependency invectio from 0.0.1 to 0.0.3
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* :pushpin: Automatic update of dependency yaspin from 0.14.2 to 0.14.3
* :pushpin: Automatic update of dependency urllib3 from 1.24.3 to 1.25.3
* Include Thoth's configuration file for sdist distribution
* rm trailing white space
* Removed self keyword
* Remove api arg
* Accidental white space
* Forgot to remove arguments
* Forgot to remove arguments
* Manual formatting
* Auto format
* Provenance here lib function
* Use own user-agent for user requests
* Thamos Library advise_here (#159)
* Edit styling
* Edit styling
* python/black styling
* Pipfile.lock is not auto added
* No need to include API client in args
* Created library function for advising current directory
* State configuration option for disabling progressbar
* Adjust default Thoth host to talk to
* Provide ability to supply configuration file template
* Report warning if no library usage was gathered
* Release of version 0.4.2
* Add missing Invectio requirement
* Release of version 0.4.1
* Use arguments instead of kwargs to be compatible with openapi
* Release of version 0.4.0
* Regenerate for new implementation
* Use openapi 3 implementation for swagger client generation
* Re-generate swagger client
* Integrate static analysis using Invectio
* :pushpin: Automatic update of dependency urllib3 from 1.24.2 to 1.24.3
* :pushpin: Automatic update of dependency yaspin from 0.14.1 to 0.14.2
* Re-generate for transition to Dgraph
* :pushpin: Automatic update of dependency urllib3 from 1.24.1 to 1.24.2
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* :sparkles: using -stage now, removed some quirks
* :sparkles: added a container build script and adjusted some readmes
* Log Thoth's API URL to show to which instance a user talks to
* bug fix on TLS turned on
* Used urljoin for maintaining semantic version of url
* Correctly handle errors from reports and empty reports
* Make sure configuration changes are propagated to config file
* Match operating system with solver results
* Pin down more dependencies
* Enable limit_latest_versions to be configured from configuration
* Update .thoth.yaml
* Fix Coala complains
* Adjust runtime-environment example to reflect data in Test environment
* Release of version 0.3.1
* Add Thoth's configuration file
* Provide environment type in library adapter
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Regenerate client
* Target coala issues
* Do not write changes in configuration if there are no changes
* Adjust Thoth's configuration based on recommendations
* Regenerate swagger-client, add limit latest versions option
* Fix formatting
* Use safe_dump() instead of dump()
* Automatic dependency re-locking
* Add ability to expand entries in configuration file
* Add ability to create configuration in non-interactive mode
* Demo with lower flask version
* Move resolved stacks to misc repo
* Fix issues reported by coala
* Add files supporting "scoring" scenario
* Fix coala complains
* Add files supporting "scoring" scenario
* Add README for runtime environment scenario
* Remove requires section in example
* Minor improvements in README file
* Minor improvements in README file
* Add README file for lockdown example
* Add example flask application to verify stack works
* fixed the wrong version specifier
* Adjust recommendation type to latest
* all the use cases
* Release of version 0.3.0
* Release of version 0.2.0
* Fix Coala issues
* Automatic update of dependency texttable from 1.6.0 to 1.6.1
* a basic lockdown example
* Remove redundant parentheses
* Introduce output formats for Thamos
* Automatic update of dependency thoth-analyzer from 0.1.0 to 0.1.2
* Add missing MANIFEST.in
* Perform autodiscovery for host runtime environment
* Use black for formatting
* Explicitly propagate recommendation type if user asked so
* Fix clash of options for CLI
* Submit runtime environments to Thoth
* Re-generate swagger client files
* Make configuration entries minimal
* Automatic update of dependency distro from 1.3.0 to 1.4.0
* Automatic update of dependency python-dateutil from 2.7.5 to 2.8.0
* Adjust configuration file structure based on comments
* Rename configuration to runtime_environments
* Make a list of configurations
* State requirements format in the config file
* Adjust structure of configuration file
* Introduce log and status sub-commands
* Introduce a way how to suppress TLS warnings
* It's already 2019
* Update README with lib/CLI instructions
* Adjust TLS verify property when thamos is used as a lib
* Provide routine for submitting and retrieving image analyses
* Automatic update of dependency yaspin from 0.14.0 to 0.14.1
* Automatic update of dependency texttable from 1.5.0 to 1.6.0
* Add missing requirements
* Fix exception happening if there was an error in analysis
* Release of version 0.1.0
* Use contoml instead of toml, it has prettier output
* Warn on using insecure network without TLS
* Provide some defaults for runtime environmnet configuration
* Remove no longer relevant TODO
* Perform API discovery when communicating with remote
* Remove unused parameters to CLI commands
* Propagate error in report to process exit code
* Give user guidance on how to configure thamos
* Regenerate thamos swagger client
* Add guards to library functions
* CLI always uses the highest rated software stack
* Serialize into a file correctly
* Remove invalid parameter to TOML
* Automatic update of dependency six from 1.11.0 to 1.12.0
* Automatic update of dependency certifi from 2018.10.15 to 2018.11.29
* Wrong index was on server side
* Fix report indexing
* Fix missing parameter
* Propagate force parameters to bypass server-side cache
* Point to upshift test environment by default
* Add long description for PyPI
* Update to correctly propagate runtime environment
* Update swagger client with hardware info on input
* Make CI happy again
* Adjust library's advise implementation for current implementation
* Update to reflect the current API implementation
* Automatic update of dependency texttable from 1.4.0 to 1.5.0
* Automatic update of dependency urllib3 from 1.24 to 1.24.1
* Do not use trailing slash in url
* Automatic update of dependency python-dateutil from 2.7.4 to 2.7.5
* use thoth-* jobs in pipeline
* added .vscode/
* Automatic update of dependency python-dateutil from 2.7.3 to 2.7.4
* Automatic update of dependency urllib3 from 1.23 to 1.24
* Automatic update of dependency thoth-analyzer from 0.0.7 to 0.1.0
* We use JSON as an output format
* Regenerate client to include dependency monkey API
* Logs can be nullable
* Introduce --no-wait flag for not waiting for analysis to finish
* Automatic update of dependency click from 6.7 to 7.0
* State properties are now model properties
* Regenerate swagger client
* Delete strict checks in nullable values
* Use yaml.safe_load due to security reasons
* Supress details from reports in table output
* Print nested dicts nicely in the provenance report
* Omit redundant findings key in the provenance report
* Omit redundant findings key in the provenance report
* Make runtime environment a parameter to CLI
* Center package name and package version in response
* Initial dependency lock
* Return code 4 is no more missing
* Fix linter complains
* Final bits in initial working implementation
* Initial implementation of CLI
* Regenerate swagger client based on the current state
* Regenerate swagger client with new response models
* removed the markdown bear as it depends on some npm tools
* more linter fixes
* missing newline
* preparing for coala
* added a job for creating releases
* added the missing coala config
* added github and zuul configs
* Initial implementation

## Release 0.9.3 (2020-04-20T20:30:51)
* :pushpin: Automatic update of dependency thoth-python from 0.9.1 to 0.9.2
* Remove checks on files as they are in Thoth-python 0.9.2
* Add TODO
* Add explanation for ConfigurationError
* Add files
* Add check on advise_here
* Add check on requirements format if missing from config file
* Added missing docstring
* :pushpin: Automatic update of dependency urllib3 from 1.25.8 to 1.25.9
* Do not report exception if no configuration was found in the directory
* Update lockdown scenario
* :pushpin: Automatic update of dependency certifi from 2020.4.5 to 2020.4.5.1
* :pushpin: Automatic update of dependency certifi from 2019.11.28 to 2020.4.5
* Use RHEL 8
* Update runtime environment example
* No CentOS, use RHEL
* Update scoring example
* Add new line after each log line if structured logging is turned off
* Long description content type missing in setup.py
* Drop raw HTTP support

## Release 0.9.4 (2020-04-27T22:43:12)
* Implement retry mechanism to avoid flakes
* Fix spelling
* Provide platform in Thoth's configuration file

## Release 0.10.0 (2020-04-29T21:43:33)
* Configure requirements format using env variables passed to build
* Respect review comments
* Regenerate client to reflect recent API schema changes
* Document environment variables that can be used
* Fix inconsistency in wait time printed
* Remove unused variable

## Release 0.10.1 (2020-05-18T09:06:19)
* :sparkles: added standard project github templates
* better version spec for pyyaml
* manually locked pyyaml :arrow_up:
* lib and CLI should have same behaviour
* :pushpin: Automatic update of dependency toml from 0.10.0 to 0.10.1
* :pushpin: Automatic update of dependency yaspin from 0.16.0 to 0.17.0
* :pushpin: Automatic update of dependency pytest from 5.4.1 to 5.4.2

## Release 0.10.2 (2020-05-25T17:00:45)
* Add missing docstring
* adjust check
* Check for S2I
* Use correct enums
* Introduce source_type flag
* :pushpin: Automatic update of dependency pytest-cov from 2.8.1 to 2.9.0
* :pushpin: Automatic update of dependency six from 1.14.0 to 1.15.0
* Removed unncessary import
* Removed alarm decorator
* Revereted formatting changes
* Revereted formatting changes
* Revereted formatting changes
* wrap moved up
* wrap moved up
* Coala fix
* Added timeout decorater
* Added default timeout to be 15mins
* Added env variable to readme

## Release 0.10.3 (2020-06-09T23:26:20)
* Regenerated swagger to fix thamos error
* Document runtime environments in the config file
* :pushpin: Automatic update of dependency certifi from 2020.4.5.1 to 2020.4.5.2
* :pushpin: Automatic update of dependency pytest from 5.4.2 to 5.4.3
* Increase timeout

## Release 0.10.4 (2020-06-10T21:14:10)
* Add sesheta as maintainer
* Fix handling of enums
* Release of version 0.10.3
* Regenerated swagger to fix thamos error
* Document runtime environments in the config file
* :pushpin: Automatic update of dependency certifi from 2020.4.5.1 to 2020.4.5.2
* :pushpin: Automatic update of dependency pytest from 5.4.2 to 5.4.3
* Increase timeout
* Release of version 0.10.2
* Add missing docstring
* adjust check
* Check for S2I
* Use correct enums
* Introduce source_type flag
* :pushpin: Automatic update of dependency pytest-cov from 2.8.1 to 2.9.0
* :pushpin: Automatic update of dependency six from 1.14.0 to 1.15.0
* Removed unncessary import
* Removed alarm decorator
* Revereted formatting changes
* Revereted formatting changes
* Revereted formatting changes
* wrap moved up
* wrap moved up
* Coala fix
* Added timeout decorater
* Added default timeout to be 15mins
* Added env variable to readme
* Release of version 0.10.1
* :sparkles: added standard project github templates
* better version spec for pyyaml
* manually locked pyyaml :arrow_up:
* lib and CLI should have same behaviour
* :pushpin: Automatic update of dependency toml from 0.10.0 to 0.10.1
* :pushpin: Automatic update of dependency yaspin from 0.16.0 to 0.17.0
* :pushpin: Automatic update of dependency pytest from 5.4.1 to 5.4.2
* Release of version 0.10.0
* Configure requirements format using env variables passed to build
* Respect review comments
* Regenerate client to reflect recent API schema changes
* Document environment variables that can be used
* Fix inconsistency in wait time printed
* Release of version 0.9.4
* Remove unused variable
* :pushpin: Automatic update of dependency click from 7.1.1 to 7.1.2
* Implement retry mechanism to avoid flakes
* Fix spelling
* Provide platform in Thoth's configuration file
* Release of version 0.9.3
* :pushpin: Automatic update of dependency thoth-python from 0.9.1 to 0.9.2
* Remove checks on files as they are in Thoth-python 0.9.2
* Add TODO
* Add explanation for ConfigurationError
* Add files
* Add check on advise_here
* Add check on requirements format if missing from config file
* Added missing docstring
* :pushpin: Automatic update of dependency urllib3 from 1.25.8 to 1.25.9
* Do not report exception if no configuration was found in the directory
* Update lockdown scenario
* :pushpin: Automatic update of dependency certifi from 2020.4.5 to 2020.4.5.1
* :pushpin: Automatic update of dependency certifi from 2019.11.28 to 2020.4.5
* Use RHEL 8
* Update runtime environment example
* No CentOS, use RHEL
* Update scoring example
* Add new line after each log line if structured logging is turned off
* Long description content type missing in setup.py
* Release of version 0.9.2
* Do not fail if obtaining origin fails
* :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
* :pushpin: Automatic update of dependency distro from 1.4.0 to 1.5.0
* Release of version 0.9.1
* Update client to also include dev flag
* Release of version 0.9.0
* Introduce thamos advise with --dev switch
* Colorize logs comming from the cluster
* Parse JSON log produced in the cluster on `thamos log`
* Remove unused imports
* Version 0.8.3
* Pin pyyaml and setuptools for pip's resolver
* Fix requirements parsing in setup.py
* Release of version 0.8.2
* :pushpin: Automatic update of dependency pyyaml from 5.3.1 to 3.13
* Add templates for Kebechet releases
* Fix analusis error detection
* A temporary workaround for workload-operator and analysis propagation
* :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
* Initial dependency lock
* Delete Pipfile.lock
* :pushpin: Automatic update of dependency daiquiri from 2.0.0 to 2.1.0
* Try to detect git origin with request
* Drop raw HTTP support
* :pushpin: Automatic update of dependency requests from 2.22.0 to 2.23.0
* Improve error handling when user-api is not available
* Update .thoth.yaml
* Release of version 0.8.1
* Regenerate client and docs after modifying GitHubApp parameters
* remove unusued parameter
* Modify parameters for GitHub App
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
* Release of version 0.8.0
* Regenerate client with updated GitHub parameter types
* Fix method name
* Add support for GitHub integration to Thamos lib
* Regenerate client for GitHub support
* :pushpin: Automatic update of dependency urllib3 from 1.25.7 to 1.25.8
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.7 to 0.1.8
* :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* :pushpin: Automatic update of dependency six from 1.13.0 to 1.14.0
* :pushpin: Automatic update of dependency yaspin from 0.15.0 to 0.16.0
* :pushpin: Automatic update of dependency thoth-python from 0.9.0 to 0.9.1
* Adjust testsuite to new response format
* Add pip/pip-compile support
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* Update examples
* Happy new year!
* :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
* Release of version 0.7.7
* Inform about no justification made
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.6 to 0.1.7
* Add missing bits for documentation
* Generate Thamos documentation
* Regenerate client to support is_s2i flag
* Propagate is_s2i flag based to User API
* minor updates
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.5 to 0.1.6
* Release of version 0.7.6
* Release of version 0.7.5
* :pencil: there was some ( too much
* :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.4 to 0.1.5
* :pushpin: Automatic update of dependency certifi from 2019.9.11 to 2019.11.28
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* Release of version 0.7.4
* Advised runtime environment is now part of recommended product
* Release of version 0.7.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.6 to 1.25.7
* Adjust output visualization according to new adviser output
* save check for the stack-info
* update thamos with latest user-api
* use https protocol to access test user-api
* :pushpin: Automatic update of dependency six from 1.12.0 to 1.13.0
* :pushpin: Automatic update of dependency python-dateutil from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* Update .codeclimate.yml
* Create .codeclimate.yml
* Create .gitattributes
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Print out Thoth backend version on `thamos version'
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.3 to 0.1.4
* :pushpin: Automatic update of dependency urllib3 from 1.25.5 to 1.25.6
* Do not send empty library usage
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.2 to 0.1.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.4 to 1.25.5
* :pushpin: Automatic update of dependency urllib3 from 1.25.3 to 1.25.4
* :pushpin: Automatic update of dependency certifi from 2019.6.16 to 2019.9.11
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* Link to docs for specific node placement
* Release of version 0.7.2
* Add missing toml in requirements.txt
* Release of version 0.7.1
* Add missing test file
* Enable zuul-pytest on this repo
* :sparkles: now using Fedora 30 and Python 3.7
* Use .coafile from adviser
* Add tests for checking serialization
* Switch from contoml to toml
* Adjust the exception message when file is not set
* State Pipfile is required
* We require Python 3.6+
* Always create config from template if template is set explictly
* Release of version 0.7.0
* :pushpin: Automatic update of dependency yaspin from 0.14.3 to 0.15.0
* :pushpin: Automatic update of dependency invectio from 0.0.6 to 0.0.7
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* :pushpin: Automatic update of dependency invectio from 0.0.5 to 0.0.6
* Document environment variables which can be used during s2i
* :pushpin: Automatic dependency re-locking
* Adjust status command to use the last analysis id
* Filter out calls to Python's standard library
* The configuration template can be user supplied
* Provide a way to note last analysis id into a temporary file
* Decrease maximum sleep time to be more responsive
* Propagate environment configuration in advise_here
* Expand configuration with environment variables
* Hot fix for accessing wrong variable
* Propagate library usage for all Python libraries
* Add ability to configure thamos using envvars
* Correctly propagate invectio version to user-api after library usage detection
* Be more descriptive with logged message about library usage
* :pushpin: Automatic update of dependency invectio from 0.0.4 to 0.0.5
* Fix issue if no report is generated by the recommendation engine
* Release of version 0.6.0
* :boat: updated thamos with latest user-api
* :snail: supporting method for submitting whole build(imagestream and buildlog)
* :pushpin: Automatic update of dependency invectio from 0.0.3 to 0.0.4
* Release of version 0.5.5
* Fix issues with generated swagger client
* Remove trailing whitespace
* Fix propagation of `limit_latest_versions` parameter
* Round up maximum line length allowed for Coala
* Be more verbose about adviser input on debug
* Use test environment as a source for swagger client
* Regenerate swagger client
* Removed unecessary from get_analysis_results
* Duplicate origin param
* Added origin to advise
* Fixed
* Release of version 0.5.4
* Add `nowrite` parameter to create_default_config
* auto swagger client generated
* Analysis ID is second argument
* Analysis ID is second argument
* Remove trailing whitespace
* Added origin option to provenance and advise
* Make sure to follow recomendation type priority
* Fix issue #182
* :pushpin: Automatic update of dependency texttable from 1.6.1 to 1.6.2
* Update docs on how autogenerating code is done
* lib analysis results
* Fix URL to OpenAPI YAML
* Release of version 0.5.3
* Release of version 0.5.2
* Release of version 0.5.1
* Release of version 0.5.0
* Fix handling based on arguments if no config file is needed
* :pushpin: Automatic update of dependency certifi from 2019.3.9 to 2019.6.16
* Release of version 0.4.3
* :pushpin: Automatic update of dependency invectio from 0.0.1 to 0.0.3
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* :pushpin: Automatic update of dependency yaspin from 0.14.2 to 0.14.3
* :pushpin: Automatic update of dependency urllib3 from 1.24.3 to 1.25.3
* Include Thoth's configuration file for sdist distribution
* rm trailing white space
* Removed self keyword
* Remove api arg
* Accidental white space
* Forgot to remove arguments
* Forgot to remove arguments
* Manual formatting
* Auto format
* Provenance here lib function
* Use own user-agent for user requests
* Thamos Library advise_here (#159)
* Edit styling
* Edit styling
* python/black styling
* Pipfile.lock is not auto added
* No need to include API client in args
* Created library function for advising current directory
* State configuration option for disabling progressbar
* Adjust default Thoth host to talk to
* Provide ability to supply configuration file template
* Report warning if no library usage was gathered
* Release of version 0.4.2
* Add missing Invectio requirement
* Release of version 0.4.1
* Use arguments instead of kwargs to be compatible with openapi
* Release of version 0.4.0
* Regenerate for new implementation
* Use openapi 3 implementation for swagger client generation
* Re-generate swagger client
* Integrate static analysis using Invectio
* :pushpin: Automatic update of dependency urllib3 from 1.24.2 to 1.24.3
* :pushpin: Automatic update of dependency yaspin from 0.14.1 to 0.14.2
* Re-generate for transition to Dgraph
* :pushpin: Automatic update of dependency urllib3 from 1.24.1 to 1.24.2
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* :sparkles: using -stage now, removed some quirks
* :sparkles: added a container build script and adjusted some readmes
* Log Thoth's API URL to show to which instance a user talks to
* bug fix on TLS turned on
* Used urljoin for maintaining semantic version of url
* Correctly handle errors from reports and empty reports
* Make sure configuration changes are propagated to config file
* Match operating system with solver results
* Pin down more dependencies
* Enable limit_latest_versions to be configured from configuration
* Update .thoth.yaml
* Fix Coala complains
* Adjust runtime-environment example to reflect data in Test environment
* Release of version 0.3.1
* Add Thoth's configuration file
* Provide environment type in library adapter
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Regenerate client
* Target coala issues
* Do not write changes in configuration if there are no changes
* Adjust Thoth's configuration based on recommendations
* Regenerate swagger-client, add limit latest versions option
* Fix formatting
* Use safe_dump() instead of dump()
* Automatic dependency re-locking
* Add ability to expand entries in configuration file
* Add ability to create configuration in non-interactive mode
* Demo with lower flask version
* Move resolved stacks to misc repo
* Fix issues reported by coala
* Add files supporting "scoring" scenario
* Fix coala complains
* Add files supporting "scoring" scenario
* Add README for runtime environment scenario
* Remove requires section in example
* Minor improvements in README file
* Minor improvements in README file
* Add README file for lockdown example
* Add example flask application to verify stack works
* fixed the wrong version specifier
* Adjust recommendation type to latest
* all the use cases
* Release of version 0.3.0
* Release of version 0.2.0
* Fix Coala issues
* Automatic update of dependency texttable from 1.6.0 to 1.6.1
* a basic lockdown example
* Remove redundant parentheses
* Introduce output formats for Thamos
* Automatic update of dependency thoth-analyzer from 0.1.0 to 0.1.2
* Add missing MANIFEST.in
* Perform autodiscovery for host runtime environment
* Use black for formatting
* Explicitly propagate recommendation type if user asked so
* Fix clash of options for CLI
* Submit runtime environments to Thoth
* Re-generate swagger client files
* Make configuration entries minimal
* Automatic update of dependency distro from 1.3.0 to 1.4.0
* Automatic update of dependency python-dateutil from 2.7.5 to 2.8.0
* Adjust configuration file structure based on comments
* Rename configuration to runtime_environments
* Make a list of configurations
* State requirements format in the config file
* Adjust structure of configuration file
* Introduce log and status sub-commands
* Introduce a way how to suppress TLS warnings
* It's already 2019
* Update README with lib/CLI instructions
* Adjust TLS verify property when thamos is used as a lib
* Provide routine for submitting and retrieving image analyses
* Automatic update of dependency yaspin from 0.14.0 to 0.14.1
* Automatic update of dependency texttable from 1.5.0 to 1.6.0
* Add missing requirements
* Fix exception happening if there was an error in analysis
* Release of version 0.1.0
* Use contoml instead of toml, it has prettier output
* Warn on using insecure network without TLS
* Provide some defaults for runtime environmnet configuration
* Remove no longer relevant TODO
* Perform API discovery when communicating with remote
* Remove unused parameters to CLI commands
* Propagate error in report to process exit code
* Give user guidance on how to configure thamos
* Regenerate thamos swagger client
* Add guards to library functions
* CLI always uses the highest rated software stack
* Serialize into a file correctly
* Remove invalid parameter to TOML
* Automatic update of dependency six from 1.11.0 to 1.12.0
* Automatic update of dependency certifi from 2018.10.15 to 2018.11.29
* Wrong index was on server side
* Fix report indexing
* Fix missing parameter
* Propagate force parameters to bypass server-side cache
* Point to upshift test environment by default
* Add long description for PyPI
* Update to correctly propagate runtime environment
* Update swagger client with hardware info on input
* Make CI happy again
* Adjust library's advise implementation for current implementation
* Update to reflect the current API implementation
* Automatic update of dependency texttable from 1.4.0 to 1.5.0
* Automatic update of dependency urllib3 from 1.24 to 1.24.1
* Do not use trailing slash in url
* Automatic update of dependency python-dateutil from 2.7.4 to 2.7.5
* use thoth-* jobs in pipeline
* added .vscode/
* Automatic update of dependency python-dateutil from 2.7.3 to 2.7.4
* Automatic update of dependency urllib3 from 1.23 to 1.24
* Automatic update of dependency thoth-analyzer from 0.0.7 to 0.1.0
* We use JSON as an output format
* Regenerate client to include dependency monkey API
* Logs can be nullable
* Introduce --no-wait flag for not waiting for analysis to finish
* Automatic update of dependency click from 6.7 to 7.0
* State properties are now model properties
* Regenerate swagger client
* Delete strict checks in nullable values
* Use yaml.safe_load due to security reasons
* Supress details from reports in table output
* Print nested dicts nicely in the provenance report
* Omit redundant findings key in the provenance report
* Omit redundant findings key in the provenance report
* Make runtime environment a parameter to CLI
* Center package name and package version in response
* Initial dependency lock
* Return code 4 is no more missing
* Fix linter complains
* Final bits in initial working implementation
* Initial implementation of CLI
* Regenerate swagger client based on the current state
* Regenerate swagger client with new response models
* removed the markdown bear as it depends on some npm tools
* more linter fixes
* missing newline
* preparing for coala
* added a job for creating releases
* added the missing coala config
* added github and zuul configs
* Initial implementation

## Release 0.10.5 (2020-06-11T16:34:41)
* Add thoth-common to requirements.txt
* Add thoth-common
* Release of version 0.10.4
* Add sesheta as maintainer
* Fix handling of enums
* Release of version 0.10.3
* Regenerated swagger to fix thamos error
* Document runtime environments in the config file
* :pushpin: Automatic update of dependency certifi from 2020.4.5.1 to 2020.4.5.2
* :pushpin: Automatic update of dependency pytest from 5.4.2 to 5.4.3
* Increase timeout
* Release of version 0.10.2
* Add missing docstring
* adjust check
* Check for S2I
* Use correct enums
* Introduce source_type flag
* :pushpin: Automatic update of dependency pytest-cov from 2.8.1 to 2.9.0
* :pushpin: Automatic update of dependency six from 1.14.0 to 1.15.0
* Removed unncessary import
* Removed alarm decorator
* Revereted formatting changes
* Revereted formatting changes
* Revereted formatting changes
* wrap moved up
* wrap moved up
* Coala fix
* Added timeout decorater
* Added default timeout to be 15mins
* Added env variable to readme
* Release of version 0.10.1
* :sparkles: added standard project github templates
* better version spec for pyyaml
* manually locked pyyaml :arrow_up:
* lib and CLI should have same behaviour
* :pushpin: Automatic update of dependency toml from 0.10.0 to 0.10.1
* :pushpin: Automatic update of dependency yaspin from 0.16.0 to 0.17.0
* :pushpin: Automatic update of dependency pytest from 5.4.1 to 5.4.2
* Release of version 0.10.0
* Configure requirements format using env variables passed to build
* Respect review comments
* Regenerate client to reflect recent API schema changes
* Document environment variables that can be used
* Fix inconsistency in wait time printed
* Release of version 0.9.4
* Remove unused variable
* :pushpin: Automatic update of dependency click from 7.1.1 to 7.1.2
* Implement retry mechanism to avoid flakes
* Fix spelling
* Provide platform in Thoth's configuration file
* Release of version 0.9.3
* :pushpin: Automatic update of dependency thoth-python from 0.9.1 to 0.9.2
* Remove checks on files as they are in Thoth-python 0.9.2
* Add TODO
* Add explanation for ConfigurationError
* Add files
* Add check on advise_here
* Add check on requirements format if missing from config file
* Added missing docstring
* :pushpin: Automatic update of dependency urllib3 from 1.25.8 to 1.25.9
* Do not report exception if no configuration was found in the directory
* Update lockdown scenario
* :pushpin: Automatic update of dependency certifi from 2020.4.5 to 2020.4.5.1
* :pushpin: Automatic update of dependency certifi from 2019.11.28 to 2020.4.5
* Use RHEL 8
* Update runtime environment example
* No CentOS, use RHEL
* Update scoring example
* Add new line after each log line if structured logging is turned off
* Long description content type missing in setup.py
* Release of version 0.9.2
* Do not fail if obtaining origin fails
* :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
* :pushpin: Automatic update of dependency distro from 1.4.0 to 1.5.0
* Release of version 0.9.1
* Update client to also include dev flag
* Release of version 0.9.0
* Introduce thamos advise with --dev switch
* Colorize logs comming from the cluster
* Parse JSON log produced in the cluster on `thamos log`
* Remove unused imports
* Version 0.8.3
* Pin pyyaml and setuptools for pip's resolver
* Fix requirements parsing in setup.py
* Release of version 0.8.2
* :pushpin: Automatic update of dependency pyyaml from 5.3.1 to 3.13
* Add templates for Kebechet releases
* Fix analusis error detection
* A temporary workaround for workload-operator and analysis propagation
* :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
* Initial dependency lock
* Delete Pipfile.lock
* :pushpin: Automatic update of dependency daiquiri from 2.0.0 to 2.1.0
* Try to detect git origin with request
* Drop raw HTTP support
* :pushpin: Automatic update of dependency requests from 2.22.0 to 2.23.0
* Improve error handling when user-api is not available
* Update .thoth.yaml
* Release of version 0.8.1
* Regenerate client and docs after modifying GitHubApp parameters
* remove unusued parameter
* Modify parameters for GitHub App
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
* Release of version 0.8.0
* Regenerate client with updated GitHub parameter types
* Fix method name
* Add support for GitHub integration to Thamos lib
* Regenerate client for GitHub support
* :pushpin: Automatic update of dependency urllib3 from 1.25.7 to 1.25.8
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.7 to 0.1.8
* :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* :pushpin: Automatic update of dependency six from 1.13.0 to 1.14.0
* :pushpin: Automatic update of dependency yaspin from 0.15.0 to 0.16.0
* :pushpin: Automatic update of dependency thoth-python from 0.9.0 to 0.9.1
* Adjust testsuite to new response format
* Add pip/pip-compile support
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* Update examples
* Happy new year!
* :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
* Release of version 0.7.7
* Inform about no justification made
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.6 to 0.1.7
* Add missing bits for documentation
* Generate Thamos documentation
* Regenerate client to support is_s2i flag
* Propagate is_s2i flag based to User API
* minor updates
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.5 to 0.1.6
* Release of version 0.7.6
* Release of version 0.7.5
* :pencil: there was some ( too much
* :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.4 to 0.1.5
* :pushpin: Automatic update of dependency certifi from 2019.9.11 to 2019.11.28
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* Release of version 0.7.4
* Advised runtime environment is now part of recommended product
* Release of version 0.7.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.6 to 1.25.7
* Adjust output visualization according to new adviser output
* save check for the stack-info
* update thamos with latest user-api
* use https protocol to access test user-api
* :pushpin: Automatic update of dependency six from 1.12.0 to 1.13.0
* :pushpin: Automatic update of dependency python-dateutil from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* Update .codeclimate.yml
* Create .codeclimate.yml
* Create .gitattributes
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Print out Thoth backend version on `thamos version'
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.3 to 0.1.4
* :pushpin: Automatic update of dependency urllib3 from 1.25.5 to 1.25.6
* Do not send empty library usage
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.2 to 0.1.3
* :pushpin: Automatic update of dependency urllib3 from 1.25.4 to 1.25.5
* :pushpin: Automatic update of dependency urllib3 from 1.25.3 to 1.25.4
* :pushpin: Automatic update of dependency certifi from 2019.6.16 to 2019.9.11
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* Link to docs for specific node placement
* Release of version 0.7.2
* Add missing toml in requirements.txt
* Release of version 0.7.1
* Add missing test file
* Enable zuul-pytest on this repo
* :sparkles: now using Fedora 30 and Python 3.7
* Use .coafile from adviser
* Add tests for checking serialization
* Switch from contoml to toml
* Adjust the exception message when file is not set
* State Pipfile is required
* We require Python 3.6+
* Always create config from template if template is set explictly
* Release of version 0.7.0
* :pushpin: Automatic update of dependency yaspin from 0.14.3 to 0.15.0
* :pushpin: Automatic update of dependency invectio from 0.0.6 to 0.0.7
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* :pushpin: Automatic update of dependency invectio from 0.0.5 to 0.0.6
* Document environment variables which can be used during s2i
* :pushpin: Automatic dependency re-locking
* Adjust status command to use the last analysis id
* Filter out calls to Python's standard library
* The configuration template can be user supplied
* Provide a way to note last analysis id into a temporary file
* Decrease maximum sleep time to be more responsive
* Propagate environment configuration in advise_here
* Expand configuration with environment variables
* Hot fix for accessing wrong variable
* Propagate library usage for all Python libraries
* Add ability to configure thamos using envvars
* Correctly propagate invectio version to user-api after library usage detection
* Be more descriptive with logged message about library usage
* :pushpin: Automatic update of dependency invectio from 0.0.4 to 0.0.5
* Fix issue if no report is generated by the recommendation engine
* Release of version 0.6.0
* :boat: updated thamos with latest user-api
* :snail: supporting method for submitting whole build(imagestream and buildlog)
* :pushpin: Automatic update of dependency invectio from 0.0.3 to 0.0.4
* Release of version 0.5.5
* Fix issues with generated swagger client
* Remove trailing whitespace
* Fix propagation of `limit_latest_versions` parameter
* Round up maximum line length allowed for Coala
* Be more verbose about adviser input on debug
* Use test environment as a source for swagger client
* Regenerate swagger client
* Removed unecessary from get_analysis_results
* Duplicate origin param
* Added origin to advise
* Fixed
* Release of version 0.5.4
* Add `nowrite` parameter to create_default_config
* auto swagger client generated
* Analysis ID is second argument
* Analysis ID is second argument
* Remove trailing whitespace
* Added origin option to provenance and advise
* Make sure to follow recomendation type priority
* Fix issue #182
* :pushpin: Automatic update of dependency texttable from 1.6.1 to 1.6.2
* Update docs on how autogenerating code is done
* lib analysis results
* Fix URL to OpenAPI YAML
* Release of version 0.5.3
* Release of version 0.5.2
* Release of version 0.5.1
* Release of version 0.5.0
* Fix handling based on arguments if no config file is needed
* :pushpin: Automatic update of dependency certifi from 2019.3.9 to 2019.6.16
* Release of version 0.4.3
* :pushpin: Automatic update of dependency invectio from 0.0.1 to 0.0.3
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* :pushpin: Automatic update of dependency yaspin from 0.14.2 to 0.14.3
* :pushpin: Automatic update of dependency urllib3 from 1.24.3 to 1.25.3
* Include Thoth's configuration file for sdist distribution
* rm trailing white space
* Removed self keyword
* Remove api arg
* Accidental white space
* Forgot to remove arguments
* Forgot to remove arguments
* Manual formatting
* Auto format
* Provenance here lib function
* Use own user-agent for user requests
* Thamos Library advise_here (#159)
* Edit styling
* Edit styling
* python/black styling
* Pipfile.lock is not auto added
* No need to include API client in args
* Created library function for advising current directory
* State configuration option for disabling progressbar
* Adjust default Thoth host to talk to
* Provide ability to supply configuration file template
* Report warning if no library usage was gathered
* Release of version 0.4.2
* Add missing Invectio requirement
* Release of version 0.4.1
* Use arguments instead of kwargs to be compatible with openapi
* Release of version 0.4.0
* Regenerate for new implementation
* Use openapi 3 implementation for swagger client generation
* Re-generate swagger client
* Integrate static analysis using Invectio
* :pushpin: Automatic update of dependency urllib3 from 1.24.2 to 1.24.3
* :pushpin: Automatic update of dependency yaspin from 0.14.1 to 0.14.2
* Re-generate for transition to Dgraph
* :pushpin: Automatic update of dependency urllib3 from 1.24.1 to 1.24.2
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* Fix link to notebook
* :sparkles: using -stage now, removed some quirks
* :sparkles: added a container build script and adjusted some readmes
* Log Thoth's API URL to show to which instance a user talks to
* bug fix on TLS turned on
* Used urljoin for maintaining semantic version of url
* Correctly handle errors from reports and empty reports
* Make sure configuration changes are propagated to config file
* Match operating system with solver results
* Pin down more dependencies
* Enable limit_latest_versions to be configured from configuration
* Update .thoth.yaml
* Fix Coala complains
* Adjust runtime-environment example to reflect data in Test environment
* Release of version 0.3.1
* Add Thoth's configuration file
* Provide environment type in library adapter
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Regenerate client
* Target coala issues
* Do not write changes in configuration if there are no changes
* Adjust Thoth's configuration based on recommendations
* Regenerate swagger-client, add limit latest versions option
* Fix formatting
* Use safe_dump() instead of dump()
* Automatic dependency re-locking
* Add ability to expand entries in configuration file
* Add ability to create configuration in non-interactive mode
* Demo with lower flask version
* Move resolved stacks to misc repo
* Fix issues reported by coala
* Add files supporting "scoring" scenario
* Fix coala complains
* Add files supporting "scoring" scenario
* Add README for runtime environment scenario
* Remove requires section in example
* Minor improvements in README file
* Minor improvements in README file
* Add README file for lockdown example
* Add example flask application to verify stack works
* fixed the wrong version specifier
* Adjust recommendation type to latest
* all the use cases
* Release of version 0.3.0
* Release of version 0.2.0
* Fix Coala issues
* Automatic update of dependency texttable from 1.6.0 to 1.6.1
* a basic lockdown example
* Remove redundant parentheses
* Introduce output formats for Thamos
* Automatic update of dependency thoth-analyzer from 0.1.0 to 0.1.2
* Add missing MANIFEST.in
* Perform autodiscovery for host runtime environment
* Use black for formatting
* Explicitly propagate recommendation type if user asked so
* Fix clash of options for CLI
* Submit runtime environments to Thoth
* Re-generate swagger client files
* Make configuration entries minimal
* Automatic update of dependency distro from 1.3.0 to 1.4.0
* Automatic update of dependency python-dateutil from 2.7.5 to 2.8.0
* Adjust configuration file structure based on comments
* Rename configuration to runtime_environments
* Make a list of configurations
* State requirements format in the config file
* Adjust structure of configuration file
* Introduce log and status sub-commands
* Introduce a way how to suppress TLS warnings
* It's already 2019
* Update README with lib/CLI instructions
* Adjust TLS verify property when thamos is used as a lib
* Provide routine for submitting and retrieving image analyses
* Automatic update of dependency yaspin from 0.14.0 to 0.14.1
* Automatic update of dependency texttable from 1.5.0 to 1.6.0
* Add missing requirements
* Fix exception happening if there was an error in analysis
* Release of version 0.1.0
* Use contoml instead of toml, it has prettier output
* Warn on using insecure network without TLS
* Provide some defaults for runtime environmnet configuration
* Remove no longer relevant TODO
* Perform API discovery when communicating with remote
* Remove unused parameters to CLI commands
* Propagate error in report to process exit code
* Give user guidance on how to configure thamos
* Regenerate thamos swagger client
* Add guards to library functions
* CLI always uses the highest rated software stack
* Serialize into a file correctly
* Remove invalid parameter to TOML
* Automatic update of dependency six from 1.11.0 to 1.12.0
* Automatic update of dependency certifi from 2018.10.15 to 2018.11.29
* Wrong index was on server side
* Fix report indexing
* Fix missing parameter
* Propagate force parameters to bypass server-side cache
* Point to upshift test environment by default
* Add long description for PyPI
* Update to correctly propagate runtime environment
* Update swagger client with hardware info on input
* Make CI happy again
* Adjust library's advise implementation for current implementation
* Update to reflect the current API implementation
* Automatic update of dependency texttable from 1.4.0 to 1.5.0
* Automatic update of dependency urllib3 from 1.24 to 1.24.1
* Do not use trailing slash in url
* Automatic update of dependency python-dateutil from 2.7.4 to 2.7.5
* use thoth-* jobs in pipeline
* added .vscode/
* Automatic update of dependency python-dateutil from 2.7.3 to 2.7.4
* Automatic update of dependency urllib3 from 1.23 to 1.24
* Automatic update of dependency thoth-analyzer from 0.0.7 to 0.1.0
* We use JSON as an output format
* Regenerate client to include dependency monkey API
* Logs can be nullable
* Introduce --no-wait flag for not waiting for analysis to finish
* Automatic update of dependency click from 6.7 to 7.0
* State properties are now model properties
* Regenerate swagger client
* Delete strict checks in nullable values
* Use yaml.safe_load due to security reasons
* Supress details from reports in table output
* Print nested dicts nicely in the provenance report
* Omit redundant findings key in the provenance report
* Omit redundant findings key in the provenance report
* Make runtime environment a parameter to CLI
* Center package name and package version in response
* Initial dependency lock
* Return code 4 is no more missing
* Fix linter complains
* Final bits in initial working implementation
* Initial implementation of CLI
* Regenerate swagger client based on the current state
* Regenerate swagger client with new response models
* removed the markdown bear as it depends on some npm tools
* more linter fixes
* missing newline
* preparing for coala
* added a job for creating releases
* added the missing coala config
* added github and zuul configs
* Initial implementation

## Release 0.10.6 (2020-07-09T10:20:39)
* Use urljoin not relative to base (#471)
* Do not use urljoin logic for host (#470)
* Default to pipenv (#468)
* :pushpin: Automatic update of dependency thoth-common from 0.14.0 to 0.14.1 (#467)
* :pushpin: Automatic update of dependency thoth-common from 0.13.13 to 0.14.0 (#465)
* :pushpin: Automatic update of dependency thoth-common from 0.13.12 to 0.13.13 (#463)
* :pushpin: Automatic update of dependency thoth-common from 0.13.12 to 0.13.13 (#462)
* :pushpin: Automatic update of dependency thoth-common from 0.13.12 to 0.13.13 (#461)
* :pushpin: Automatic update of dependency thoth-common from 0.13.12 to 0.13.13 (#460)
* :pushpin: Automatic update of dependency certifi from 2020.4.5.2 to 2020.6.20 (#459)
* :pushpin: Automatic update of dependency certifi from 2020.4.5.2 to 2020.6.20 (#458)
* :pushpin: Automatic update of dependency certifi from 2020.4.5.2 to 2020.6.20 (#457)
* :pushpin: Automatic update of dependency certifi from 2020.4.5.2 to 2020.6.20 (#456)
* Create OWNERS
* :pushpin: Automatic update of dependency thoth-common from 0.13.11 to 0.13.12
* :pushpin: Automatic update of dependency thoth-common from 0.13.11 to 0.13.12
* :pushpin: Automatic update of dependency thoth-python from 0.9.2 to 0.10.0
* :pushpin: Automatic update of dependency requests from 2.23.0 to 2.24.0
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.4 to 1.4.1
* :pushpin: Automatic update of dependency pytest-cov from 2.9.0 to 2.10.0

## Release 0.11.0 (2020-08-07T16:44:50)
* Swtich advise to result route (#475)
* :pushpin: Automatic update of dependency yaspin from 0.18.0 to 1.0.0 (#490)
* Running_swagger_codegen (#485)
* :pushpin: Automatic update of dependency pytest from 5.4.3 to 6.0.1 (#487)
* :pushpin: Automatic update of dependency thoth-common from 0.14.2 to 0.16.0 (#486)
* :arrow_down: removed the files as they are no longer required
* :pushpin: Automatic update of dependency pytest-timeout from 1.4.1 to 1.4.2 (#484)
* :pushpin: Automatic update of dependency pytest-timeout from 1.4.1 to 1.4.2 (#483)
* :pushpin: Automatic update of dependency pytest-timeout from 1.4.1 to 1.4.2 (#482)
* :pushpin: Automatic update of dependency thoth-common from 0.14.1 to 0.14.2 (#481)
* :pushpin: Automatic update of dependency thoth-common from 0.14.1 to 0.14.2 (#480)
* :pushpin: Automatic update of dependency yaspin from 0.17.0 to 0.18.0 (#479)
* :pushpin: Automatic update of dependency urllib3 from 1.25.9 to 1.25.10 (#478)
* Extend recommendation type (#477)
* Remove latest versions limitation (#476)
* MyPy typing solved
* add pre-commit and fix all except mypy errors

## Release 0.11.1 (2020-08-12T13:03:05)
* :pushpin: Automatic update of dependency thoth-python from 0.10.0 to 0.10.1 (#494)
* Fixed wrong exception (#493)

## Release 0.12.0 (2020-09-01T12:53:00)
### Features
* Produce TLS related warning just once per session in logs (#501)
* Update default .thoth.yaml generated (#497)
### Bug Fixes
* Do not retry client requests if the analysis was not successful (#503)
### Improvements
* Perform status obtaining request only for debug level (#500)
* Give up querying server if the response signalizes unsuccessful request
### Non-functional
* Add GitHub pull request template
### Automatic Updates
* :pushpin: Automatic update of dependency thoth-common from 0.16.1 to 0.17.0 (#505)
* :pushpin: Automatic update of dependency pytest-cov from 2.10.0 to 2.10.1 (#499)
* :pushpin: Automatic update of dependency thoth-common from 0.16.0 to 0.16.1 (#498)

## Release 0.12.1 (2020-09-04T08:53:14)
### Features
* Fix environment dict expansion (#511)
### Automatic Updates
* :pushpin: Automatic update of dependency thoth-common from 0.17.0 to 0.17.2 (#509)

## Release 0.12.2 (2020-09-07T20:04:14)
### Bug Fixes
* Raise appropriate exception when Thoth backend is down (#515)
### Improvements
* Fix URL when obtaining results for provenance and image analyses
### Automatic Updates
* :pushpin: Automatic update of dependency texttable from 1.6.2 to 1.6.3 (#519)

## Release 1.0.0 (2020-09-15T09:04:07)
### Features
* Provide aliased groups for commands (#521)
* Fix missing requirements
### Improvements
* Use rich output to improve console output (#518)

## Release 1.0.1 (2020-09-25T06:19:54)
### Features
* Link document with recommendation types
### Bug Fixes
* Allow users not to submit lock file with the request (#532)
### Automatic Updates
* :pushpin: Automatic update of dependency thoth-common from 0.19.0 to 0.20.0 (#536)
* :pushpin: Automatic update of dependency thoth-python from 0.10.1 to 0.10.2 (#535)
* :pushpin: Automatic update of dependency rich from 6.2.0 to 7.0.0 (#533)
* :pushpin: Automatic update of dependency rich from 6.1.2 to 6.2.0 (#525)
* :pushpin: Automatic update of dependency thoth-common from 0.18.3 to 0.19.0 (#531)
* :pushpin: Automatic update of dependency thoth-common from 0.18.3 to 0.19.0 (#530)

## Release 1.1.0 (2020-10-27T10:30:07)
### Features
* Regenerate client (#539)
### Bug Fixes
* Provide stack info when adviser fails

## Release 1.1.1 (2020-10-28T08:30:23)
### Features
* Fix report missing case (#553)
* pre-commit initiated reformatting
### Bug Fixes
* :star: pre-commit fixes (#562)
* fixed some pre-commit config, added mypy ini file to ignore the misc errors (hello is a duplicate module)
### Automatic Updates
* :pushpin: Automatic update of dependency urllib3 from 1.25.10 to 1.25.11 (#561)
* :pushpin: Automatic update of dependency urllib3 from 1.25.10 to 1.25.11 (#555)
* :pushpin: Automatic update of dependency yaspin from 1.0.0 to 1.2.0 (#556)
* :pushpin: Automatic update of dependency rich from 7.0.0 to 9.1.0 (#558)
* :pushpin: Automatic update of dependency pytest from 6.0.2 to 6.1.1 (#559)
* :pushpin: Automatic update of dependency thoth-common from 0.20.0 to 0.20.2 (#557)

## Release 1.2.0 (2020-11-03T15:30:51)
### Features
* Fold on overflow when printing output (#570)
### Improvements
* Add logger name and padding to logs output (#568)
### Automatic Updates
* :pushpin: Automatic update of dependency toml from 0.10.1 to 0.10.2 (#576)
* :pushpin: Automatic update of dependency toml from 0.10.1 to 0.10.2 (#575)
* :pushpin: Automatic update of dependency toml from 0.10.1 to 0.10.2 (#574)
* :pushpin: Automatic update of dependency thoth-common from 0.20.2 to 0.20.4 (#573)
* :pushpin: Automatic update of dependency thoth-common from 0.20.2 to 0.20.4 (#572)
* :pushpin: Automatic update of dependency pytest from 6.1.1 to 6.1.2 (#567)

## Release 1.3.0 (2020-11-10T10:50:54)
### Features
* Implement thamos install command (#581)
### Improvements
* Switch recommended stack report and stack info (#582)
### Automatic Updates
* :pushpin: Automatic update of dependency rich from 9.1.0 to 9.2.0 (#589)
* :pushpin: Automatic update of dependency rich from 9.1.0 to 9.2.0 (#588)
* :pushpin: Automatic update of dependency daiquiri from 2.1.1 to 3.0.0 (#587)
* :pushpin: Automatic update of dependency invectio from 0.0.7 to 0.1.0 (#586)
* :pushpin: Automatic update of dependency daiquiri from 2.1.1 to 3.0.0 (#585)
* :pushpin: Automatic update of dependency certifi from 2020.6.20 to 2020.11.8 (#584)

## Release 1.3.1 (2020-11-10T16:57:41)
### Features
* Remove sleep before first attempt to obtain results (#569)
* Adjust host to User API in the README (#597)
### Automatic Updates
* :pushpin: Automatic update of dependency rich from 9.1.0 to 9.2.0 (#595)
* :pushpin: Automatic update of dependency micropipenv from 1.0.0 to 1.0.1 (#594)
* :pushpin: Automatic update of dependency rich from 9.1.0 to 9.2.0 (#593)

## Release 1.4.0 (2020-11-23T13:50:23)
### Features
* Introduce advise_using_config to enable supplying config file (#623)
* Notify users about hash mismatch in Pipenv files (#618)
* Notify users that development dependencies will not be installed (#616)
* Add a link to justification on timeout (#611)
* Notify users about requirements used and project root (#610)
* Add option for writing advised manifest changes (#605)
* Set has no extend method but update (#608)
* Remove duplicit records in library usage (#600)
### Improvements
* Adjust datatype of parameters in _write_files method (#625)
### Other
* Refactor duplicate logic (#621)
* Match colors shown in logs with logs in CLI (#601)
### Automatic Updates
* :pushpin: Automatic update of dependency requests from 2.24.0 to 2.25.0 (#607)
* :pushpin: Automatic update of dependency requests from 2.24.0 to 2.25.0 (#606)
* :pushpin: Automatic update of dependency requests from 2.24.0 to 2.25.0 (#604)
* :pushpin: Automatic update of dependency urllib3 from 1.25.11 to 1.26.2 (#603)
* :pushpin: Automatic update of dependency urllib3 from 1.25.11 to 1.26.2 (#602)

## Release 1.5.0 (2020-11-26T16:52:14)
### Features
* Introduce overlays to thamos (#631)
* Introduce thamos check command (#632)

## Release 1.5.1 (2020-11-30T09:47:24)
### Features
* Improve obtaining Thoth backend version information (#642)
* Add missing jsonschema to requirements.txt (#641)
* :honeybee: Deliver missing package module to pypi github issue template (#638)

## Release 1.5.2 (2020-11-30T20:56:57)
### Features
* Fix s2i detection (#649)
* :arrow_up: Automatic update of dependencies by kebechet. (#647)

## Release 1.5.3 (2021-01-05T12:05:48)
### Features
* Port to Python 3.8 (#663)
* Remove coala from requirements (#662)
* :arrow_up: Automatic update of dependencies by kebechet. (#657)
* Treat UBI and RHEL as synonyms (#654)
### Improvements
* Load configuration just once and avoid misleading warnings (#659)

## Release 1.5.4 (2021-01-06T06:23:27)
### Features
* :arrow_up: Automatic update of dependencies by kebechet. (#668)
* :arrow_up: Automatic update of dependencies by kebechet. (#667)
### Improvements
* Perform normalization of os name and os version (#658)

## Release 1.5.5 (2021-01-11T10:06:15)
### Features
* :arrow_up: Automatic update of dependencies by kebechet. (#678)
* Do not override list builtin (#676)
* :arrow_up: Automatic update of dependencies by kebechet. (#673)
* :arrow_up: Automatic update of dependencies by kebechet. (#671)
### Improvements
* Add commands for showing and listing runtime environments (#675)

## Release 1.6.0 (2021-01-12T19:19:51)
### Features
* :arrow_up: Automatic update of dependencies by kebechet. (#687)
* Adjust build analysis library handling (#684)
* Regenerate build analysis response models (#683)
* :arrow_up: Automatic update of dependencies by kebechet. (#682)
* Regenerate and update thamos client (#681)
### Improvements
* removed bissenbay, thanks for your contributions!

## Release 1.6.1 (2021-01-19T15:12:32)
### Features
* Allow nullables in post build analysis response (#695)
* Fix parameter propagation in post_build (#693)
* :arrow_up: Automatic update of dependencies by kebechet. (#694)
* :arrow_up: Automatic update of dependencies by kebechet. (#692)
* Remove buildlog analyzer results endpoints (#691)
* add the SIG label

## Release 1.7.0 (2021-01-21T11:42:29)
### Features
* Add Kebechet issue templates
* :arrow_up: Automatic update of dependencies by kebechet. (#700)
* Extend Thamos configuration file with additional options (#672)
* :arrow_up: Automatic update of dependencies by kebechet. (#699)
* :arrow_up: Automatic update of dependencies by kebechet. (#698)

## Release 1.8.0 (2021-02-01T20:33:46)
### Features
* Fix CUDA version handling (#710)
* Regenerate client to support S2I endpoint (#709)
* Discover Thoth's s2i tooling to use it in recommendations (#704)
* :arrow_up: Automatic update of dependencies by kebechet. (#706)

## Release 1.9.0 (2021-02-02T11:29:23)
### Features
* Add section about hw and s2i commands to the README file
* Fix link to Thoth s2i description
* Regenerate client with nullable hardware parameters
* Update S2I endpoint response
### Improvements
* Provide thamos hw and thamos s2i commands (#716)
* Regenerate to support new User API structure

## Release 1.10.0 (2021-02-02T20:02:20)
### Features
* Add support for passing options to pip during thamos install (#722)

## Release 1.11.0 (2021-02-09T12:09:06)
### Features
* :arrow_up: Automatic update of dependencies by Kebechet (#730)

## Release 1.11.1 (2021-02-09T15:20:50)
### Features
* Fix URL creation when obtaining analysis status (#733)

## Release 1.12.0 (2021-02-16T14:39:50)
### Features
* Add method for adding new runtime environments (#744)
* Introduce thamos index command for listing package indexes available (#743)
* :arrow_up: Automatic update of dependencies by Kebechet (#746)
* :arrow_up: Automatic update of dependencies by Kebechet (#741)
* Update thoth yaml (#740)
* Regenerate client respecting API changes (#738)

## Release 1.13.0 (2021-02-23T09:53:26)
### Features
* Adjust client to respect recent API response schema changes (#768)
* Add warning message when repo setup might be misleading (#767)
* Keep Thoth section when generating Pipfile (#766)
* Fix obtaining status information for provenance-checker
* Correctly pass debug option to provenance-check command
* Any invalid thamos command notifies about creating overlays
* Handle CLI exceptions
* Generate default Pipfile if none is present in the project (#755)
* :arrow_up: Automatic update of dependencies by Kebechet (#760)
* Turn on overlays by default (#757)
* :arrow_up: Automatic update of dependencies by Kebechet (#756)
* Add some examples to the README file
* Minor fixes, be more verbose about output
* Provide `thamos add' functionality to add packages to Pipenv files
* :arrow_up: Automatic update of dependencies by Kebechet (#751)
* :arrow_up: Automatic update of dependencies by Kebechet (#750)
### Bug Fixes
* Support requirement files when `thamos add` or `thamos remove` is called (#758)
### Improvements
* Create directory structure for overlay if not present yet
### Other
* Implement thamos remove command

## Release 1.14.0 (2021-03-04T17:37:20)
### Features
* Fix aggregating library usage (#779)
* Keep Thoth section in Pipfile if Pipenv files are generated using Thoth (#776)
* Do not show Warehouse API url in the index listing (#775)
* :arrow_up: Automatic update of dependencies by Kebechet (#774)
* Reset loaded config in memory (#771)

## Release 1.15.0 (2021-03-10T10:42:36)
### Features
* State .venv in the README file
* Provide an example to install with pip arguments
* Reformat using black
* Remove duplicite call to micropipenv
* Add examples to CLI help
* Detect virtual environment running
* Add capability to manage virtual environments for the application
* :arrow_up: Automatic update of dependencies by Kebechet (#798)
* Print information about requirements installed (#797)
* thamos ci updates (#794)
* Document thamos install in the README file (#787)
* Improve help messages printed to users
* :arrow_up: Automatic update of dependencies by Kebechet (#793)
* :arrow_up: Automatic update of dependencies by Kebechet (#792)
* :arrow_up: Automatic update of dependencies by Kebechet (#789)
* :arrow_up: Automatic update of dependencies by Kebechet (#786)
* allow aicoe-ci to release the module to pypi (#783)
### Bug Fixes
* Issue an error if a user tries to install missing dev requirements (#796)
### Improvements
* Discover base image based on IMAGE_NAME and IMAGE_TAG
### Other
* Exclude autogenerated code from pre-commit (#790)

## Release 1.16.0 (2021-03-23T17:50:09)
### Features
* add .typed to manifest file
* add kebechet metadata to thamos lib functions
* Be more verbose when printing host information detected
* Introduce a parameter to adjust timeout for analyses
* Fix generating base image
* Add py.typed
* :arrow_up: Automatic update of dependencies by Kebechet (#807)
* :arrow_up: Automatic update of dependencies by Kebechet
### Bug Fixes
* Handle cases when virtual environment was not created yet

## Release 1.16.1 (2021-03-25T14:38:18)
### Improvements
* Fix typo in the parameter
* make functions part of thamos.lib

## Release 1.17.0 (2021-04-13T09:24:16)
### Features
* Provide ability to pass token on the client side
* Fix pre-commit issues (#833)
* Link thoth-station/cli-examples repository
* Adjust endpoint calls in the lib to supply objects
* Regenerate client to conform to inputs
* Add URL page
* Adjust TimeoutError message
### Bug Fixes
* Fix overlay name - it must not contain colon (#835)
### Other
* Adjust code to include authentication info
* remove reviewer

## Release 1.18.0 (2021-04-28T08:31:29)
### Features
* Add support for constraints files (#841)
* :arrow_up: Automatic update of dependencies by Kebechet (#843)

## Release 1.18.1 (2021-04-30T12:20:29)
### Features
* Virtualenv cli_run is available since 20.0.3 (#848)
* :arrow_up: Automatic update of dependencies by Kebechet (#847)

## Release 1.18.2 (2021-06-03T19:39:49)
### Features
* Respect tls_verify configuration option from the config file
* :arrow_up: Automatic update of dependencies by Kebechet (#859)
* :arrow_up: Automatic update of dependencies by Kebechet (#858)
* :hatched_chick: update the prow resource limits (#857)
* :arrow_up: Automatic update of dependencies by Kebechet (#854)
### Bug Fixes
* Be more visible about errors reported (#855)

## Release 1.18.3 (2021-06-08T09:42:33)
### Features
* add project_url so that we show more info on pypi :pencil:
* Introduce labels concept
* Regenerate client to support labels
### Improvements
* Document how to use labels

## Release 1.18.4 (2021-06-25T05:11:17)
### Features
* Adjust copyright notice in headers
* Log recommendation type used in the advise request
* :arrow_up: Automatic update of dependencies by Kebechet
* Use latest recommendations by default
* Require at least one runtime environment set in the config file

## Release 1.19.0 (2021-07-08T13:47:02)
### Features
* Set Python version based on .thoth.yaml file
* Add a link to labels demo
* :arrow_up: Automatic update of dependencies by Kebechet
* advise_here uses overlay directories

## Release 1.20.0 (2021-07-26T20:16:39)
### Features
* Implement thamos graph command
* :arrow_up: Automatic update of dependencies by Kebechet
* Fix spacing in CLI examples
