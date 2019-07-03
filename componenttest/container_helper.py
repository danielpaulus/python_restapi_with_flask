import logging
import time
from conu import DockerRunBuilder, DockerBackend
import pymongo
# docker run -d -p 27017:27017 mongo
# our webserver will be accessible on this port
port = 27017

# we'll utilize this container image
image_name = "mongo"
image_tag = "latest"


def isMongoRunning():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=1000)
        client.server_info()
        return True
    except pymongo.errors.ServerSelectionTimeoutError as err:
        # do whatever you need
        print(err)
        return False

# we'll run our container using docker engine
with DockerBackend(logging_level=logging.DEBUG) as backend:
    # the image will be pulled if it's not present
    image = backend.ImageClass(image_name, tag=image_tag)

    # the command to run in a container
    options = ["-p", "{}:{}".format(port, port)]
    container = image.run_via_binary(additional_opts=options)

    try:
        # we need to wait for the webserver to start serving
        is_open = False
        container.start()
        while not isMongoRunning():
            print("mongo is not up yet..")
            time.sleep(1)
        print("mongo is up")


    finally:
        container.kill()
        container.delete()

# def launchMongo():
