# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.6.0-dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from thamos.swagger_client.configuration import Configuration


class AnalysisResultResponseMetadataDistributionVersionParts(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"build_number": "str", "major": "str", "minor": "str"}

    attribute_map = {"build_number": "build_number", "major": "major", "minor": "minor"}

    def __init__(
        self, build_number=None, major=None, minor=None, local_vars_configuration=None
    ):  # noqa: E501
        """AnalysisResultResponseMetadataDistributionVersionParts - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._build_number = None
        self._major = None
        self._minor = None
        self.discriminator = None

        self.build_number = build_number
        self.major = major
        self.minor = minor

    @property
    def build_number(self):
        """Gets the build_number of this AnalysisResultResponseMetadataDistributionVersionParts.  # noqa: E501


        :return: The build_number of this AnalysisResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this AnalysisResultResponseMetadataDistributionVersionParts.


        :param build_number: The build_number of this AnalysisResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and build_number is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `build_number`, must not be `None`"
            )  # noqa: E501

        self._build_number = build_number

    @property
    def major(self):
        """Gets the major of this AnalysisResultResponseMetadataDistributionVersionParts.  # noqa: E501


        :return: The major of this AnalysisResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :rtype: str
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this AnalysisResultResponseMetadataDistributionVersionParts.


        :param major: The major of this AnalysisResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and major is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `major`, must not be `None`"
            )  # noqa: E501

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this AnalysisResultResponseMetadataDistributionVersionParts.  # noqa: E501


        :return: The minor of this AnalysisResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :rtype: str
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this AnalysisResultResponseMetadataDistributionVersionParts.


        :param minor: The minor of this AnalysisResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and minor is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `minor`, must not be `None`"
            )  # noqa: E501

        self._minor = minor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(
            other, AnalysisResultResponseMetadataDistributionVersionParts
        ):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(
            other, AnalysisResultResponseMetadataDistributionVersionParts
        ):
            return True

        return self.to_dict() != other.to_dict()
