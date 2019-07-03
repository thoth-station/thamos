# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AdviseInputApplicationStack(object):
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
        'requirements': 'str',
        'requirements_format': 'str[str]',
        'requirements_lock': 'str'
    }

    attribute_map = {
        'requirements': 'requirements',
        'requirements_format': 'requirements_format',
        'requirements_lock': 'requirements_lock'
    }

    def __init__(self, requirements=None, requirements_format=None, requirements_lock=None):  # noqa: E501
        """AdviseInputApplicationStack - a model defined in Swagger"""  # noqa: E501
        self._requirements = None
        self._requirements_format = None
        self._requirements_lock = None
        self.discriminator = None
        self.requirements = requirements
        if requirements_format is not None:
            self.requirements_format = requirements_format
        self.requirements_lock = requirements_lock

    @property
    def requirements(self):
        """Gets the requirements of this AdviseInputApplicationStack.  # noqa: E501

        Direct dependencies for the application stack.  # noqa: E501

        :return: The requirements of this AdviseInputApplicationStack.  # noqa: E501
        :rtype: str
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this AdviseInputApplicationStack.

        Direct dependencies for the application stack.  # noqa: E501

        :param requirements: The requirements of this AdviseInputApplicationStack.  # noqa: E501
        :type: str
        """
        if requirements is None:
            raise ValueError("Invalid value for `requirements`, must not be `None`")  # noqa: E501

        self._requirements = requirements

    @property
    def requirements_format(self):
        """Gets the requirements_format of this AdviseInputApplicationStack.  # noqa: E501

        Lockfile format - defaults to pipenv if not explicitly specified.   # noqa: E501

        :return: The requirements_format of this AdviseInputApplicationStack.  # noqa: E501
        :rtype: str[str]
        """
        return self._requirements_format

    @requirements_format.setter
    def requirements_format(self, requirements_format):
        """Sets the requirements_format of this AdviseInputApplicationStack.

        Lockfile format - defaults to pipenv if not explicitly specified.   # noqa: E501

        :param requirements_format: The requirements_format of this AdviseInputApplicationStack.  # noqa: E501
        :type: str[str]
        """

        self._requirements_format = requirements_format

    @property
    def requirements_lock(self):
        """Gets the requirements_lock of this AdviseInputApplicationStack.  # noqa: E501

        Fully pinned down dependency stack.  # noqa: E501

        :return: The requirements_lock of this AdviseInputApplicationStack.  # noqa: E501
        :rtype: str
        """
        return self._requirements_lock

    @requirements_lock.setter
    def requirements_lock(self, requirements_lock):
        """Sets the requirements_lock of this AdviseInputApplicationStack.

        Fully pinned down dependency stack.  # noqa: E501

        :param requirements_lock: The requirements_lock of this AdviseInputApplicationStack.  # noqa: E501
        :type: str
        """
        if requirements_lock is None:
            raise ValueError("Invalid value for `requirements_lock`, must not be `None`")  # noqa: E501

        self._requirements_lock = requirements_lock

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
        if issubclass(AdviseInputApplicationStack, dict):
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
        if not isinstance(other, AdviseInputApplicationStack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other