import json
import logging


def get_configuration() -> dict:
    try:
        with open(file='config.json') as configuration_file:
            return json.load(configuration_file)
    except FileExistsError:
        logging.error('The configuration file (config.json) does not appear to exist in the current directory.')


def get_credentials(project: str, cluster: str, username: str) -> tuple:
    """
    Retrieve credentials from the local configuration file (config.json).

    :param project: The name of Atlas (MongoDB) project.
    :param cluster: The name of a cluster within the project.
    :param username: An existing username added to the cluster.
    :return: A user : password key pairing (dict).
    """
    configuration_json: dict = get_configuration()

    try:
        userpasswd: str = configuration_json[project][cluster]['users'][username]

        return username, userpasswd
    except KeyError:
        logging.error('One or more dictionary keys does not exist. Please review your config file.')


if __name__ == '__main__':
    pass
