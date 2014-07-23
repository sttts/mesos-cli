# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import argcomplete
import json

from . import cli
from .master import current as master

parser = cli.parser(
    description="fetch the json state for either the master or a specific slave"
)

parser.add_argument(
    "slave", nargs="?",
    help="ID of the slave. May match multiple slaves (or all)"
).completer = cli.slave_completer

def main():
    args = cli.init(parser)

    if not args.slave:
        print json.dumps(master.state, indent=4)
    else:
        print json.dumps([s.state for s in master.slaves(args.slave)], indent=4)