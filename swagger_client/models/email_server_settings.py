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


class EmailServerSettings(object):
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
        'source_addr': 'str',
        'email_server': 'str',
        'port': 'int',
        'ssl_port': 'int',
        'timeout': 'int',
        'retry_attempts': 'int',
        'retry_delay': 'int',
        'use_ssl': 'bool',
        'use_tls': 'bool',
        'verify_hostname': 'bool',
        'enable_utf8_message_headers': 'bool',
        'use_debugging': 'bool',
        'username': 'str',
        'password': 'str',
        'encrypted_password': 'str'
    }

    attribute_map = {
        'source_addr': 'sourceAddr',
        'email_server': 'emailServer',
        'port': 'port',
        'ssl_port': 'sslPort',
        'timeout': 'timeout',
        'retry_attempts': 'retryAttempts',
        'retry_delay': 'retryDelay',
        'use_ssl': 'useSSL',
        'use_tls': 'useTLS',
        'verify_hostname': 'verifyHostname',
        'enable_utf8_message_headers': 'enableUtf8MessageHeaders',
        'use_debugging': 'useDebugging',
        'username': 'username',
        'password': 'password',
        'encrypted_password': 'encryptedPassword'
    }

    def __init__(self, source_addr=None, email_server=None, port=None, ssl_port=None, timeout=None, retry_attempts=None, retry_delay=None, use_ssl=None, use_tls=None, verify_hostname=None, enable_utf8_message_headers=None, use_debugging=None, username=None, password=None, encrypted_password=None, _configuration=None):  # noqa: E501
        """EmailServerSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._source_addr = None
        self._email_server = None
        self._port = None
        self._ssl_port = None
        self._timeout = None
        self._retry_attempts = None
        self._retry_delay = None
        self._use_ssl = None
        self._use_tls = None
        self._verify_hostname = None
        self._enable_utf8_message_headers = None
        self._use_debugging = None
        self._username = None
        self._password = None
        self._encrypted_password = None
        self.discriminator = None

        self.source_addr = source_addr
        self.email_server = email_server
        self.port = port
        if ssl_port is not None:
            self.ssl_port = ssl_port
        if timeout is not None:
            self.timeout = timeout
        if retry_attempts is not None:
            self.retry_attempts = retry_attempts
        if retry_delay is not None:
            self.retry_delay = retry_delay
        if use_ssl is not None:
            self.use_ssl = use_ssl
        if use_tls is not None:
            self.use_tls = use_tls
        if verify_hostname is not None:
            self.verify_hostname = verify_hostname
        if enable_utf8_message_headers is not None:
            self.enable_utf8_message_headers = enable_utf8_message_headers
        if use_debugging is not None:
            self.use_debugging = use_debugging
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if encrypted_password is not None:
            self.encrypted_password = encrypted_password

    @property
    def source_addr(self):
        """Gets the source_addr of this EmailServerSettings.  # noqa: E501

        The email address that appears in the 'From' header line in email messages generated by PingFederate.  The address must be in valid format but need not be set up on your system.  # noqa: E501

        :return: The source_addr of this EmailServerSettings.  # noqa: E501
        :rtype: str
        """
        return self._source_addr

    @source_addr.setter
    def source_addr(self, source_addr):
        """Sets the source_addr of this EmailServerSettings.

        The email address that appears in the 'From' header line in email messages generated by PingFederate.  The address must be in valid format but need not be set up on your system.  # noqa: E501

        :param source_addr: The source_addr of this EmailServerSettings.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and source_addr is None:
            raise ValueError("Invalid value for `source_addr`, must not be `None`")  # noqa: E501

        self._source_addr = source_addr

    @property
    def email_server(self):
        """Gets the email_server of this EmailServerSettings.  # noqa: E501

        The IP address or hostname of your email server.  # noqa: E501

        :return: The email_server of this EmailServerSettings.  # noqa: E501
        :rtype: str
        """
        return self._email_server

    @email_server.setter
    def email_server(self, email_server):
        """Sets the email_server of this EmailServerSettings.

        The IP address or hostname of your email server.  # noqa: E501

        :param email_server: The email_server of this EmailServerSettings.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email_server is None:
            raise ValueError("Invalid value for `email_server`, must not be `None`")  # noqa: E501

        self._email_server = email_server

    @property
    def port(self):
        """Gets the port of this EmailServerSettings.  # noqa: E501

        The SMTP port on your email server. Allowable values: 1 - 65535. The default value is 25.  # noqa: E501

        :return: The port of this EmailServerSettings.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this EmailServerSettings.

        The SMTP port on your email server. Allowable values: 1 - 65535. The default value is 25.  # noqa: E501

        :param port: The port of this EmailServerSettings.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def ssl_port(self):
        """Gets the ssl_port of this EmailServerSettings.  # noqa: E501

        The secure SMTP port on your email server. This field is not active unless Use SSL is enabled. Allowable values: 1 - 65535. The default value is  465.  # noqa: E501

        :return: The ssl_port of this EmailServerSettings.  # noqa: E501
        :rtype: int
        """
        return self._ssl_port

    @ssl_port.setter
    def ssl_port(self, ssl_port):
        """Sets the ssl_port of this EmailServerSettings.

        The secure SMTP port on your email server. This field is not active unless Use SSL is enabled. Allowable values: 1 - 65535. The default value is  465.  # noqa: E501

        :param ssl_port: The ssl_port of this EmailServerSettings.  # noqa: E501
        :type: int
        """

        self._ssl_port = ssl_port

    @property
    def timeout(self):
        """Gets the timeout of this EmailServerSettings.  # noqa: E501

        The amount of time in seconds that PingFederate will wait before it times out connecting to the SMTP server. Allowable values: 0 - 3600. The default value is 30.  # noqa: E501

        :return: The timeout of this EmailServerSettings.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this EmailServerSettings.

        The amount of time in seconds that PingFederate will wait before it times out connecting to the SMTP server. Allowable values: 0 - 3600. The default value is 30.  # noqa: E501

        :param timeout: The timeout of this EmailServerSettings.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def retry_attempts(self):
        """Gets the retry_attempts of this EmailServerSettings.  # noqa: E501

        The number of times PingFederate tries to resend an email upon unsuccessful delivery. The default value is 2.  # noqa: E501

        :return: The retry_attempts of this EmailServerSettings.  # noqa: E501
        :rtype: int
        """
        return self._retry_attempts

    @retry_attempts.setter
    def retry_attempts(self, retry_attempts):
        """Sets the retry_attempts of this EmailServerSettings.

        The number of times PingFederate tries to resend an email upon unsuccessful delivery. The default value is 2.  # noqa: E501

        :param retry_attempts: The retry_attempts of this EmailServerSettings.  # noqa: E501
        :type: int
        """

        self._retry_attempts = retry_attempts

    @property
    def retry_delay(self):
        """Gets the retry_delay of this EmailServerSettings.  # noqa: E501

        The number of minutes PingFederate waits before the next retry attempt. The default value is 2.  # noqa: E501

        :return: The retry_delay of this EmailServerSettings.  # noqa: E501
        :rtype: int
        """
        return self._retry_delay

    @retry_delay.setter
    def retry_delay(self, retry_delay):
        """Sets the retry_delay of this EmailServerSettings.

        The number of minutes PingFederate waits before the next retry attempt. The default value is 2.  # noqa: E501

        :param retry_delay: The retry_delay of this EmailServerSettings.  # noqa: E501
        :type: int
        """

        self._retry_delay = retry_delay

    @property
    def use_ssl(self):
        """Gets the use_ssl of this EmailServerSettings.  # noqa: E501

        Requires the use of SSL/TLS on the port specified by 'sslPort'. If this option is enabled, it overrides the 'useTLS' option.  # noqa: E501

        :return: The use_ssl of this EmailServerSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this EmailServerSettings.

        Requires the use of SSL/TLS on the port specified by 'sslPort'. If this option is enabled, it overrides the 'useTLS' option.  # noqa: E501

        :param use_ssl: The use_ssl of this EmailServerSettings.  # noqa: E501
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def use_tls(self):
        """Gets the use_tls of this EmailServerSettings.  # noqa: E501

        Requires the use of the STARTTLS protocol on the port specified by 'port'.  # noqa: E501

        :return: The use_tls of this EmailServerSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_tls

    @use_tls.setter
    def use_tls(self, use_tls):
        """Sets the use_tls of this EmailServerSettings.

        Requires the use of the STARTTLS protocol on the port specified by 'port'.  # noqa: E501

        :param use_tls: The use_tls of this EmailServerSettings.  # noqa: E501
        :type: bool
        """

        self._use_tls = use_tls

    @property
    def verify_hostname(self):
        """Gets the verify_hostname of this EmailServerSettings.  # noqa: E501

        If useSSL or useTLS is enabled, this flag determines whether the email server hostname is verified against the server's SMTPS certificate.  # noqa: E501

        :return: The verify_hostname of this EmailServerSettings.  # noqa: E501
        :rtype: bool
        """
        return self._verify_hostname

    @verify_hostname.setter
    def verify_hostname(self, verify_hostname):
        """Sets the verify_hostname of this EmailServerSettings.

        If useSSL or useTLS is enabled, this flag determines whether the email server hostname is verified against the server's SMTPS certificate.  # noqa: E501

        :param verify_hostname: The verify_hostname of this EmailServerSettings.  # noqa: E501
        :type: bool
        """

        self._verify_hostname = verify_hostname

    @property
    def enable_utf8_message_headers(self):
        """Gets the enable_utf8_message_headers of this EmailServerSettings.  # noqa: E501

        Only set this flag to true if the email server supports UTF-8 characters in message headers. Otherwise, this is defaulted to false.  # noqa: E501

        :return: The enable_utf8_message_headers of this EmailServerSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_utf8_message_headers

    @enable_utf8_message_headers.setter
    def enable_utf8_message_headers(self, enable_utf8_message_headers):
        """Sets the enable_utf8_message_headers of this EmailServerSettings.

        Only set this flag to true if the email server supports UTF-8 characters in message headers. Otherwise, this is defaulted to false.  # noqa: E501

        :param enable_utf8_message_headers: The enable_utf8_message_headers of this EmailServerSettings.  # noqa: E501
        :type: bool
        """

        self._enable_utf8_message_headers = enable_utf8_message_headers

    @property
    def use_debugging(self):
        """Gets the use_debugging of this EmailServerSettings.  # noqa: E501

        Turns on detailed error messages for the PingFederate server log to help troubleshoot any problems.  # noqa: E501

        :return: The use_debugging of this EmailServerSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_debugging

    @use_debugging.setter
    def use_debugging(self, use_debugging):
        """Sets the use_debugging of this EmailServerSettings.

        Turns on detailed error messages for the PingFederate server log to help troubleshoot any problems.  # noqa: E501

        :param use_debugging: The use_debugging of this EmailServerSettings.  # noqa: E501
        :type: bool
        """

        self._use_debugging = use_debugging

    @property
    def username(self):
        """Gets the username of this EmailServerSettings.  # noqa: E501

        Authorized email username. Required if the password is provided.  # noqa: E501

        :return: The username of this EmailServerSettings.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this EmailServerSettings.

        Authorized email username. Required if the password is provided.  # noqa: E501

        :param username: The username of this EmailServerSettings.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this EmailServerSettings.  # noqa: E501

        User password.  To update the password, specify the plaintext value in this field.  This field will not be populated for GET requests.  # noqa: E501

        :return: The password of this EmailServerSettings.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this EmailServerSettings.

        User password.  To update the password, specify the plaintext value in this field.  This field will not be populated for GET requests.  # noqa: E501

        :param password: The password of this EmailServerSettings.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def encrypted_password(self):
        """Gets the encrypted_password of this EmailServerSettings.  # noqa: E501

        For GET requests, this field contains the encrypted password, if one exists.  For POST and PUT requests, if you wish to reuse the existing password, this field should be passed back unchanged.  # noqa: E501

        :return: The encrypted_password of this EmailServerSettings.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_password

    @encrypted_password.setter
    def encrypted_password(self, encrypted_password):
        """Sets the encrypted_password of this EmailServerSettings.

        For GET requests, this field contains the encrypted password, if one exists.  For POST and PUT requests, if you wish to reuse the existing password, this field should be passed back unchanged.  # noqa: E501

        :param encrypted_password: The encrypted_password of this EmailServerSettings.  # noqa: E501
        :type: str
        """

        self._encrypted_password = encrypted_password

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
        if issubclass(EmailServerSettings, dict):
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
        if not isinstance(other, EmailServerSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailServerSettings):
            return True

        return self.to_dict() != other.to_dict()
