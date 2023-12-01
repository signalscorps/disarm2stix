import json
from stix2 import parse
from helpers import utils

def make_disarm_marking_definition(identity_id=None):

    DEFAULT_OBJECT_URL = [
        "https://raw.githubusercontent.com/signalscorps/stix4signalscorps/main/objects/marking-definition/marking-definition--e9988722-c396-5a91-a08d-db742bd3624b.json",
    ]
    object_list = []
    for obj in DEFAULT_OBJECT_URL:
        object = parse(json.loads(utils.load_file_from_url(obj)))
        if not utils.fs.get(object.get("id")):
            utils.fs.add(object)
        object_list.append(json.loads(utils.load_file_from_url(obj)))
    return object_list


def custom_md():
    return ["marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9"
            ]+[make_disarm_marking_definition()[0].get("id")]
