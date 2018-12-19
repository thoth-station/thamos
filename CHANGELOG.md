
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
