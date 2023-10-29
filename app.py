import swagger_client
from swagger_client.rest import ApiException
from swagger_client.configuration import Configuration
from pprint import pprint
import string
import random


def get_random_id(size=3, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_client(configuration):
    client = swagger_client.ApiClient(configuration)
    client.set_default_header("X-XSRF-Header", "41A65048-D2CE-4A8B-ACF0-D8D1C7547215")
    client.set_default_header("Authorization", configuration.get_basic_auth_token())
    return client


def get_version(client):
    api_instance = swagger_client.VersionApi(client)

    try:
        # Check Version
        response = api_instance.get_version()
        return response
    except ApiException as e:
        print("Exception when calling Version: %s\n" % e)
        exit(-1)


# Create a PingFederate Administrative Account
def create_admin_account(client,
                         username=None,
                         password=None,
                         active=None,
                         description=None,
                         email_address=None,
                         department=None,
                         roles=[]):
    # create an instance of the API class
    admin_account_api = swagger_client.AdministrativeAccountsApi(api_client=client)
    # AdministrativeAccount | Administrative account information.
    request = swagger_client.AdministrativeAccount(
        username=username,
        password=password,
        active=active,
        description=description,
        email_address=email_address,
        department=department,
        roles=roles
    )

    try:
        # Add a new PingFederate native Administrative Account.
        response = admin_account_api.add_account(request)
        return response
    except ApiException as e:
        print("Exception when calling AdministrativeAccountsApi->add_account: %s\n" % e)
        exit(-1)


# Get all the PingFederate native Administrative Accounts.
def get_admin_account_list(client):
    # create an instance of the API class
    admin_account_api = swagger_client.AdministrativeAccountsApi(api_client=client)
    try:
        # Add a new PingFederate native Administrative Account.
        response = admin_account_api.get_accounts()
        return response
    except ApiException as e:
        print("Exception when calling AdministrativeAccountsApi->add_account: %s\n" % e)
        exit(-1)


if __name__ == '__main__':
    print("Initializing Configuration")

    configuration = Configuration()
    configuration.username = "Administrator"
    configuration.password = "2FederateM0re"
    configuration.verify_ssl = False

    client = get_client(configuration)

    resp = get_version(client)

    print(f"PingFederate version {resp.version}")
    username = f"alice_{get_random_id()}"
    resp = create_admin_account(client,
                                username=username,
                                password="2FederateM0re",
                                active=True,
                                description="Admin Account for Me",
                                email_address=f"{username}@example.com",
                                department="Identity and Access Management",
                                roles=["ADMINISTRATOR"]
                                )

    print(f"Admin Account {username} created.")
    pprint(resp)

    resp = get_admin_account_list(client)
    print("List of current Admin Accounts")
    for ac in resp.items:
        pprint(ac)
