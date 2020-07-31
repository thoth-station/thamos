#!/usr/bin/env bash
# Generate OpenAPI client from User-API's swagger specification.
# Fridolin Pokorny <fridolin.pokorny@gmail.com>
# Saisankar Gochhayat <saisankargochhayat@gmail.com>
#
# This file automates generation of the openapi client and makes it reproducible. Run this
# file to automatically generate Python openapi client for interacting with User-API.

set -ex

USER_API_SWAGGER_YAML=${1:-'https://test.thoth-station.ninja/api/v1/openapi.json'}
OPENAPI_GENERATOR_CLI_VERSION="4.3.1"

function die() {
    echo $@ 1>&2
    exit 1
}

which which > /dev/null || die "Please install which command to continue"
which wget > /dev/null  || die "Please install wget to continue"
which find > /dev/null  || die "Please install find utility to continue"
which java > /dev/null  || die "Please install java to continue"


[[ -f 'openapi-generator-cli.jar' ]] || {
    wget -O openapi-generator-cli.jar \
    "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/${OPENAPI_GENERATOR_CLI_VERSION}/openapi-generator-cli-${OPENAPI_GENERATOR_CLI_VERSION}.jar"
}


rm -rf swagger-codegen-output/ Documentation/
java -jar openapi-generator-cli.jar generate \
     -i "${USER_API_SWAGGER_YAML}" \
     -g python \
     -o swagger-codegen-output \
     -c swagger-codegen.json

rm -rf thamos/swagger_client
cp -r swagger-codegen-output/thamos/swagger_client/ thamos/swagger_client
# There is a bug in swagger-codegen - it does not respect sub-package for some files, this is a simple workaround.
# find swagger-codegen-output/thamos.swagger_client/ -iname '*.py' -exec sed -i 's/^from thoth/from thamos.swagger_client.thoth/' {} \+
# cp -r swagger-codegen-output/thamos.swagger_client/* thamos/swagger_client
cp -r swagger-codegen-output/docs Documentation
