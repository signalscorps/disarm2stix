# disarm2stix

A command line tool that turns the DISARM framework into STIX 2.1 Objects.

## Overview

The [DISARM Framework](https://www.disarm.foundation/framework) in parts aims to provide a single knowledge-base for disinformation classifications.

In the way MITRE ATT&CK has provided a standard for contextual information about adversary tactics and techniques based on real-world observations, DISARM aims to do the same for disinformation.

This code is heavily based on the DISARM Foundations [DISARM-STIX2 repository](https://github.com/DISARMFoundation/DISARM-STIX2/). I decided to create a seperate codebase as that repository does not seem to be actively maintained.

The code in this repository;

1. Takes the latest DISARM data (`.xls` file)
2. Converts them to STIX 2.1 Objects
3. Stores the STIX 2.1 Objects in the file store

## Install

```shell
# get code
git clone https://github.com/signalscorps/disarm2stix
cd DISARM-STIX2
# create venv
python3 -m venv disarm2stix_venv
source disarm2stix_venv/bin/activate
# install requirements
pip3 install -r requirements.txt
```

## Run

Generate the STIX objects in the `stix2_objects/` folder;

```shell 
python3 disarm2stix.py
```

On each run, all objects will be completely regenerated.

## Useful supporting tools

* Existing STIX 2.1 schemas: [cti-stix2-json-schemas](https://github.com/oasis-open/cti-stix2-json-schemas): OASIS TC Open Repository: Non-normative schemas and examples for STIX 2
* To generate STIX 2.1 extensions: [stix2 Python Lib](https://stix2.readthedocs.io/en/latest/)
* STIX 2.1 specifications for objects: [STIX 2.1 docs](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html)
* [DISARM Framework](https://www.disarm.foundation/framework)

## Support

[Minimal support provided via Slack in the #support-oss channel](https://join.slack.com/t/signalscorps-public/shared_invite/zt-1exnc12ww-9RKR6aMgO57GmHcl156DAA).

## License

[Apache 2.0](/LICENSE).