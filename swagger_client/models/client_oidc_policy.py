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


class ClientOIDCPolicy(object):
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
        'id_token_signing_algorithm': 'str',
        'id_token_encryption_algorithm': 'str',
        'id_token_content_encryption_algorithm': 'str',
        'policy_group': 'ResourceLink',
        'grant_access_session_revocation_api': 'bool',
        'grant_access_session_session_management_api': 'bool',
        'logout_mode': 'str',
        'ping_access_logout_capable': 'bool',
        'logout_uris': 'list[str]',
        'back_channel_logout_uri': 'str',
        'pairwise_identifier_user_type': 'bool',
        'sector_identifier_uri': 'str'
    }

    attribute_map = {
        'id_token_signing_algorithm': 'idTokenSigningAlgorithm',
        'id_token_encryption_algorithm': 'idTokenEncryptionAlgorithm',
        'id_token_content_encryption_algorithm': 'idTokenContentEncryptionAlgorithm',
        'policy_group': 'policyGroup',
        'grant_access_session_revocation_api': 'grantAccessSessionRevocationApi',
        'grant_access_session_session_management_api': 'grantAccessSessionSessionManagementApi',
        'logout_mode': 'logoutMode',
        'ping_access_logout_capable': 'pingAccessLogoutCapable',
        'logout_uris': 'logoutUris',
        'back_channel_logout_uri': 'backChannelLogoutUri',
        'pairwise_identifier_user_type': 'pairwiseIdentifierUserType',
        'sector_identifier_uri': 'sectorIdentifierUri'
    }

    def __init__(self, id_token_signing_algorithm=None, id_token_encryption_algorithm=None, id_token_content_encryption_algorithm=None, policy_group=None, grant_access_session_revocation_api=None, grant_access_session_session_management_api=None, logout_mode=None, ping_access_logout_capable=None, logout_uris=None, back_channel_logout_uri=None, pairwise_identifier_user_type=None, sector_identifier_uri=None, _configuration=None):  # noqa: E501
        """ClientOIDCPolicy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id_token_signing_algorithm = None
        self._id_token_encryption_algorithm = None
        self._id_token_content_encryption_algorithm = None
        self._policy_group = None
        self._grant_access_session_revocation_api = None
        self._grant_access_session_session_management_api = None
        self._logout_mode = None
        self._ping_access_logout_capable = None
        self._logout_uris = None
        self._back_channel_logout_uri = None
        self._pairwise_identifier_user_type = None
        self._sector_identifier_uri = None
        self.discriminator = None

        if id_token_signing_algorithm is not None:
            self.id_token_signing_algorithm = id_token_signing_algorithm
        if id_token_encryption_algorithm is not None:
            self.id_token_encryption_algorithm = id_token_encryption_algorithm
        if id_token_content_encryption_algorithm is not None:
            self.id_token_content_encryption_algorithm = id_token_content_encryption_algorithm
        if policy_group is not None:
            self.policy_group = policy_group
        if grant_access_session_revocation_api is not None:
            self.grant_access_session_revocation_api = grant_access_session_revocation_api
        if grant_access_session_session_management_api is not None:
            self.grant_access_session_session_management_api = grant_access_session_session_management_api
        if logout_mode is not None:
            self.logout_mode = logout_mode
        if ping_access_logout_capable is not None:
            self.ping_access_logout_capable = ping_access_logout_capable
        if logout_uris is not None:
            self.logout_uris = logout_uris
        if back_channel_logout_uri is not None:
            self.back_channel_logout_uri = back_channel_logout_uri
        if pairwise_identifier_user_type is not None:
            self.pairwise_identifier_user_type = pairwise_identifier_user_type
        if sector_identifier_uri is not None:
            self.sector_identifier_uri = sector_identifier_uri

    @property
    def id_token_signing_algorithm(self):
        """Gets the id_token_signing_algorithm of this ClientOIDCPolicy.  # noqa: E501

        The JSON Web Signature [JWS] algorithm required for the ID Token.<br>NONE - No signing algorithm<br>HS256 - HMAC using SHA-256<br>HS384 - HMAC using SHA-384<br>HS512 - HMAC using SHA-512<br>RS256 - RSA using SHA-256<br>RS384 - RSA using SHA-384<br>RS512 - RSA using SHA-512<br>ES256 - ECDSA using P256 Curve and SHA-256<br>ES384 - ECDSA using P384 Curve and SHA-384<br>ES512 - ECDSA using P521 Curve and SHA-512<br>PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256<br>PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384<br>PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512<br>A null value will represent the default algorithm which is RS256.<br>RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11  # noqa: E501

        :return: The id_token_signing_algorithm of this ClientOIDCPolicy.  # noqa: E501
        :rtype: str
        """
        return self._id_token_signing_algorithm

    @id_token_signing_algorithm.setter
    def id_token_signing_algorithm(self, id_token_signing_algorithm):
        """Sets the id_token_signing_algorithm of this ClientOIDCPolicy.

        The JSON Web Signature [JWS] algorithm required for the ID Token.<br>NONE - No signing algorithm<br>HS256 - HMAC using SHA-256<br>HS384 - HMAC using SHA-384<br>HS512 - HMAC using SHA-512<br>RS256 - RSA using SHA-256<br>RS384 - RSA using SHA-384<br>RS512 - RSA using SHA-512<br>ES256 - ECDSA using P256 Curve and SHA-256<br>ES384 - ECDSA using P384 Curve and SHA-384<br>ES512 - ECDSA using P521 Curve and SHA-512<br>PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256<br>PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384<br>PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512<br>A null value will represent the default algorithm which is RS256.<br>RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11  # noqa: E501

        :param id_token_signing_algorithm: The id_token_signing_algorithm of this ClientOIDCPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "HS256", "HS384", "HS512", "RS256", "RS384", "RS512", "ES256", "ES384", "ES512", "PS256", "PS384", "PS512"]  # noqa: E501
        if (self._configuration.client_side_validation and
                id_token_signing_algorithm not in allowed_values):
            raise ValueError(
                "Invalid value for `id_token_signing_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(id_token_signing_algorithm, allowed_values)
            )

        self._id_token_signing_algorithm = id_token_signing_algorithm

    @property
    def id_token_encryption_algorithm(self):
        """Gets the id_token_encryption_algorithm of this ClientOIDCPolicy.  # noqa: E501

        The JSON Web Encryption [JWE] encryption algorithm used to encrypt the content encryption key for the ID Token.<br>DIR - Direct Encryption with symmetric key<br>A128KW - AES-128 Key Wrap<br>A192KW - AES-192 Key Wrap<br>A256KW - AES-256 Key Wrap<br>A128GCMKW - AES-GCM-128 key encryption<br>A192GCMKW - AES-GCM-192 key encryption<br>A256GCMKW - AES-GCM-256 key encryption<br>ECDH_ES - ECDH-ES<br>ECDH_ES_A128KW - ECDH-ES with AES-128 Key Wrap<br>ECDH_ES_A192KW - ECDH-ES with AES-192 Key Wrap<br>ECDH_ES_A256KW - ECDH-ES with AES-256 Key Wrap<br>RSA_OAEP - RSAES OAEP<br>RSA_OAEP_256 - RSAES OAEP using SHA-256 and MGF1 with SHA-256  # noqa: E501

        :return: The id_token_encryption_algorithm of this ClientOIDCPolicy.  # noqa: E501
        :rtype: str
        """
        return self._id_token_encryption_algorithm

    @id_token_encryption_algorithm.setter
    def id_token_encryption_algorithm(self, id_token_encryption_algorithm):
        """Sets the id_token_encryption_algorithm of this ClientOIDCPolicy.

        The JSON Web Encryption [JWE] encryption algorithm used to encrypt the content encryption key for the ID Token.<br>DIR - Direct Encryption with symmetric key<br>A128KW - AES-128 Key Wrap<br>A192KW - AES-192 Key Wrap<br>A256KW - AES-256 Key Wrap<br>A128GCMKW - AES-GCM-128 key encryption<br>A192GCMKW - AES-GCM-192 key encryption<br>A256GCMKW - AES-GCM-256 key encryption<br>ECDH_ES - ECDH-ES<br>ECDH_ES_A128KW - ECDH-ES with AES-128 Key Wrap<br>ECDH_ES_A192KW - ECDH-ES with AES-192 Key Wrap<br>ECDH_ES_A256KW - ECDH-ES with AES-256 Key Wrap<br>RSA_OAEP - RSAES OAEP<br>RSA_OAEP_256 - RSAES OAEP using SHA-256 and MGF1 with SHA-256  # noqa: E501

        :param id_token_encryption_algorithm: The id_token_encryption_algorithm of this ClientOIDCPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["DIR", "A128KW", "A192KW", "A256KW", "A128GCMKW", "A192GCMKW", "A256GCMKW", "ECDH_ES", "ECDH_ES_A128KW", "ECDH_ES_A192KW", "ECDH_ES_A256KW", "RSA_OAEP", "RSA_OAEP_256"]  # noqa: E501
        if (self._configuration.client_side_validation and
                id_token_encryption_algorithm not in allowed_values):
            raise ValueError(
                "Invalid value for `id_token_encryption_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(id_token_encryption_algorithm, allowed_values)
            )

        self._id_token_encryption_algorithm = id_token_encryption_algorithm

    @property
    def id_token_content_encryption_algorithm(self):
        """Gets the id_token_content_encryption_algorithm of this ClientOIDCPolicy.  # noqa: E501

        The JSON Web Encryption [JWE] content encryption algorithm for the ID Token.<br>AES_128_CBC_HMAC_SHA_256 - Composite AES-CBC-128 HMAC-SHA-256<br>AES_192_CBC_HMAC_SHA_384 - Composite AES-CBC-192 HMAC-SHA-384<br>AES_256_CBC_HMAC_SHA_512 - Composite AES-CBC-256 HMAC-SHA-512<br>AES_128_GCM - AES-GCM-128<br>AES_192_GCM - AES-GCM-192<br>AES_256_GCM - AES-GCM-256  # noqa: E501

        :return: The id_token_content_encryption_algorithm of this ClientOIDCPolicy.  # noqa: E501
        :rtype: str
        """
        return self._id_token_content_encryption_algorithm

    @id_token_content_encryption_algorithm.setter
    def id_token_content_encryption_algorithm(self, id_token_content_encryption_algorithm):
        """Sets the id_token_content_encryption_algorithm of this ClientOIDCPolicy.

        The JSON Web Encryption [JWE] content encryption algorithm for the ID Token.<br>AES_128_CBC_HMAC_SHA_256 - Composite AES-CBC-128 HMAC-SHA-256<br>AES_192_CBC_HMAC_SHA_384 - Composite AES-CBC-192 HMAC-SHA-384<br>AES_256_CBC_HMAC_SHA_512 - Composite AES-CBC-256 HMAC-SHA-512<br>AES_128_GCM - AES-GCM-128<br>AES_192_GCM - AES-GCM-192<br>AES_256_GCM - AES-GCM-256  # noqa: E501

        :param id_token_content_encryption_algorithm: The id_token_content_encryption_algorithm of this ClientOIDCPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["AES_128_CBC_HMAC_SHA_256", "AES_192_CBC_HMAC_SHA_384", "AES_256_CBC_HMAC_SHA_512", "AES_128_GCM", "AES_192_GCM", "AES_256_GCM"]  # noqa: E501
        if (self._configuration.client_side_validation and
                id_token_content_encryption_algorithm not in allowed_values):
            raise ValueError(
                "Invalid value for `id_token_content_encryption_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(id_token_content_encryption_algorithm, allowed_values)
            )

        self._id_token_content_encryption_algorithm = id_token_content_encryption_algorithm

    @property
    def policy_group(self):
        """Gets the policy_group of this ClientOIDCPolicy.  # noqa: E501

        The Open ID Connect policy. A null value will represent the default policy group.  # noqa: E501

        :return: The policy_group of this ClientOIDCPolicy.  # noqa: E501
        :rtype: ResourceLink
        """
        return self._policy_group

    @policy_group.setter
    def policy_group(self, policy_group):
        """Sets the policy_group of this ClientOIDCPolicy.

        The Open ID Connect policy. A null value will represent the default policy group.  # noqa: E501

        :param policy_group: The policy_group of this ClientOIDCPolicy.  # noqa: E501
        :type: ResourceLink
        """

        self._policy_group = policy_group

    @property
    def grant_access_session_revocation_api(self):
        """Gets the grant_access_session_revocation_api of this ClientOIDCPolicy.  # noqa: E501

        Determines whether this client is allowed to access the Session Revocation API.  # noqa: E501

        :return: The grant_access_session_revocation_api of this ClientOIDCPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._grant_access_session_revocation_api

    @grant_access_session_revocation_api.setter
    def grant_access_session_revocation_api(self, grant_access_session_revocation_api):
        """Sets the grant_access_session_revocation_api of this ClientOIDCPolicy.

        Determines whether this client is allowed to access the Session Revocation API.  # noqa: E501

        :param grant_access_session_revocation_api: The grant_access_session_revocation_api of this ClientOIDCPolicy.  # noqa: E501
        :type: bool
        """

        self._grant_access_session_revocation_api = grant_access_session_revocation_api

    @property
    def grant_access_session_session_management_api(self):
        """Gets the grant_access_session_session_management_api of this ClientOIDCPolicy.  # noqa: E501

        Determines whether this client is allowed to access the Session Management API.  # noqa: E501

        :return: The grant_access_session_session_management_api of this ClientOIDCPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._grant_access_session_session_management_api

    @grant_access_session_session_management_api.setter
    def grant_access_session_session_management_api(self, grant_access_session_session_management_api):
        """Sets the grant_access_session_session_management_api of this ClientOIDCPolicy.

        Determines whether this client is allowed to access the Session Management API.  # noqa: E501

        :param grant_access_session_session_management_api: The grant_access_session_session_management_api of this ClientOIDCPolicy.  # noqa: E501
        :type: bool
        """

        self._grant_access_session_session_management_api = grant_access_session_session_management_api

    @property
    def logout_mode(self):
        """Gets the logout_mode of this ClientOIDCPolicy.  # noqa: E501

        The logout mode for this client. The default is 'NONE'.  # noqa: E501

        :return: The logout_mode of this ClientOIDCPolicy.  # noqa: E501
        :rtype: str
        """
        return self._logout_mode

    @logout_mode.setter
    def logout_mode(self, logout_mode):
        """Sets the logout_mode of this ClientOIDCPolicy.

        The logout mode for this client. The default is 'NONE'.  # noqa: E501

        :param logout_mode: The logout_mode of this ClientOIDCPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "PING_FRONT_CHANNEL", "OIDC_BACK_CHANNEL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                logout_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `logout_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(logout_mode, allowed_values)
            )

        self._logout_mode = logout_mode

    @property
    def ping_access_logout_capable(self):
        """Gets the ping_access_logout_capable of this ClientOIDCPolicy.  # noqa: E501

        Set this value to true if you wish to enable client application logout, and the client is PingAccess, or its logout endpoints follow the PingAccess path convention.  # noqa: E501

        :return: The ping_access_logout_capable of this ClientOIDCPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._ping_access_logout_capable

    @ping_access_logout_capable.setter
    def ping_access_logout_capable(self, ping_access_logout_capable):
        """Sets the ping_access_logout_capable of this ClientOIDCPolicy.

        Set this value to true if you wish to enable client application logout, and the client is PingAccess, or its logout endpoints follow the PingAccess path convention.  # noqa: E501

        :param ping_access_logout_capable: The ping_access_logout_capable of this ClientOIDCPolicy.  # noqa: E501
        :type: bool
        """

        self._ping_access_logout_capable = ping_access_logout_capable

    @property
    def logout_uris(self):
        """Gets the logout_uris of this ClientOIDCPolicy.  # noqa: E501

        A list of front-channel logout URIs for this client.  # noqa: E501

        :return: The logout_uris of this ClientOIDCPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._logout_uris

    @logout_uris.setter
    def logout_uris(self, logout_uris):
        """Sets the logout_uris of this ClientOIDCPolicy.

        A list of front-channel logout URIs for this client.  # noqa: E501

        :param logout_uris: The logout_uris of this ClientOIDCPolicy.  # noqa: E501
        :type: list[str]
        """

        self._logout_uris = logout_uris

    @property
    def back_channel_logout_uri(self):
        """Gets the back_channel_logout_uri of this ClientOIDCPolicy.  # noqa: E501

        The back-channel logout URI for this client.  # noqa: E501

        :return: The back_channel_logout_uri of this ClientOIDCPolicy.  # noqa: E501
        :rtype: str
        """
        return self._back_channel_logout_uri

    @back_channel_logout_uri.setter
    def back_channel_logout_uri(self, back_channel_logout_uri):
        """Sets the back_channel_logout_uri of this ClientOIDCPolicy.

        The back-channel logout URI for this client.  # noqa: E501

        :param back_channel_logout_uri: The back_channel_logout_uri of this ClientOIDCPolicy.  # noqa: E501
        :type: str
        """

        self._back_channel_logout_uri = back_channel_logout_uri

    @property
    def pairwise_identifier_user_type(self):
        """Gets the pairwise_identifier_user_type of this ClientOIDCPolicy.  # noqa: E501

        Determines whether the subject identifier type is pairwise.  # noqa: E501

        :return: The pairwise_identifier_user_type of this ClientOIDCPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._pairwise_identifier_user_type

    @pairwise_identifier_user_type.setter
    def pairwise_identifier_user_type(self, pairwise_identifier_user_type):
        """Sets the pairwise_identifier_user_type of this ClientOIDCPolicy.

        Determines whether the subject identifier type is pairwise.  # noqa: E501

        :param pairwise_identifier_user_type: The pairwise_identifier_user_type of this ClientOIDCPolicy.  # noqa: E501
        :type: bool
        """

        self._pairwise_identifier_user_type = pairwise_identifier_user_type

    @property
    def sector_identifier_uri(self):
        """Gets the sector_identifier_uri of this ClientOIDCPolicy.  # noqa: E501

        The URI references a file with a single JSON array of Redirect URI and JWKS URL values.  # noqa: E501

        :return: The sector_identifier_uri of this ClientOIDCPolicy.  # noqa: E501
        :rtype: str
        """
        return self._sector_identifier_uri

    @sector_identifier_uri.setter
    def sector_identifier_uri(self, sector_identifier_uri):
        """Sets the sector_identifier_uri of this ClientOIDCPolicy.

        The URI references a file with a single JSON array of Redirect URI and JWKS URL values.  # noqa: E501

        :param sector_identifier_uri: The sector_identifier_uri of this ClientOIDCPolicy.  # noqa: E501
        :type: str
        """

        self._sector_identifier_uri = sector_identifier_uri

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
        if issubclass(ClientOIDCPolicy, dict):
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
        if not isinstance(other, ClientOIDCPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientOIDCPolicy):
            return True

        return self.to_dict() != other.to_dict()