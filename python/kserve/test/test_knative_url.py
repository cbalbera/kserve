# Copyright 2021 The KServe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    KServe

    Python SDK for KServe  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kserve
from kserve.models.knative_url import KnativeURL  # noqa: E501
from kserve.rest import ApiException


class TestKnativeURL(unittest.TestCase):
    """KnativeURL unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testKnativeURL(self):
        """Test KnativeURL"""
        # FIXME: construct object with mandatory attributes with example values
        # model = kserve.models.knative_url.KnativeURL()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
