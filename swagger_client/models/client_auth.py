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


class ClientAuth(object):
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
        'type': 'str',
        'secret': 'str',
        'encrypted_secret': 'str',
        'secondary_secrets': 'list[SecondarySecret]',
        'client_cert_issuer_dn': 'str',
        'client_cert_subject_dn': 'str',
        'enforce_replay_prevention': 'bool',
        'token_endpoint_auth_signing_algorithm': 'str'
    }

    attribute_map = {
        'type': 'type',
        'secret': 'secret',
        'encrypted_secret': 'encryptedSecret',
        'secondary_secrets': 'secondarySecrets',
        'client_cert_issuer_dn': 'clientCertIssuerDn',
        'client_cert_subject_dn': 'clientCertSubjectDn',
        'enforce_replay_prevention': 'enforceReplayPrevention',
        'token_endpoint_auth_signing_algorithm': 'tokenEndpointAuthSigningAlgorithm'
    }

    def __init__(self, type=None, secret=None, encrypted_secret=None, secondary_secrets=None, client_cert_issuer_dn=None, client_cert_subject_dn=None, enforce_replay_prevention=None, token_endpoint_auth_signing_algorithm=None, _configuration=None):  # noqa: E501
        """ClientAuth - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._secret = None
        self._encrypted_secret = None
        self._secondary_secrets = None
        self._client_cert_issuer_dn = None
        self._client_cert_subject_dn = None
        self._enforce_replay_prevention = None
        self._token_endpoint_auth_signing_algorithm = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if secret is not None:
            self.secret = secret
        if encrypted_secret is not None:
            self.encrypted_secret = encrypted_secret
        if secondary_secrets is not None:
            self.secondary_secrets = secondary_secrets
        if client_cert_issuer_dn is not None:
            self.client_cert_issuer_dn = client_cert_issuer_dn
        if client_cert_subject_dn is not None:
            self.client_cert_subject_dn = client_cert_subject_dn
        if enforce_replay_prevention is not None:
            self.enforce_replay_prevention = enforce_replay_prevention
        if token_endpoint_auth_signing_algorithm is not None:
            self.token_endpoint_auth_signing_algorithm = token_endpoint_auth_signing_algorithm

    @property
    def type(self):
        """Gets the type of this ClientAuth.  # noqa: E501

        Client authentication type.<br>The required field for type SECRET is secret.<br>The required fields for type CERTIFICATE are clientCertIssuerDn and clientCertSubjectDn.<br>The required field for type PRIVATE_KEY_JWT is: either jwks or jwksUrl.  # noqa: E501

        :return: The type of this ClientAuth.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClientAuth.

        Client authentication type.<br>The required field for type SECRET is secret.<br>The required fields for type CERTIFICATE are clientCertIssuerDn and clientCertSubjectDn.<br>The required field for type PRIVATE_KEY_JWT is: either jwks or jwksUrl.  # noqa: E501

        :param type: The type of this ClientAuth.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "SECRET", "CERTIFICATE", "PRIVATE_KEY_JWT", "CLIENT_SECRET_JWT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def secret(self):
        """Gets the secret of this ClientAuth.  # noqa: E501

        Client secret for Basic Authentication.  To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.  # noqa: E501

        :return: The secret of this ClientAuth.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this ClientAuth.

        Client secret for Basic Authentication.  To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.  # noqa: E501

        :param secret: The secret of this ClientAuth.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def encrypted_secret(self):
        """Gets the encrypted_secret of this ClientAuth.  # noqa: E501

        For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.  # noqa: E501

        :return: The encrypted_secret of this ClientAuth.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_secret

    @encrypted_secret.setter
    def encrypted_secret(self, encrypted_secret):
        """Sets the encrypted_secret of this ClientAuth.

        For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.  # noqa: E501

        :param encrypted_secret: The encrypted_secret of this ClientAuth.  # noqa: E501
        :type: str
        """

        self._encrypted_secret = encrypted_secret

    @property
    def secondary_secrets(self):
        """Gets the secondary_secrets of this ClientAuth.  # noqa: E501

        The list of secondary client secrets that are temporarily retained.  # noqa: E501

        :return: The secondary_secrets of this ClientAuth.  # noqa: E501
        :rtype: list[SecondarySecret]
        """
        return self._secondary_secrets

    @secondary_secrets.setter
    def secondary_secrets(self, secondary_secrets):
        """Sets the secondary_secrets of this ClientAuth.

        The list of secondary client secrets that are temporarily retained.  # noqa: E501

        :param secondary_secrets: The secondary_secrets of this ClientAuth.  # noqa: E501
        :type: list[SecondarySecret]
        """

        self._secondary_secrets = secondary_secrets

    @property
    def client_cert_issuer_dn(self):
        """Gets the client_cert_issuer_dn of this ClientAuth.  # noqa: E501

        Client TLS Certificate Issuer DN.  # noqa: E501

        :return: The client_cert_issuer_dn of this ClientAuth.  # noqa: E501
        :rtype: str
        """
        return self._client_cert_issuer_dn

    @client_cert_issuer_dn.setter
    def client_cert_issuer_dn(self, client_cert_issuer_dn):
        """Sets the client_cert_issuer_dn of this ClientAuth.

        Client TLS Certificate Issuer DN.  # noqa: E501

        :param client_cert_issuer_dn: The client_cert_issuer_dn of this ClientAuth.  # noqa: E501
        :type: str
        """

        self._client_cert_issuer_dn = client_cert_issuer_dn

    @property
    def client_cert_subject_dn(self):
        """Gets the client_cert_subject_dn of this ClientAuth.  # noqa: E501

        Client TLS Certificate Subject DN.  # noqa: E501

        :return: The client_cert_subject_dn of this ClientAuth.  # noqa: E501
        :rtype: str
        """
        return self._client_cert_subject_dn

    @client_cert_subject_dn.setter
    def client_cert_subject_dn(self, client_cert_subject_dn):
        """Sets the client_cert_subject_dn of this ClientAuth.

        Client TLS Certificate Subject DN.  # noqa: E501

        :param client_cert_subject_dn: The client_cert_subject_dn of this ClientAuth.  # noqa: E501
        :type: str
        """

        self._client_cert_subject_dn = client_cert_subject_dn

    @property
    def enforce_replay_prevention(self):
        """Gets the enforce_replay_prevention of this ClientAuth.  # noqa: E501

        Enforce replay prevention on JSON Web Tokens. This field is applicable only for Private Key JWT Client and Client Secret JWT Authentication.  # noqa: E501

        :return: The enforce_replay_prevention of this ClientAuth.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_replay_prevention

    @enforce_replay_prevention.setter
    def enforce_replay_prevention(self, enforce_replay_prevention):
        """Sets the enforce_replay_prevention of this ClientAuth.

        Enforce replay prevention on JSON Web Tokens. This field is applicable only for Private Key JWT Client and Client Secret JWT Authentication.  # noqa: E501

        :param enforce_replay_prevention: The enforce_replay_prevention of this ClientAuth.  # noqa: E501
        :type: bool
        """

        self._enforce_replay_prevention = enforce_replay_prevention

    @property
    def token_endpoint_auth_signing_algorithm(self):
        """Gets the token_endpoint_auth_signing_algorithm of this ClientAuth.  # noqa: E501

        The JSON Web Signature [JWS] algorithm that must be used to sign the JSON Web Tokens. This field is applicable only for Private Key JWT and Client Secret JWT Client Authentication. All asymmetric signing algorithms are allowed for Private Key JWT if value is not present.All symmetric signing algorithms are allowed for Client Secret JWT if value is not present <br>RS256 - RSA using SHA-256<br>RS384 - RSA using SHA-384<br>RS512 - RSA using SHA-512<br>ES256 - ECDSA using P256 Curve and SHA-256<br>ES384 - ECDSA using P384 Curve and SHA-384<br>ES512 - ECDSA using P521 Curve and SHA-512<br>PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256<br>PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384<br>PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512<br>RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11.<br>HS256 - HMAC using SHA-256<br>HS384 - HMAC using SHA-384<br>HS512 - HMAC using SHA-512.  # noqa: E501

        :return: The token_endpoint_auth_signing_algorithm of this ClientAuth.  # noqa: E501
        :rtype: str
        """
        return self._token_endpoint_auth_signing_algorithm

    @token_endpoint_auth_signing_algorithm.setter
    def token_endpoint_auth_signing_algorithm(self, token_endpoint_auth_signing_algorithm):
        """Sets the token_endpoint_auth_signing_algorithm of this ClientAuth.

        The JSON Web Signature [JWS] algorithm that must be used to sign the JSON Web Tokens. This field is applicable only for Private Key JWT and Client Secret JWT Client Authentication. All asymmetric signing algorithms are allowed for Private Key JWT if value is not present.All symmetric signing algorithms are allowed for Client Secret JWT if value is not present <br>RS256 - RSA using SHA-256<br>RS384 - RSA using SHA-384<br>RS512 - RSA using SHA-512<br>ES256 - ECDSA using P256 Curve and SHA-256<br>ES384 - ECDSA using P384 Curve and SHA-384<br>ES512 - ECDSA using P521 Curve and SHA-512<br>PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256<br>PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384<br>PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512<br>RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11.<br>HS256 - HMAC using SHA-256<br>HS384 - HMAC using SHA-384<br>HS512 - HMAC using SHA-512.  # noqa: E501

        :param token_endpoint_auth_signing_algorithm: The token_endpoint_auth_signing_algorithm of this ClientAuth.  # noqa: E501
        :type: str
        """
        allowed_values = ["RS256", "RS384", "RS512", "ES256", "ES384", "ES512", "PS256", "PS384", "PS512", "HS256", "HS384", "HS512"]  # noqa: E501
        if (self._configuration.client_side_validation and
                token_endpoint_auth_signing_algorithm not in allowed_values):
            raise ValueError(
                "Invalid value for `token_endpoint_auth_signing_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(token_endpoint_auth_signing_algorithm, allowed_values)
            )

        self._token_endpoint_auth_signing_algorithm = token_endpoint_auth_signing_algorithm

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
        if issubclass(ClientAuth, dict):
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
        if not isinstance(other, ClientAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientAuth):
            return True

        return self.to_dict() != other.to_dict()
