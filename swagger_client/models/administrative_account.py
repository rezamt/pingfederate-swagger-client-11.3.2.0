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


class AdministrativeAccount(object):
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
        'username': 'str',
        'password': 'str',
        'encrypted_password': 'str',
        'active': 'bool',
        'description': 'str',
        'auditor': 'bool',
        'phone_number': 'str',
        'email_address': 'str',
        'department': 'str',
        'roles': 'list[str]'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'encrypted_password': 'encryptedPassword',
        'active': 'active',
        'description': 'description',
        'auditor': 'auditor',
        'phone_number': 'phoneNumber',
        'email_address': 'emailAddress',
        'department': 'department',
        'roles': 'roles'
    }

    def __init__(self, username=None, password=None, encrypted_password=None, active=None, description=None, auditor=None, phone_number=None, email_address=None, department=None, roles=None, _configuration=None):  # noqa: E501
        """AdministrativeAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._username = None
        self._password = None
        self._encrypted_password = None
        self._active = None
        self._description = None
        self._auditor = None
        self._phone_number = None
        self._email_address = None
        self._department = None
        self._roles = None
        self.discriminator = None

        self.username = username
        if password is not None:
            self.password = password
        if encrypted_password is not None:
            self.encrypted_password = encrypted_password
        if active is not None:
            self.active = active
        if description is not None:
            self.description = description
        if auditor is not None:
            self.auditor = auditor
        if phone_number is not None:
            self.phone_number = phone_number
        if email_address is not None:
            self.email_address = email_address
        if department is not None:
            self.department = department
        if roles is not None:
            self.roles = roles

    @property
    def username(self):
        """Gets the username of this AdministrativeAccount.  # noqa: E501

        Username for the Administrative Account.  # noqa: E501

        :return: The username of this AdministrativeAccount.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AdministrativeAccount.

        Username for the Administrative Account.  # noqa: E501

        :param username: The username of this AdministrativeAccount.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this AdministrativeAccount.  # noqa: E501

        Password for the Account. This field is only applicable during a POST operation.  # noqa: E501

        :return: The password of this AdministrativeAccount.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AdministrativeAccount.

        Password for the Account. This field is only applicable during a POST operation.  # noqa: E501

        :param password: The password of this AdministrativeAccount.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def encrypted_password(self):
        """Gets the encrypted_password of this AdministrativeAccount.  # noqa: E501

        For GET requests, this field contains the encrypted account password. For POST and PUT requests, if you wish to re-use the password from an API response to this endpoint, this field should be passed back unchanged.  # noqa: E501

        :return: The encrypted_password of this AdministrativeAccount.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_password

    @encrypted_password.setter
    def encrypted_password(self, encrypted_password):
        """Sets the encrypted_password of this AdministrativeAccount.

        For GET requests, this field contains the encrypted account password. For POST and PUT requests, if you wish to re-use the password from an API response to this endpoint, this field should be passed back unchanged.  # noqa: E501

        :param encrypted_password: The encrypted_password of this AdministrativeAccount.  # noqa: E501
        :type: str
        """

        self._encrypted_password = encrypted_password

    @property
    def active(self):
        """Gets the active of this AdministrativeAccount.  # noqa: E501

        Indicates whether the account is active or not.  # noqa: E501

        :return: The active of this AdministrativeAccount.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AdministrativeAccount.

        Indicates whether the account is active or not.  # noqa: E501

        :param active: The active of this AdministrativeAccount.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def description(self):
        """Gets the description of this AdministrativeAccount.  # noqa: E501

        Description of the account.  # noqa: E501

        :return: The description of this AdministrativeAccount.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AdministrativeAccount.

        Description of the account.  # noqa: E501

        :param description: The description of this AdministrativeAccount.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def auditor(self):
        """Gets the auditor of this AdministrativeAccount.  # noqa: E501

        Indicates whether the account belongs to an Auditor. An Auditor has View-only permissions for all administrative functions. An Auditor cannot have any administrative roles.  # noqa: E501

        :return: The auditor of this AdministrativeAccount.  # noqa: E501
        :rtype: bool
        """
        return self._auditor

    @auditor.setter
    def auditor(self, auditor):
        """Sets the auditor of this AdministrativeAccount.

        Indicates whether the account belongs to an Auditor. An Auditor has View-only permissions for all administrative functions. An Auditor cannot have any administrative roles.  # noqa: E501

        :param auditor: The auditor of this AdministrativeAccount.  # noqa: E501
        :type: bool
        """

        self._auditor = auditor

    @property
    def phone_number(self):
        """Gets the phone_number of this AdministrativeAccount.  # noqa: E501

        Phone number associated with the account.  # noqa: E501

        :return: The phone_number of this AdministrativeAccount.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this AdministrativeAccount.

        Phone number associated with the account.  # noqa: E501

        :param phone_number: The phone_number of this AdministrativeAccount.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def email_address(self):
        """Gets the email_address of this AdministrativeAccount.  # noqa: E501

        Email address associated with the account.  # noqa: E501

        :return: The email_address of this AdministrativeAccount.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this AdministrativeAccount.

        Email address associated with the account.  # noqa: E501

        :param email_address: The email_address of this AdministrativeAccount.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def department(self):
        """Gets the department of this AdministrativeAccount.  # noqa: E501

        The Department name of account user.  # noqa: E501

        :return: The department of this AdministrativeAccount.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this AdministrativeAccount.

        The Department name of account user.  # noqa: E501

        :param department: The department of this AdministrativeAccount.  # noqa: E501
        :type: str
        """

        self._department = department

    @property
    def roles(self):
        """Gets the roles of this AdministrativeAccount.  # noqa: E501

        Roles available for an administrator. <br>USER_ADMINISTRATOR - Can create, deactivate or delete accounts and reset passwords. Additionally, install replacement license keys. <br> CRYPTO_ADMINISTRATOR - Can manage local keys and certificates. <br> ADMINISTRATOR - Can configure partner connections and most system settings (except the management of native accounts and the handling of local keys and certificates. <br>EXPRESSION_ADMINISTRATOR - Can add and update OGNL expressions. <br>  # noqa: E501

        :return: The roles of this AdministrativeAccount.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AdministrativeAccount.

        Roles available for an administrator. <br>USER_ADMINISTRATOR - Can create, deactivate or delete accounts and reset passwords. Additionally, install replacement license keys. <br> CRYPTO_ADMINISTRATOR - Can manage local keys and certificates. <br> ADMINISTRATOR - Can configure partner connections and most system settings (except the management of native accounts and the handling of local keys and certificates. <br>EXPRESSION_ADMINISTRATOR - Can add and update OGNL expressions. <br>  # noqa: E501

        :param roles: The roles of this AdministrativeAccount.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["USER_ADMINISTRATOR", "CRYPTO_ADMINISTRATOR", "ADMINISTRATOR", "EXPRESSION_ADMINISTRATOR"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(roles).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `roles` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles = roles

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
        if issubclass(AdministrativeAccount, dict):
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
        if not isinstance(other, AdministrativeAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdministrativeAccount):
            return True

        return self.to_dict() != other.to_dict()
