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

class Log(object):
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
    swagger_types = {
        'log': 'str',
        'apiversion': 'str',
        'kind': 'str',
        'metadata': 'str'
    }

    attribute_map = {
        'log': 'log',
        'apiversion': 'apiversion',
        'kind': 'kind',
        'metadata': 'metadata'
    }

    def __init__(self, log=None, apiversion=None, kind=None, metadata=None):  # noqa: E501
        """Log - a model defined in Swagger"""  # noqa: E501
        self._log = None
        self._apiversion = None
        self._kind = None
        self._metadata = None
        self.discriminator = None
        self.log = log
        if apiversion is not None:
            self.apiversion = apiversion
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata

    @property
    def log(self):
        """Gets the log of this Log.  # noqa: E501

        A full build or installation log that was output during image build.   # noqa: E501

        :return: The log of this Log.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this Log.

        A full build or installation log that was output during image build.   # noqa: E501

        :param log: The log of this Log.  # noqa: E501
        :type: str
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def apiversion(self):
        """Gets the apiversion of this Log.  # noqa: E501

        BuildLog api version.   # noqa: E501

        :return: The apiversion of this Log.  # noqa: E501
        :rtype: str
        """
        return self._apiversion

    @apiversion.setter
    def apiversion(self, apiversion):
        """Sets the apiversion of this Log.

        BuildLog api version.   # noqa: E501

        :param apiversion: The apiversion of this Log.  # noqa: E501
        :type: str
        """

        self._apiversion = apiversion

    @property
    def kind(self):
        """Gets the kind of this Log.  # noqa: E501

        Type of log.   # noqa: E501

        :return: The kind of this Log.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Log.

        Type of log.   # noqa: E501

        :param kind: The kind of this Log.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this Log.  # noqa: E501


        :return: The metadata of this Log.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Log.


        :param metadata: The metadata of this Log.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Log, dict):
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
        if not isinstance(other, Log):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
