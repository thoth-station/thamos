
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

