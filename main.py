import logging

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# Setup basic logging at INFO level
logging.basicConfig(level=logging.INFO)


def ping_server(cluster: str, credentials: tuple) -> None:
    """
    From Atlas (MongoDB) sample code for pinging a server cluster.

    :param credentials: A user : password key pairing (dict).
    :param cluster: The name of a cluster within the project.
    :return: None. A successful ping message will be logged.
    """
    username, password = credentials

    # Build server URI
    uri = (f"mongodb+srv://{username}:{password}@{cluster.lower()}.ejwdq.mongodb.net/"
           f"?retryWrites=true&w=majority&appName={cluster}")

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        logging.info("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    logging.info("Main program starting...")

    PROJECT: str = 'forgineer'
    CLUSTER: str = 'FreeMongoDB'
    USER: str = 'blake'

    import config

    user_credentials: tuple = config.get_credentials(project=PROJECT, cluster=CLUSTER, username=USER)
    ping_server(cluster=CLUSTER, credentials=user_credentials)
