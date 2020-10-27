# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.6.0-dev

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PythonPackageIndexesInner(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"url": "str", "warehouse_api_url": "str", "verify_ssl": "bool"}

    attribute_map = {
        "url": "url",
        "warehouse_api_url": "warehouse_api_url",
        "verify_ssl": "verify_ssl",
    }

    def __init__(self, url=None, warehouse_api_url=None, verify_ssl=None):  # noqa: E501
        """PythonPackageIndexesInner - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._warehouse_api_url = None
        self._verify_ssl = None
        self.discriminator = None
        self.url = url
        self.warehouse_api_url = warehouse_api_url
        self.verify_ssl = verify_ssl

    @property
    def url(self):
        """Gets the url of this PythonPackageIndexesInner.  # noqa: E501

        URL to the Python simple repository as described in PEP 503.  # noqa: E501

        :return: The url of this PythonPackageIndexesInner.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PythonPackageIndexesInner.

        URL to the Python simple repository as described in PEP 503.  # noqa: E501

        :param url: The url of this PythonPackageIndexesInner.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError(
                "Invalid value for `url`, must not be `None`"
            )  # noqa: E501

        self._url = url

    @property
    def warehouse_api_url(self):
        """Gets the warehouse_api_url of this PythonPackageIndexesInner.  # noqa: E501

        URL to the warehouse API.  # noqa: E501

        :return: The warehouse_api_url of this PythonPackageIndexesInner.  # noqa: E501
        :rtype: str
        """
        return self._warehouse_api_url

    @warehouse_api_url.setter
    def warehouse_api_url(self, warehouse_api_url):
        """Sets the warehouse_api_url of this PythonPackageIndexesInner.

        URL to the warehouse API.  # noqa: E501

        :param warehouse_api_url: The warehouse_api_url of this PythonPackageIndexesInner.  # noqa: E501
        :type: str
        """
        if warehouse_api_url is None:
            raise ValueError(
                "Invalid value for `warehouse_api_url`, must not be `None`"
            )  # noqa: E501

        self._warehouse_api_url = warehouse_api_url

    @property
    def verify_ssl(self):
        """Gets the verify_ssl of this PythonPackageIndexesInner.  # noqa: E501

        Use secured connection to warehouse.  # noqa: E501

        :return: The verify_ssl of this PythonPackageIndexesInner.  # noqa: E501
        :rtype: bool
        """
        return self._verify_ssl

    @verify_ssl.setter
    def verify_ssl(self, verify_ssl):
        """Sets the verify_ssl of this PythonPackageIndexesInner.

        Use secured connection to warehouse.  # noqa: E501

        :param verify_ssl: The verify_ssl of this PythonPackageIndexesInner.  # noqa: E501
        :type: bool
        """
        if verify_ssl is None:
            raise ValueError(
                "Invalid value for `verify_ssl`, must not be `None`"
            )  # noqa: E501

        self._verify_ssl = verify_ssl

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(PythonPackageIndexesInner, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PythonPackageIndexesInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
