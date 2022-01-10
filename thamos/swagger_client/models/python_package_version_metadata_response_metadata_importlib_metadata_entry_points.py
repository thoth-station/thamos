# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.7.0-dev

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints(object):
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
        'group': 'str',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'group': 'group',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, group=None, name=None, value=None):  # noqa: E501
        """PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints - a model defined in Swagger"""  # noqa: E501
        self._group = None
        self._name = None
        self._value = None
        self.discriminator = None
        self.group = group
        self.name = name
        self.value = value

    @property
    def group(self):
        """Gets the group of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.  # noqa: E501


        :return: The group of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.


        :param group: The group of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.  # noqa: E501
        :type: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def name(self):
        """Gets the name of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.  # noqa: E501


        :return: The name of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.


        :param name: The name of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.  # noqa: E501


        :return: The value of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.


        :param value: The value of this PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints, dict):
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
        if not isinstance(other, PythonPackageVersionMetadataResponseMetadataImportlibMetadataEntryPoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other