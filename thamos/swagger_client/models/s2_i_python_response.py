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


class S2IPythonResponse(object):
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
        's2i': 'list[S2IPythonResponseS2i]'
    }

    attribute_map = {
        's2i': 's2i'
    }

    def __init__(self, s2i=None):  # noqa: E501
        """S2IPythonResponse - a model defined in Swagger"""  # noqa: E501
        self._s2i = None
        self.discriminator = None
        self.s2i = s2i

    @property
    def s2i(self):
        """Gets the s2i of this S2IPythonResponse.  # noqa: E501


        :return: The s2i of this S2IPythonResponse.  # noqa: E501
        :rtype: list[S2IPythonResponseS2i]
        """
        return self._s2i

    @s2i.setter
    def s2i(self, s2i):
        """Sets the s2i of this S2IPythonResponse.


        :param s2i: The s2i of this S2IPythonResponse.  # noqa: E501
        :type: list[S2IPythonResponseS2i]
        """
        if s2i is None:
            raise ValueError("Invalid value for `s2i`, must not be `None`")  # noqa: E501

        self._s2i = s2i

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
        if issubclass(S2IPythonResponse, dict):
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
        if not isinstance(other, S2IPythonResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
