"""
Copyright 2019 NerdWallet

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


from .objects import (  # noqa
    Data,  # noqa
    DuplicateKey,  # noqa
    Module,  # noqa
    OrderedDict,  # noqa
    Output,  # noqa
    Provider,  # noqa
    Resource,  # noqa
    Terraform,  # noqa
    TFObject,  # noqa
    Variable,  # noqa
)  # noqa
from .resource_collections import ResourceCollection, Variant  # noqa

# add a couple shortcuts
compile = TFObject.compile  # pylint: disable=redefined-builtin
reset = TFObject.reset