## The logic

### Data download

The DISARM foundation maintain an Excel copy of the DISARM Framework here:

```shell
https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/DISARM_MASTER_DATA/DISARM_FRAMEWORKS_MASTER.xlsx
```

This is downloaded on each request, and is used to generate the STIX 2.1 objects. Currently only the `techniques` and `tactics` tabs are used.

## How is works

disarm2stix converts the corresponding DISARM object into the following STIX 2.1 object shown in the following table.

| DISARM    | STIX2                 |
|-----------|-----------------------|
| Matrix    | `x-mitre-matrix`      |
| Tactic    | `x-mitre-tactic`      |
| Technique | `attack-pattern`      |

This conversion (especially the STIX custom objects `x-`) is heavily inspired by MITRE ATT&CK STIX 2.1 Objects.

### Matrix

```json
{
    "type": "x-mitre-matrix",
    "spec_version": "2.1",
    "id": "x-mitre-matrix--<UUID V5>",
    "created_by_ref": "<IMPORTED IDENTITY OBJECT>",
    "created": "<DATE IN DISARM_VERSION FILE>",
    "modified": "<DATE IN DISARM_VERSION FILE>",
    "name": "DISARM Framework",
    "description": "DISARM is a framework designed for describing and understanding disinformation incidents.",
    "tactic_refs": [
        "<LIST OF ALL x-mitre-tactic IN BUNDLE>",
	],
    "external_references": [
        {
            "source_name": "DISARM",
            "url": "https://www.disarm.foundation/",
            "external_id": "DISARM"
        }
    ],
    "object_marking_refs": [
        "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9",
        "<IMPORTED MARKING DEFINITION OBJECT>"
    ]
}
```

To generate the id, a UUIDv5 is generated using the namespace `e9988722-c396-5a91-a08d-db742bd3624b` and `DISARM`.

### Tactic

```json
{
    "type": "x-mitre-tactic",
    "spec_version": "2.1",
    "id": "x-mitre-tactic--<UUID V5>",
    "created_by_ref": "<IMPORTED IDENTITY OBJECT>",
    "created": "<DATE IN DISARM_VERSION FILE>",
    "modified": "<DATE IN DISARM_VERSION FILE>",
    "name": "<name>",
    "description": "<summary>",
    "external_references": [
        {
           "source_name": "DISARM",
           "url": "https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/generated_pages/tactics/<tactic.disarm_id>.md",
           "external_id": "<tactic.disarm_id>"
        }
    ],
    "object_marking_refs": [
        "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9",
        "<IMPORTED MARKING DEFINTION OBJECTS>"
    ],
    "x_mitre_shortname": "<machine friendly name>"
}
```

To generate the id, a UUIDv5 is generated using the namespace `e9988722-c396-5a91-a08d-db742bd3624b` and `<tactic.disarm_id>`.

### Technique

```json
{
    "type": "attack-pattern",
    "spec_version": "2.1",
    "id": "attack-pattern--<UUID V5>",
    "created_by_ref": "<IMPORTED IDENTITY OBJECT>",
    "created": "<DATE IN DISARM_VERSION FILE>",
    "modified": "<DATE IN DISARM_VERSION FILE>",
    "name": "<name>",
    "description": "<summary>",
    "external_references": [
       {
            "source_name": "DISARM",
            "url": "https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/generated_pages/techniques/<technique.disarm_id>.md",
            "external_id": "<technique.disarm_id>"
        }
    ],
    "object_marking_refs": [
        "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9",
        "<IMPORTED MARKING DEFINTION OBJECTS>"
    ],
    "kill_chain_phases": [
       {
           "kill_chain_name": "DISARM",
           "phase_name": "<parent tactic machine friendly name>"
        }
    ],
    "x_mitre_is_subtechnique": "<boolean, if subtechique>",
    "x_mitre_platforms": [
        "Windows",
        "Linux",
        "Mac"
    ],
    "x_mitre_version": "2.1"
}
```

An object is determined to be a subtechnique if the `<technique.disarm_id>` contains a `.`. e.g. is a subtechnique `T0019.002`, is not a subtechnique `T0019`.

To generate the id, a UUIDv5 is generated using the namespace `e9988722-c396-5a91-a08d-db742bd3624b` and `<technique.disarm_id>`.

### Relationships

DISARM contains a hierachical structure of data where a technique can have a child (a subtechnique). e.g parent = T0019 and child = T0019.002.

You can identify a subtechnique if the techniques `attack-pattern` object has a `x_mitre_is_subtechnique` equal to `true`. If this is the case, the following relationship is created;

```json
{
    "type": "relationship",
    "spec_version": "2.1",
    "id": "relationship--<UUIDV5 GENERATION LOGIC>",
    "created_by_ref": "<IMPORTED IDENTITY OBJECT>",
    "created": "<CREATED TIME OF MOST RECENT DISARM OBJECT IN PAIR>",
    "modified": "<CREATED TIME OF MOST RECENT DISARM OBJECT IN PAIR>",
    "relationship_type": "subtechnique-of",
    "source_ref": "attack-pattern--<CHILD OBJECT>",
    "target_ref": "attack-pattern--<PARENT OBJECT>",
    "object_marking_refs": [
        "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9",
        "<IMPORTED MARKING DEFINTION OBJECTS>"
    ],
}
```

To generate the id of the SRO, a UUIDv5 is generated using the namespace `e9988722-c396-5a91-a08d-db742bd3624b` and `<source_ref>+<target_ref>`.

### Bundle

disarm2stix also creates a STIX 2.1 Bundle JSON object containing all the other STIX 2.1 Objects created at each run. The Bundle takes the format;

```json
{
    "type": "bundle",
    "id": "bundle--<UUIDV5 GENERATION LOGIC>",
    "objects": [
        "<ALL STIX JSON OBJECTS>"
    ]
}
```

To generate the id, a UUIDv5 is generated using the namespace `e9988722-c396-5a91-a08d-db742bd3624b` and the MD5 file hash of all objects in the bundle.

Unlike the other STIX Objects, this means on every update a new bundle ID will be generated (as the date changes in the UUIDv5 generation). This means each saved bundle provides a historic snapshot of the old versions, should a user ever need to retrieve them.

### Misc objects

To support the `_ref`s created in the objects shown above, two other objects are imported by disarm2stix on first run;

* https://raw.githubusercontent.com/signalscorps/stix4signalscorps/main/objects/identity/identity--e9988722-c396-5a91-a08d-db742bd3624b.json
* https://raw.githubusercontent.com/signalscorps/stix4signalscorps/main/objects/marking-definition/marking-definition--e9988722-c396-5a91-a08d-db742bd3624b.json

These are hardcoded into the `data/stix_templates/` directory in this repository.

### A note on custom properties (`x_`)

The DISARM team used a range of custom properties found in ATT&CK so the DISARM can be rendered with MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/).

In many cases these don't make sense in the context of a DISARM object, but are required to render in the A&CK navigator, e.g.

```json
            "x_mitre_is_subtechnique": true,
            "x_mitre_platforms": [
                "Windows",
                "Linux",
                "Mac"
            ],
            "x_mitre_version": "2.1"
```

I decided to also include these.

### Shortcomings

* DISARM is not obviously versionsed. [It appears this is only done in blog posts](https://medium.com/disarming-disinformation/disarm-update-version-1-3-9dfcf2a29864). A such the `DISARM_VERSION` needs to be manually updated.

### Storing the objects in the file store

To support a similar approach to object distribution as MITRE do for both ATT&CK and CAPEC (objects stored as json files on GihHub), this script also allows for the STIX 2.1 objects to be stored in the filesystem.

The objects are stored in the root directory. The directory structure is defined by the STIX 2 Library's filesystem API, [as described here](https://stix2.readthedocs.io/en/latest/guide/filesystem.html).

A [STIX 2.1 Bundle file](https://stix2.readthedocs.io/en/latest/guide/creating.html#Creating-Bundles) (that contains all Objects for that version) is also created in the same way. The STIX 2.1 library does not have the functionality to store bundles directly to the filesystem like other objects, so disarm2stix stores bundles under the path;

```shell
/bundle/disarm-bundle.json
```