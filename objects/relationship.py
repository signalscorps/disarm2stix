import uuid
from uuid import UUID
from helpers import utils
from stix2 import Relationship
from datetime import datetime

def make_disarm_subtechnique_relationship(source, target, marking_id, identity_id, date):

    relationship = Relationship(
       id ="relationship--{}".format(uuid.uuid5(namespace=UUID('e9988722-c396-5a91-a08d-db742bd3624b'), name="{}+{}".format(source,target))

        ),
        source_ref=source,
        target_ref=target,
        relationship_type="subtechnique-of",
        object_marking_refs=marking_id,
        created_by_ref=identity_id,
        created=datetime.strptime(date, '%Y-%m-%d'),
        modified=datetime.strptime(date, '%Y-%m-%d'),
    )

    return relationship



def make_disarm_subtechnique_relationships(techniques, identity_id, marking_id, date):

    technique_ids = {}
    for technique in techniques:
        technique_ids[technique["external_references"][0]["external_id"]] = technique["id"]

    relationships = []
    for technique in techniques:
        if technique["x_mitre_is_subtechnique"]:
            technique_id = technique_ids[technique["external_references"][0]["external_id"].split(".")[0]]
            relationship = make_disarm_subtechnique_relationship(technique["id"], technique_id, marking_id, identity_id, date)
            relationships.append(relationship)
            utils.fs.add(relationship)

    return relationships