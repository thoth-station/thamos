
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
