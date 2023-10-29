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


class OIDCProviderSettings(object):
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
        'scopes': 'str',
        'authorization_endpoint': 'str',
        'pushed_authorization_request_endpoint': 'str',
        'login_type': 'str',
        'authentication_scheme': 'str',
        'authentication_signing_algorithm': 'str',
        'request_signing_algorithm': 'str',
        'enable_pkce': 'bool',
        'token_endpoint': 'str',
        'user_info_endpoint': 'str',
        'jwks_url': 'str',
        'track_user_sessions_for_logout': 'bool',
        'request_parameters': 'list[OIDCRequestParameter]',
        'redirect_uri': 'str',
        'back_channel_logout_uri': 'str'
    }

    attribute_map = {
        'scopes': 'scopes',
        'authorization_endpoint': 'authorizationEndpoint',
        'pushed_authorization_request_endpoint': 'pushedAuthorizationRequestEndpoint',
        'login_type': 'loginType',
        'authentication_scheme': 'authenticationScheme',
        'authentication_signing_algorithm': 'authenticationSigningAlgorithm',
        'request_signing_algorithm': 'requestSigningAlgorithm',
        'enable_pkce': 'enablePKCE',
        'token_endpoint': 'tokenEndpoint',
        'user_info_endpoint': 'userInfoEndpoint',
        'jwks_url': 'jwksURL',
        'track_user_sessions_for_logout': 'trackUserSessionsForLogout',
        'request_parameters': 'requestParameters',
        'redirect_uri': 'redirectUri',
        'back_channel_logout_uri': 'backChannelLogoutUri'
    }

    def __init__(self, scopes=None, authorization_endpoint=None, pushed_authorization_request_endpoint=None, login_type=None, authentication_scheme=None, authentication_signing_algorithm=None, request_signing_algorithm=None, enable_pkce=None, token_endpoint=None, user_info_endpoint=None, jwks_url=None, track_user_sessions_for_logout=None, request_parameters=None, redirect_uri=None, back_channel_logout_uri=None, _configuration=None):  # noqa: E501
        """OIDCProviderSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._scopes = None
        self._authorization_endpoint = None
        self._pushed_authorization_request_endpoint = None
        self._login_type = None
        self._authentication_scheme = None
        self._authentication_signing_algorithm = None
        self._request_signing_algorithm = None
        self._enable_pkce = None
        self._token_endpoint = None
        self._user_info_endpoint = None
        self._jwks_url = None
        self._track_user_sessions_for_logout = None
        self._request_parameters = None
        self._redirect_uri = None
        self._back_channel_logout_uri = None
        self.discriminator = None

        self.scopes = scopes
        self.authorization_endpoint = authorization_endpoint
        if pushed_authorization_request_endpoint is not None:
            self.pushed_authorization_request_endpoint = pushed_authorization_request_endpoint
        self.login_type = login_type
        if authentication_scheme is not None:
            self.authentication_scheme = authentication_scheme
        if authentication_signing_algorithm is not None:
            self.authentication_signing_algorithm = authentication_signing_algorithm
        if request_signing_algorithm is not None:
            self.request_signing_algorithm = request_signing_algorithm
        if enable_pkce is not None:
            self.enable_pkce = enable_pkce
        if token_endpoint is not None:
            self.token_endpoint = token_endpoint
        if user_info_endpoint is not None:
            self.user_info_endpoint = user_info_endpoint
        self.jwks_url = jwks_url
        if track_user_sessions_for_logout is not None:
            self.track_user_sessions_for_logout = track_user_sessions_for_logout
        if request_parameters is not None:
            self.request_parameters = request_parameters
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        if back_channel_logout_uri is not None:
            self.back_channel_logout_uri = back_channel_logout_uri

    @property
    def scopes(self):
        """Gets the scopes of this OIDCProviderSettings.  # noqa: E501

        Space separated scope values that the OpenID Provider supports.  # noqa: E501

        :return: The scopes of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this OIDCProviderSettings.

        Space separated scope values that the OpenID Provider supports.  # noqa: E501

        :param scopes: The scopes of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and scopes is None:
            raise ValueError("Invalid value for `scopes`, must not be `None`")  # noqa: E501

        self._scopes = scopes

    @property
    def authorization_endpoint(self):
        """Gets the authorization_endpoint of this OIDCProviderSettings.  # noqa: E501

        URL of the OpenID Provider's OAuth 2.0 Authorization Endpoint.  # noqa: E501

        :return: The authorization_endpoint of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._authorization_endpoint

    @authorization_endpoint.setter
    def authorization_endpoint(self, authorization_endpoint):
        """Sets the authorization_endpoint of this OIDCProviderSettings.

        URL of the OpenID Provider's OAuth 2.0 Authorization Endpoint.  # noqa: E501

        :param authorization_endpoint: The authorization_endpoint of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and authorization_endpoint is None:
            raise ValueError("Invalid value for `authorization_endpoint`, must not be `None`")  # noqa: E501

        self._authorization_endpoint = authorization_endpoint

    @property
    def pushed_authorization_request_endpoint(self):
        """Gets the pushed_authorization_request_endpoint of this OIDCProviderSettings.  # noqa: E501

        URL of the OpenID Provider's OAuth 2.0 Pushed Authorization Request Endpoint.  # noqa: E501

        :return: The pushed_authorization_request_endpoint of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._pushed_authorization_request_endpoint

    @pushed_authorization_request_endpoint.setter
    def pushed_authorization_request_endpoint(self, pushed_authorization_request_endpoint):
        """Sets the pushed_authorization_request_endpoint of this OIDCProviderSettings.

        URL of the OpenID Provider's OAuth 2.0 Pushed Authorization Request Endpoint.  # noqa: E501

        :param pushed_authorization_request_endpoint: The pushed_authorization_request_endpoint of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """

        self._pushed_authorization_request_endpoint = pushed_authorization_request_endpoint

    @property
    def login_type(self):
        """Gets the login_type of this OIDCProviderSettings.  # noqa: E501

        The OpenID Connect login type. These values maps to: <br>  CODE: Authentication using Code Flow <br> POST: Authentication using Form Post <br> POST_AT: Authentication using Form Post with Access Token  # noqa: E501

        :return: The login_type of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._login_type

    @login_type.setter
    def login_type(self, login_type):
        """Sets the login_type of this OIDCProviderSettings.

        The OpenID Connect login type. These values maps to: <br>  CODE: Authentication using Code Flow <br> POST: Authentication using Form Post <br> POST_AT: Authentication using Form Post with Access Token  # noqa: E501

        :param login_type: The login_type of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and login_type is None:
            raise ValueError("Invalid value for `login_type`, must not be `None`")  # noqa: E501
        allowed_values = ["CODE", "POST", "POST_AT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                login_type not in allowed_values):
            raise ValueError(
                "Invalid value for `login_type` ({0}), must be one of {1}"  # noqa: E501
                .format(login_type, allowed_values)
            )

        self._login_type = login_type

    @property
    def authentication_scheme(self):
        """Gets the authentication_scheme of this OIDCProviderSettings.  # noqa: E501

        The OpenID Connect Authentication Scheme. This is required for Authentication using Code Flow.   # noqa: E501

        :return: The authentication_scheme of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._authentication_scheme

    @authentication_scheme.setter
    def authentication_scheme(self, authentication_scheme):
        """Sets the authentication_scheme of this OIDCProviderSettings.

        The OpenID Connect Authentication Scheme. This is required for Authentication using Code Flow.   # noqa: E501

        :param authentication_scheme: The authentication_scheme of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["BASIC", "POST", "PRIVATE_KEY_JWT", "CLIENT_SECRET_JWT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                authentication_scheme not in allowed_values):
            raise ValueError(
                "Invalid value for `authentication_scheme` ({0}), must be one of {1}"  # noqa: E501
                .format(authentication_scheme, allowed_values)
            )

        self._authentication_scheme = authentication_scheme

    @property
    def authentication_signing_algorithm(self):
        """Gets the authentication_signing_algorithm of this OIDCProviderSettings.  # noqa: E501

        The authentication signing algorithm for token endpoint PRIVATE_KEY_JWT or CLIENT_SECRET_JWT authentication. Asymmetric algorithms are allowed for PRIVATE_KEY_JWT and symmetric algorithms are allowed for CLIENT_SECRET_JWT. For RSASSA-PSS signing algorithm, PingFederate must be integrated with a hardware security module (HSM) or Java 11.  # noqa: E501

        :return: The authentication_signing_algorithm of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._authentication_signing_algorithm

    @authentication_signing_algorithm.setter
    def authentication_signing_algorithm(self, authentication_signing_algorithm):
        """Sets the authentication_signing_algorithm of this OIDCProviderSettings.

        The authentication signing algorithm for token endpoint PRIVATE_KEY_JWT or CLIENT_SECRET_JWT authentication. Asymmetric algorithms are allowed for PRIVATE_KEY_JWT and symmetric algorithms are allowed for CLIENT_SECRET_JWT. For RSASSA-PSS signing algorithm, PingFederate must be integrated with a hardware security module (HSM) or Java 11.  # noqa: E501

        :param authentication_signing_algorithm: The authentication_signing_algorithm of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "HS256", "HS384", "HS512", "RS256", "RS384", "RS512", "ES256", "ES384", "ES512", "PS256", "PS384", "PS512"]  # noqa: E501
        if (self._configuration.client_side_validation and
                authentication_signing_algorithm not in allowed_values):
            raise ValueError(
                "Invalid value for `authentication_signing_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(authentication_signing_algorithm, allowed_values)
            )

        self._authentication_signing_algorithm = authentication_signing_algorithm

    @property
    def request_signing_algorithm(self):
        """Gets the request_signing_algorithm of this OIDCProviderSettings.  # noqa: E501

        The request signing algorithm. Required only if you wish to use signed requests. Only asymmetric algorithms are allowed. For RSASSA-PSS signing algorithm, PingFederate must be integrated with a hardware security module (HSM) or Java 11.  # noqa: E501

        :return: The request_signing_algorithm of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._request_signing_algorithm

    @request_signing_algorithm.setter
    def request_signing_algorithm(self, request_signing_algorithm):
        """Sets the request_signing_algorithm of this OIDCProviderSettings.

        The request signing algorithm. Required only if you wish to use signed requests. Only asymmetric algorithms are allowed. For RSASSA-PSS signing algorithm, PingFederate must be integrated with a hardware security module (HSM) or Java 11.  # noqa: E501

        :param request_signing_algorithm: The request_signing_algorithm of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "HS256", "HS384", "HS512", "RS256", "RS384", "RS512", "ES256", "ES384", "ES512", "PS256", "PS384", "PS512"]  # noqa: E501
        if (self._configuration.client_side_validation and
                request_signing_algorithm not in allowed_values):
            raise ValueError(
                "Invalid value for `request_signing_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(request_signing_algorithm, allowed_values)
            )

        self._request_signing_algorithm = request_signing_algorithm

    @property
    def enable_pkce(self):
        """Gets the enable_pkce of this OIDCProviderSettings.  # noqa: E501

        Enable Proof Key for Code Exchange (PKCE). When enabled, the client sends an SHA-256 code challenge and corresponding code verifier to the OpenID Provider during the authorization code flow.  # noqa: E501

        :return: The enable_pkce of this OIDCProviderSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_pkce

    @enable_pkce.setter
    def enable_pkce(self, enable_pkce):
        """Sets the enable_pkce of this OIDCProviderSettings.

        Enable Proof Key for Code Exchange (PKCE). When enabled, the client sends an SHA-256 code challenge and corresponding code verifier to the OpenID Provider during the authorization code flow.  # noqa: E501

        :param enable_pkce: The enable_pkce of this OIDCProviderSettings.  # noqa: E501
        :type: bool
        """

        self._enable_pkce = enable_pkce

    @property
    def token_endpoint(self):
        """Gets the token_endpoint of this OIDCProviderSettings.  # noqa: E501

        URL of the OpenID Provider's OAuth 2.0 Token Endpoint.  # noqa: E501

        :return: The token_endpoint of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._token_endpoint

    @token_endpoint.setter
    def token_endpoint(self, token_endpoint):
        """Sets the token_endpoint of this OIDCProviderSettings.

        URL of the OpenID Provider's OAuth 2.0 Token Endpoint.  # noqa: E501

        :param token_endpoint: The token_endpoint of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """

        self._token_endpoint = token_endpoint

    @property
    def user_info_endpoint(self):
        """Gets the user_info_endpoint of this OIDCProviderSettings.  # noqa: E501

        URL of the OpenID Provider's UserInfo Endpoint.  # noqa: E501

        :return: The user_info_endpoint of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._user_info_endpoint

    @user_info_endpoint.setter
    def user_info_endpoint(self, user_info_endpoint):
        """Sets the user_info_endpoint of this OIDCProviderSettings.

        URL of the OpenID Provider's UserInfo Endpoint.  # noqa: E501

        :param user_info_endpoint: The user_info_endpoint of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """

        self._user_info_endpoint = user_info_endpoint

    @property
    def jwks_url(self):
        """Gets the jwks_url of this OIDCProviderSettings.  # noqa: E501

        URL of the OpenID Provider's JSON Web Key Set [JWK] document.  # noqa: E501

        :return: The jwks_url of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._jwks_url

    @jwks_url.setter
    def jwks_url(self, jwks_url):
        """Sets the jwks_url of this OIDCProviderSettings.

        URL of the OpenID Provider's JSON Web Key Set [JWK] document.  # noqa: E501

        :param jwks_url: The jwks_url of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and jwks_url is None:
            raise ValueError("Invalid value for `jwks_url`, must not be `None`")  # noqa: E501

        self._jwks_url = jwks_url

    @property
    def track_user_sessions_for_logout(self):
        """Gets the track_user_sessions_for_logout of this OIDCProviderSettings.  # noqa: E501

        Determines whether PingFederate tracks a logout entry when a user signs in, so that the user session can later be terminated via back-channel logout.  # noqa: E501

        :return: The track_user_sessions_for_logout of this OIDCProviderSettings.  # noqa: E501
        :rtype: bool
        """
        return self._track_user_sessions_for_logout

    @track_user_sessions_for_logout.setter
    def track_user_sessions_for_logout(self, track_user_sessions_for_logout):
        """Sets the track_user_sessions_for_logout of this OIDCProviderSettings.

        Determines whether PingFederate tracks a logout entry when a user signs in, so that the user session can later be terminated via back-channel logout.  # noqa: E501

        :param track_user_sessions_for_logout: The track_user_sessions_for_logout of this OIDCProviderSettings.  # noqa: E501
        :type: bool
        """

        self._track_user_sessions_for_logout = track_user_sessions_for_logout

    @property
    def request_parameters(self):
        """Gets the request_parameters of this OIDCProviderSettings.  # noqa: E501

        A list of request parameters. Request parameters with same name but different attribute values are treated as a multi-valued request parameter.  # noqa: E501

        :return: The request_parameters of this OIDCProviderSettings.  # noqa: E501
        :rtype: list[OIDCRequestParameter]
        """
        return self._request_parameters

    @request_parameters.setter
    def request_parameters(self, request_parameters):
        """Sets the request_parameters of this OIDCProviderSettings.

        A list of request parameters. Request parameters with same name but different attribute values are treated as a multi-valued request parameter.  # noqa: E501

        :param request_parameters: The request_parameters of this OIDCProviderSettings.  # noqa: E501
        :type: list[OIDCRequestParameter]
        """

        self._request_parameters = request_parameters

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this OIDCProviderSettings.  # noqa: E501

        The redirect URI. This is a read-only parameter.  # noqa: E501

        :return: The redirect_uri of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this OIDCProviderSettings.

        The redirect URI. This is a read-only parameter.  # noqa: E501

        :param redirect_uri: The redirect_uri of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def back_channel_logout_uri(self):
        """Gets the back_channel_logout_uri of this OIDCProviderSettings.  # noqa: E501

        The Back-Channel Logout URI. This read-only parameter is available when user sessions are tracked for logout.  # noqa: E501

        :return: The back_channel_logout_uri of this OIDCProviderSettings.  # noqa: E501
        :rtype: str
        """
        return self._back_channel_logout_uri

    @back_channel_logout_uri.setter
    def back_channel_logout_uri(self, back_channel_logout_uri):
        """Sets the back_channel_logout_uri of this OIDCProviderSettings.

        The Back-Channel Logout URI. This read-only parameter is available when user sessions are tracked for logout.  # noqa: E501

        :param back_channel_logout_uri: The back_channel_logout_uri of this OIDCProviderSettings.  # noqa: E501
        :type: str
        """

        self._back_channel_logout_uri = back_channel_logout_uri

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
        if issubclass(OIDCProviderSettings, dict):
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
        if not isinstance(other, OIDCProviderSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OIDCProviderSettings):
            return True

        return self.to_dict() != other.to_dict()