import logging

from botocore.exceptions import ClientError

log = logging.getLogger("cloudcam")
log.setLevel(logging.DEBUG)


def ignore_resource_already_exists(method, **kwargs):
    try:
        return method(**kwargs)
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceAlreadyExistsException":
            pass
        else:
            raise


def ignore_resource_not_found(method, **kwargs):
    try:
        return method(**kwargs)
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            pass
        else:
            raise


def ignore_all(method, **kwargs):
    try:
        return method(**kwargs)
    except ClientError as e:
        pass


