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


class ImageMetadataResponse(object):
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
        'name': 'str',
        'tag': 'str',
        'digest': 'str',
        'repo_tags': 'list[str]',
        'created': 'str',
        'docker_version': 'str',
        'labels': 'object',
        'architecture': 'str',
        'os': 'str',
        'layers': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'tag': 'tag',
        'digest': 'digest',
        'repo_tags': 'repo_tags',
        'created': 'created',
        'docker_version': 'docker_version',
        'labels': 'labels',
        'architecture': 'architecture',
        'os': 'os',
        'layers': 'layers'
    }

    def __init__(self, name=None, tag=None, digest=None, repo_tags=None, created=None, docker_version=None, labels=None, architecture=None, os=None, layers=None):  # noqa: E501
        """ImageMetadataResponse - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._tag = None
        self._digest = None
        self._repo_tags = None
        self._created = None
        self._docker_version = None
        self._labels = None
        self._architecture = None
        self._os = None
        self._layers = None
        self.discriminator = None
        self.name = name
        if tag is not None:
            self.tag = tag
        self.digest = digest
        self.repo_tags = repo_tags
        self.created = created
        self.docker_version = docker_version
        self.labels = labels
        self.architecture = architecture
        self.os = os
        self.layers = layers

    @property
    def name(self):
        """Gets the name of this ImageMetadataResponse.  # noqa: E501

        Name of the image with optional tag.  # noqa: E501

        :return: The name of this ImageMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageMetadataResponse.

        Name of the image with optional tag.  # noqa: E501

        :param name: The name of this ImageMetadataResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tag(self):
        """Gets the tag of this ImageMetadataResponse.  # noqa: E501

        Tag of the image.  # noqa: E501

        :return: The tag of this ImageMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ImageMetadataResponse.

        Tag of the image.  # noqa: E501

        :param tag: The tag of this ImageMetadataResponse.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def digest(self):
        """Gets the digest of this ImageMetadataResponse.  # noqa: E501

        Digest of the image.  # noqa: E501

        :return: The digest of this ImageMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this ImageMetadataResponse.

        Digest of the image.  # noqa: E501

        :param digest: The digest of this ImageMetadataResponse.  # noqa: E501
        :type: str
        """
        if digest is None:
            raise ValueError("Invalid value for `digest`, must not be `None`")  # noqa: E501

        self._digest = digest

    @property
    def repo_tags(self):
        """Gets the repo_tags of this ImageMetadataResponse.  # noqa: E501


        :return: The repo_tags of this ImageMetadataResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._repo_tags

    @repo_tags.setter
    def repo_tags(self, repo_tags):
        """Sets the repo_tags of this ImageMetadataResponse.


        :param repo_tags: The repo_tags of this ImageMetadataResponse.  # noqa: E501
        :type: list[str]
        """
        if repo_tags is None:
            raise ValueError("Invalid value for `repo_tags`, must not be `None`")  # noqa: E501

        self._repo_tags = repo_tags

    @property
    def created(self):
        """Gets the created of this ImageMetadataResponse.  # noqa: E501

        Image creation date and time.  # noqa: E501

        :return: The created of this ImageMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ImageMetadataResponse.

        Image creation date and time.  # noqa: E501

        :param created: The created of this ImageMetadataResponse.  # noqa: E501
        :type: str
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def docker_version(self):
        """Gets the docker_version of this ImageMetadataResponse.  # noqa: E501

        Version of Docker.  # noqa: E501

        :return: The docker_version of this ImageMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._docker_version

    @docker_version.setter
    def docker_version(self, docker_version):
        """Sets the docker_version of this ImageMetadataResponse.

        Version of Docker.  # noqa: E501

        :param docker_version: The docker_version of this ImageMetadataResponse.  # noqa: E501
        :type: str
        """
        if docker_version is None:
            raise ValueError("Invalid value for `docker_version`, must not be `None`")  # noqa: E501

        self._docker_version = docker_version

    @property
    def labels(self):
        """Gets the labels of this ImageMetadataResponse.  # noqa: E501

        Image labels.  # noqa: E501

        :return: The labels of this ImageMetadataResponse.  # noqa: E501
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ImageMetadataResponse.

        Image labels.  # noqa: E501

        :param labels: The labels of this ImageMetadataResponse.  # noqa: E501
        :type: object
        """
        if labels is None:
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def architecture(self):
        """Gets the architecture of this ImageMetadataResponse.  # noqa: E501

        Target architecture of image.  # noqa: E501

        :return: The architecture of this ImageMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ImageMetadataResponse.

        Target architecture of image.  # noqa: E501

        :param architecture: The architecture of this ImageMetadataResponse.  # noqa: E501
        :type: str
        """
        if architecture is None:
            raise ValueError("Invalid value for `architecture`, must not be `None`")  # noqa: E501

        self._architecture = architecture

    @property
    def os(self):
        """Gets the os of this ImageMetadataResponse.  # noqa: E501

        Operating system identifier.  # noqa: E501

        :return: The os of this ImageMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this ImageMetadataResponse.

        Operating system identifier.  # noqa: E501

        :param os: The os of this ImageMetadataResponse.  # noqa: E501
        :type: str
        """
        if os is None:
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def layers(self):
        """Gets the layers of this ImageMetadataResponse.  # noqa: E501


        :return: The layers of this ImageMetadataResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this ImageMetadataResponse.


        :param layers: The layers of this ImageMetadataResponse.  # noqa: E501
        :type: list[str]
        """
        if layers is None:
            raise ValueError("Invalid value for `layers`, must not be `None`")  # noqa: E501

        self._layers = layers

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
        if issubclass(ImageMetadataResponse, dict):
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
        if not isinstance(other, ImageMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
