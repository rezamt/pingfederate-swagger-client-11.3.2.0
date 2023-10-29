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


class JdbcDataStore(object):
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
        'connection_url_tags': 'list[JdbcTagConfig]',
        'connection_url': 'str',
        'name': 'str',
        'driver_class': 'str',
        'user_name': 'str',
        'password': 'str',
        'encrypted_password': 'str',
        'validate_connection_sql': 'str',
        'allow_multi_value_attributes': 'bool',
        'min_pool_size': 'int',
        'max_pool_size': 'int',
        'blocking_timeout': 'int',
        'idle_timeout': 'int'
    }

    attribute_map = {
        'connection_url_tags': 'connectionUrlTags',
        'connection_url': 'connectionUrl',
        'name': 'name',
        'driver_class': 'driverClass',
        'user_name': 'userName',
        'password': 'password',
        'encrypted_password': 'encryptedPassword',
        'validate_connection_sql': 'validateConnectionSql',
        'allow_multi_value_attributes': 'allowMultiValueAttributes',
        'min_pool_size': 'minPoolSize',
        'max_pool_size': 'maxPoolSize',
        'blocking_timeout': 'blockingTimeout',
        'idle_timeout': 'idleTimeout'
    }

    def __init__(self, connection_url_tags=None, connection_url=None, name=None, driver_class=None, user_name=None, password=None, encrypted_password=None, validate_connection_sql=None, allow_multi_value_attributes=None, min_pool_size=None, max_pool_size=None, blocking_timeout=None, idle_timeout=None, _configuration=None):  # noqa: E501
        """JdbcDataStore - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connection_url_tags = None
        self._connection_url = None
        self._name = None
        self._driver_class = None
        self._user_name = None
        self._password = None
        self._encrypted_password = None
        self._validate_connection_sql = None
        self._allow_multi_value_attributes = None
        self._min_pool_size = None
        self._max_pool_size = None
        self._blocking_timeout = None
        self._idle_timeout = None
        self.discriminator = None

        if connection_url_tags is not None:
            self.connection_url_tags = connection_url_tags
        if connection_url is not None:
            self.connection_url = connection_url
        if name is not None:
            self.name = name
        self.driver_class = driver_class
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
        if encrypted_password is not None:
            self.encrypted_password = encrypted_password
        if validate_connection_sql is not None:
            self.validate_connection_sql = validate_connection_sql
        if allow_multi_value_attributes is not None:
            self.allow_multi_value_attributes = allow_multi_value_attributes
        if min_pool_size is not None:
            self.min_pool_size = min_pool_size
        if max_pool_size is not None:
            self.max_pool_size = max_pool_size
        if blocking_timeout is not None:
            self.blocking_timeout = blocking_timeout
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout

    @property
    def connection_url_tags(self):
        """Gets the connection_url_tags of this JdbcDataStore.  # noqa: E501

        The set of connection URLs and associated tags for this JDBC data store. This is required if 'connectionUrl' is not provided.  # noqa: E501

        :return: The connection_url_tags of this JdbcDataStore.  # noqa: E501
        :rtype: list[JdbcTagConfig]
        """
        return self._connection_url_tags

    @connection_url_tags.setter
    def connection_url_tags(self, connection_url_tags):
        """Sets the connection_url_tags of this JdbcDataStore.

        The set of connection URLs and associated tags for this JDBC data store. This is required if 'connectionUrl' is not provided.  # noqa: E501

        :param connection_url_tags: The connection_url_tags of this JdbcDataStore.  # noqa: E501
        :type: list[JdbcTagConfig]
        """

        self._connection_url_tags = connection_url_tags

    @property
    def connection_url(self):
        """Gets the connection_url of this JdbcDataStore.  # noqa: E501

        The default location of the JDBC database. This field is required if no mapping for JDBC database location and tags is specified.  # noqa: E501

        :return: The connection_url of this JdbcDataStore.  # noqa: E501
        :rtype: str
        """
        return self._connection_url

    @connection_url.setter
    def connection_url(self, connection_url):
        """Sets the connection_url of this JdbcDataStore.

        The default location of the JDBC database. This field is required if no mapping for JDBC database location and tags is specified.  # noqa: E501

        :param connection_url: The connection_url of this JdbcDataStore.  # noqa: E501
        :type: str
        """

        self._connection_url = connection_url

    @property
    def name(self):
        """Gets the name of this JdbcDataStore.  # noqa: E501

        The data store name with a unique value across all data sources. Omitting this attribute will set the value to a combination of the connection url and the username.  # noqa: E501

        :return: The name of this JdbcDataStore.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JdbcDataStore.

        The data store name with a unique value across all data sources. Omitting this attribute will set the value to a combination of the connection url and the username.  # noqa: E501

        :param name: The name of this JdbcDataStore.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def driver_class(self):
        """Gets the driver_class of this JdbcDataStore.  # noqa: E501

        The name of the driver class used to communicate with the source database.  # noqa: E501

        :return: The driver_class of this JdbcDataStore.  # noqa: E501
        :rtype: str
        """
        return self._driver_class

    @driver_class.setter
    def driver_class(self, driver_class):
        """Sets the driver_class of this JdbcDataStore.

        The name of the driver class used to communicate with the source database.  # noqa: E501

        :param driver_class: The driver_class of this JdbcDataStore.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and driver_class is None:
            raise ValueError("Invalid value for `driver_class`, must not be `None`")  # noqa: E501

        self._driver_class = driver_class

    @property
    def user_name(self):
        """Gets the user_name of this JdbcDataStore.  # noqa: E501

        The name that identifies the user when connecting to the database.  # noqa: E501

        :return: The user_name of this JdbcDataStore.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this JdbcDataStore.

        The name that identifies the user when connecting to the database.  # noqa: E501

        :param user_name: The user_name of this JdbcDataStore.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this JdbcDataStore.  # noqa: E501

        The password needed to access the database. GETs will not return this attribute. To update this field, specify the new value in this attribute.  # noqa: E501

        :return: The password of this JdbcDataStore.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this JdbcDataStore.

        The password needed to access the database. GETs will not return this attribute. To update this field, specify the new value in this attribute.  # noqa: E501

        :param password: The password of this JdbcDataStore.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def encrypted_password(self):
        """Gets the encrypted_password of this JdbcDataStore.  # noqa: E501

        The encrypted password needed to access the database. If you do not want to update the stored value, this attribute should be passed back unchanged. Secret Reference may be provided in this field with format 'OBF:MGR:{secretManagerId}:{secretId}'.  # noqa: E501

        :return: The encrypted_password of this JdbcDataStore.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_password

    @encrypted_password.setter
    def encrypted_password(self, encrypted_password):
        """Sets the encrypted_password of this JdbcDataStore.

        The encrypted password needed to access the database. If you do not want to update the stored value, this attribute should be passed back unchanged. Secret Reference may be provided in this field with format 'OBF:MGR:{secretManagerId}:{secretId}'.  # noqa: E501

        :param encrypted_password: The encrypted_password of this JdbcDataStore.  # noqa: E501
        :type: str
        """

        self._encrypted_password = encrypted_password

    @property
    def validate_connection_sql(self):
        """Gets the validate_connection_sql of this JdbcDataStore.  # noqa: E501

        A simple SQL statement used by PingFederate at runtime to verify that the database connection is still active and to reconnect if needed.  # noqa: E501

        :return: The validate_connection_sql of this JdbcDataStore.  # noqa: E501
        :rtype: str
        """
        return self._validate_connection_sql

    @validate_connection_sql.setter
    def validate_connection_sql(self, validate_connection_sql):
        """Sets the validate_connection_sql of this JdbcDataStore.

        A simple SQL statement used by PingFederate at runtime to verify that the database connection is still active and to reconnect if needed.  # noqa: E501

        :param validate_connection_sql: The validate_connection_sql of this JdbcDataStore.  # noqa: E501
        :type: str
        """

        self._validate_connection_sql = validate_connection_sql

    @property
    def allow_multi_value_attributes(self):
        """Gets the allow_multi_value_attributes of this JdbcDataStore.  # noqa: E501

        Indicates that this data store can select more than one record from a column and return the results as a multi-value attribute.  # noqa: E501

        :return: The allow_multi_value_attributes of this JdbcDataStore.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multi_value_attributes

    @allow_multi_value_attributes.setter
    def allow_multi_value_attributes(self, allow_multi_value_attributes):
        """Sets the allow_multi_value_attributes of this JdbcDataStore.

        Indicates that this data store can select more than one record from a column and return the results as a multi-value attribute.  # noqa: E501

        :param allow_multi_value_attributes: The allow_multi_value_attributes of this JdbcDataStore.  # noqa: E501
        :type: bool
        """

        self._allow_multi_value_attributes = allow_multi_value_attributes

    @property
    def min_pool_size(self):
        """Gets the min_pool_size of this JdbcDataStore.  # noqa: E501

        The smallest number of database connections in the connection pool for the given data store. Omitting this attribute will set the value to the connection pool default.  # noqa: E501

        :return: The min_pool_size of this JdbcDataStore.  # noqa: E501
        :rtype: int
        """
        return self._min_pool_size

    @min_pool_size.setter
    def min_pool_size(self, min_pool_size):
        """Sets the min_pool_size of this JdbcDataStore.

        The smallest number of database connections in the connection pool for the given data store. Omitting this attribute will set the value to the connection pool default.  # noqa: E501

        :param min_pool_size: The min_pool_size of this JdbcDataStore.  # noqa: E501
        :type: int
        """

        self._min_pool_size = min_pool_size

    @property
    def max_pool_size(self):
        """Gets the max_pool_size of this JdbcDataStore.  # noqa: E501

        The largest number of database connections in the connection pool for the given data store. Omitting this attribute will set the value to the connection pool default.  # noqa: E501

        :return: The max_pool_size of this JdbcDataStore.  # noqa: E501
        :rtype: int
        """
        return self._max_pool_size

    @max_pool_size.setter
    def max_pool_size(self, max_pool_size):
        """Sets the max_pool_size of this JdbcDataStore.

        The largest number of database connections in the connection pool for the given data store. Omitting this attribute will set the value to the connection pool default.  # noqa: E501

        :param max_pool_size: The max_pool_size of this JdbcDataStore.  # noqa: E501
        :type: int
        """

        self._max_pool_size = max_pool_size

    @property
    def blocking_timeout(self):
        """Gets the blocking_timeout of this JdbcDataStore.  # noqa: E501

        The amount of time in milliseconds a request waits to get a connection from the connection pool before it fails. Omitting this attribute will set the value to the connection pool default.  # noqa: E501

        :return: The blocking_timeout of this JdbcDataStore.  # noqa: E501
        :rtype: int
        """
        return self._blocking_timeout

    @blocking_timeout.setter
    def blocking_timeout(self, blocking_timeout):
        """Sets the blocking_timeout of this JdbcDataStore.

        The amount of time in milliseconds a request waits to get a connection from the connection pool before it fails. Omitting this attribute will set the value to the connection pool default.  # noqa: E501

        :param blocking_timeout: The blocking_timeout of this JdbcDataStore.  # noqa: E501
        :type: int
        """

        self._blocking_timeout = blocking_timeout

    @property
    def idle_timeout(self):
        """Gets the idle_timeout of this JdbcDataStore.  # noqa: E501

        The length of time in minutes the connection can be idle in the pool before it is closed. Omitting this attribute will set the value to the connection pool default.  # noqa: E501

        :return: The idle_timeout of this JdbcDataStore.  # noqa: E501
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """Sets the idle_timeout of this JdbcDataStore.

        The length of time in minutes the connection can be idle in the pool before it is closed. Omitting this attribute will set the value to the connection pool default.  # noqa: E501

        :param idle_timeout: The idle_timeout of this JdbcDataStore.  # noqa: E501
        :type: int
        """

        self._idle_timeout = idle_timeout

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
        if issubclass(JdbcDataStore, dict):
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
        if not isinstance(other, JdbcDataStore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JdbcDataStore):
            return True

        return self.to_dict() != other.to_dict()