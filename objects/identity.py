import json
from stix2 import parse
from helpers import utils


def make_disarm_identity():
    DEFAULT_OBJECT_URL = [
        "https://raw.githubusercontent.com/signalscorps/stix4signalscorps/main/objects/identity/identity--e9988722-c396-5a91-a08d-db742bd3624b.json"
    ]

    object_list = []
    for obj in DEFAULT_OBJECT_URL:
        utils.fs.add(parse(json.loads(utils.load_file_from_url(obj))))
        object_list.append(json.loads(utils.load_file_from_url(obj)))
    return object_list
