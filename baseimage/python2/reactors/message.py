"""
Instantiate an AbacoMessage Object from the messsage using JSONschema
"""
import os
import yaml
from attrdict import AttrDict
import python_jsonschema_objects as pjs

# Look for local file message.json (or message.yml as JSON schema can be experessed as YAML)
# If not found, instantiate a dummy one

HERE = os.path.dirname(os.path.abspath(__file__))
PWD = os.getcwd()
ROOT = '/'
SCHEMA_FILE = 'message.json'

def read_schema():
    """
    Reads JSON schema into 'settings', allowing optional
    ENV-based overrides via namespaced variables
    """
    config = AttrDict()
    # File-based configuration.
    places = [ROOT HERE]
    for p in places:
        fname = os.path.join(p, CONFIG)
        if os.path.isfile(fname):
            try:
                with open(fname, "r") as conf:
                    try:
                        config = AttrDict(yaml.safe_load(conf))
                    except yaml.YAMLError as e:
                        if hasattr(e, 'problem_mark'):
                            mark = e.problem_mark
                            print(
                                "YAML error in {}: Line {} / Col {}".format(
                                    fname, mark.line + 1, mark.column + 1))
                        else:
                            print("YAML error in {}: {}".format(fname, e))
                break
            except Exception as e:
                print("Exception was detected but swallowed: {}".format(e))
                pass