# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for formatting twitter data

import json
import requests
from st2common.runners.base_action import Action

class FormatTweet(Action):

    def run(self, tweet_body):        # Get trigger dictionaary.
        if tweet_body['payload']['user']['screen_name'] == 'netwookie':
            line = tweet_body['payload']['text']
            # Anything between two slashes is the vlan group
            x,vlans,y = line.split('/')
            name='Automated vlan group with Twitter & StackStorm'
            description="To prove I can integrate anything into plexxi"
        return (True, vlans.strip(),name,description)
