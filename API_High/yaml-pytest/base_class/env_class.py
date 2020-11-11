import os
import json
class EnvClass:
    def get_env(self):
        return json.loads(os.environ['case'])
    