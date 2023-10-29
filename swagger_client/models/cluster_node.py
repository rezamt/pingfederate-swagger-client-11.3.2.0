# coding: utf-8

"""
    Administrative API Documentation

    The PingFederate Administrative API is a REST-based interface that provides a programmatic way to make configuration changes to PingFederate as an alternative to using the administrative console.<br/><br/>Expand the resources below to display implementation details on that resource such as the available endpoints, the parameter and response models for the operation, and the model structure of the resources themselves. Each resource operation comes with the ability to interact with the API. You are prompted for proper administration credentials when you try to perform an API operation.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ClusterNode(object):
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
        'address': 'str',
        'index': 'int',
        'mode': 'str',
        'node_group': 'str',
        'version': 'str',
        'node_tags': 'str',
        'configuration_timestamp': 'datetime',
        'replication_status': 'str'
    }

    attribute_map = {
        'address': 'address',
        'index': 'index',
        'mode': 'mode',
        'node_group': 'nodeGroup',
        'version': 'version',
        'node_tags': 'nodeTags',
        'configuration_timestamp': 'configurationTimestamp',
        'replication_status': 'replicationStatus'
    }

    def __init__(self, address=None, index=None, mode=None, node_group=None, version=None, node_tags=None, configuration_timestamp=None, replication_status=None, _configuration=None):  # noqa: E501
        """ClusterNode - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._index = None
        self._mode = None
        self._node_group = None
        self._version = None
        self._node_tags = None
        self._configuration_timestamp = None
        self._replication_status = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if index is not None:
            self.index = index
        if mode is not None:
            self.mode = mode
        if node_group is not None:
            self.node_group = node_group
        if version is not None:
            self.version = version
        if node_tags is not None:
            self.node_tags = node_tags
        if configuration_timestamp is not None:
            self.configuration_timestamp = configuration_timestamp
        if replication_status is not None:
            self.replication_status = replication_status

    @property
    def address(self):
        """Gets the address of this ClusterNode.  # noqa: E501

        The IP address and port this node is running on.  # noqa: E501

        :return: The address of this ClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ClusterNode.

        The IP address and port this node is running on.  # noqa: E501

        :param address: The address of this ClusterNode.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def index(self):
        """Gets the index of this ClusterNode.  # noqa: E501

        Index of the node within the cluster, or -1 if an index is not assigned.  # noqa: E501

        :return: The index of this ClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ClusterNode.

        Index of the node within the cluster, or -1 if an index is not assigned.  # noqa: E501

        :param index: The index of this ClusterNode.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def mode(self):
        """Gets the mode of this ClusterNode.  # noqa: E501

        The deployment mode of this node, from a clustering standpoint. CLUSTERED_DUAL is not supported.  # noqa: E501

        :return: The mode of this ClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ClusterNode.

        The deployment mode of this node, from a clustering standpoint. CLUSTERED_DUAL is not supported.  # noqa: E501

        :param mode: The mode of this ClusterNode.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLUSTERED_ENGINE", "CLUSTERED_CONSOLE", "CLUSTERED_DUAL", "STANDALONE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                mode not in allowed_values):
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def node_group(self):
        """Gets the node_group of this ClusterNode.  # noqa: E501

        The node group for this node. This field is only populated if adaptive clustering is enabled.  # noqa: E501

        :return: The node_group of this ClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._node_group

    @node_group.setter
    def node_group(self, node_group):
        """Sets the node_group of this ClusterNode.

        The node group for this node. This field is only populated if adaptive clustering is enabled.  # noqa: E501

        :param node_group: The node_group of this ClusterNode.  # noqa: E501
        :type: str
        """

        self._node_group = node_group

    @property
    def version(self):
        """Gets the version of this ClusterNode.  # noqa: E501

        The PingFederate version this node is running on.  # noqa: E501

        :return: The version of this ClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterNode.

        The PingFederate version this node is running on.  # noqa: E501

        :param version: The version of this ClusterNode.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def node_tags(self):
        """Gets the node_tags of this ClusterNode.  # noqa: E501

        The node tags for this node. This field is only populated for engine nodes.  # noqa: E501

        :return: The node_tags of this ClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._node_tags

    @node_tags.setter
    def node_tags(self, node_tags):
        """Sets the node_tags of this ClusterNode.

        The node tags for this node. This field is only populated for engine nodes.  # noqa: E501

        :param node_tags: The node_tags of this ClusterNode.  # noqa: E501
        :type: str
        """

        self._node_tags = node_tags

    @property
    def configuration_timestamp(self):
        """Gets the configuration_timestamp of this ClusterNode.  # noqa: E501

        The time stamp of the configuration data retrieved by this node.  # noqa: E501

        :return: The configuration_timestamp of this ClusterNode.  # noqa: E501
        :rtype: datetime
        """
        return self._configuration_timestamp

    @configuration_timestamp.setter
    def configuration_timestamp(self, configuration_timestamp):
        """Sets the configuration_timestamp of this ClusterNode.

        The time stamp of the configuration data retrieved by this node.  # noqa: E501

        :param configuration_timestamp: The configuration_timestamp of this ClusterNode.  # noqa: E501
        :type: datetime
        """

        self._configuration_timestamp = configuration_timestamp

    @property
    def replication_status(self):
        """Gets the replication_status of this ClusterNode.  # noqa: E501

        The replication status of the node.  # noqa: E501

        :return: The replication_status of this ClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._replication_status

    @replication_status.setter
    def replication_status(self, replication_status):
        """Sets the replication_status of this ClusterNode.

        The replication status of the node.  # noqa: E501

        :param replication_status: The replication_status of this ClusterNode.  # noqa: E501
        :type: str
        """
        allowed_values = ["RETRIEVING", "APPLYING", "FAILED", "SUCCEEDED", "OUT_OF_DATE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                replication_status not in allowed_values):
            raise ValueError(
                "Invalid value for `replication_status` ({0}), must be one of {1}"  # noqa: E501
                .format(replication_status, allowed_values)
            )

        self._replication_status = replication_status

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
        if issubclass(ClusterNode, dict):
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
        if not isinstance(other, ClusterNode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterNode):
            return True

        return self.to_dict() != other.to_dict()