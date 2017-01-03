#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import unittest
import json


sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import cpe_utils


class TestBasic(unittest.TestCase):
    """Test the basic functionality of cpe_utils
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cpe_parsing(self):
        cpe_str = "cpe:/part:vendor:product:version:update:edition"
        cpe_obj = cpe_utils.CPE(cpe_str)

        self.assertEqual(cpe_obj.part, "part")
        self.assertEqual(cpe_obj.vendor, "vendor")
        self.assertEqual(cpe_obj.product, "product")
        self.assertEqual(cpe_obj.version, "version")
        self.assertEqual(cpe_obj.update, "update")
        self.assertEqual(cpe_obj.edition, "edition")

        # see issue #5
        # TODO Test vendor
        # TODO Test product
        # TODO Test version
        # TODO Test update
        # TODO Test edition

    def test_matches(self):
        tests = [
            ["cpe:/a:vendor:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            
            
            ["cpe:/X:vendor:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:X:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:X:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:X:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.1:X:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.1:sp3:X", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            
            ["cpe:/a:vandor:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:ndor:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:dor:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:or:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:r:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vbndo:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vand:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:ven:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:ve:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:v:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vbndor:produc:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:produ:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vcndor:prod:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vindor:pro:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vondor:pr:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vundor:p:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vondor::1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.0:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product::sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:1.1:sp:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.1:s:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.1::x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:1.1:sp3:x8", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.1:sp3:x", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.1:sp3:", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vndor:poduct:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vedor:prduct:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:venor:prouct:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendr:prodct:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendo:produt:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:produc:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:space:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            
            
            ["cpe:/a:vendor:space:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.10:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.11:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.12:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.13:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.14:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.15:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.16:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.17:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.18:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            ["cpe:/a:vendor:product:1.19:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", False],
            
            
            
            ["cpe:/a:vendor:product:1.1:sp3:*", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:1.1:*:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:*:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:*:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:*:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            
            
            ["cpe:/*:vendor:product:1.1:sp3:x8?", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:1.1:sp3:x?6", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:1.1:sp3:?86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:1.1:sp?:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:1.1:s?3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:1.1:?p3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:1.?:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:1?1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:product:?.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:produc?:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:produ?t:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:prod?ct:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:pro?uct:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:pr?duct:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:p?oduct:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendor:?roduct:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vendo?:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:vend?r:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:ven?or:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:ve?dor:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:v?ndor:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/a:?endor:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],
            ["cpe:/?:vendor:product:1.1:sp3:x86", "cpe:/a:vendor:product:1.1:sp3:x86", True],

            
            
        ]
        
        count = 0
        for test_info in tests:
            count += 1
            cpe_str1, cpe_str2, match_result = test_info
            cpe1 = cpe_utils.CPE(cpe_str1)
            cpe2 = cpe_utils.CPE(cpe_str2)
            
            self.assertTrue(cpe1.matches(cpe2) == match_result, "[{}] {}.match({}) was not {}".format(
                count,
                cpe_str1,
                cpe_str2,
                match_result
            ))

    def test_cpe_parsing_23(self):
        cpe_str = "cpe:2.3:o:vendor:product:version:update:edition"

        cpe_obj = cpe_utils.CPE(cpe_str)

        self.assertEqual(cpe_obj.part, "o")
        self.assertEqual(cpe_obj.vendor, "vendor")
        self.assertEqual(cpe_obj.product, "product")
        self.assertEqual(cpe_obj.version, "version")
        self.assertEqual(cpe_obj.update, "update")
        self.assertEqual(cpe_obj.edition, "edition")

        # see issue #5
        # TODO Test vendor
        # TODO Test product
        # TODO Test version
        # TODO Test update
        # TODO Test edition

    def test_cpe_exception(self):
        with self.assertRaises(cpe_utils.CPEException):
            cpe_utils.CPE("cpe:::::")

    def test_human(self):
        tests = [
            ["cpe:/"
             "a:vendor:product:1.1:sp3:x86", "Vendor Product 1.1 SP3 x86"],
            ["cpe:/a:vendor_name:product:1.1:sp3:x86", "Vendor Name Product 1.1 SP3 x86"],
            ["cpe:/a:vendor:product::sp3:x86", "Vendor Product SP3 x86"],
            ["cpe:/a:vendor:::sp3:x86", "Vendor SP3 x86"],
            ["cpe:/a:vendor::::", "Vendor"],
            ["cpe:/a::::sp3:x86", "SP3 x86"],
            ["cpe:/a:vendor:product:1.1::", "Vendor Product 1.1"],
            ["cpe:/a:::::", ""],
            ["cpe:/a::product:::", "Product"],
            ["cpe:/a:::1.1::", "1.1"],
            ["cpe:/a::::sp3:", "SP3"],
            ["cpe:/a:::::x86", "x86"],
            ["cpe:/a:vendor:product:::", "Vendor Product"],
            ["cpe:/a:vendor:product:1.1:sp3:", "Vendor Product 1.1 SP3"],
            ["cpe:/a:vendor_name::::x86", "Vendor Name x86"],
            ["cpe:/a:vendor_name:::sp3:", "Vendor Name SP3"],
            ["cpe:/a:vendor_name:product:1.1::", "Vendor Name Product 1.1"],
            ["cpe:/a:vendor_name::::", "Vendor Name"],
            ["cpe:/a:vendor::::x86", "Vendor x86"],
            ["cpe:/a:vendor:::sp3:", "Vendor SP3"],
        ]

        for test_info in tests:
            cpe_string = test_info[0]
            correct_human = test_info[1]

            cpe = cpe_utils.CPE(cpe_string)
            self.assertEqual(cpe.human(), correct_human, "{!r} was not {!r} (for cpe {})".format(
                cpe.human(),
                correct_human,
                cpe_string
            ))

    def test_to_json(self):

        tests = [
            ["cpe:/a:vendor:product:1.1:sp3:x86",{
                "part": "a",
                "vendor": "vendor",
                "product": "product",
                "version": "1.1",
                "update": "sp3",
                "edition": "x86"
            }],
            ["cpe:/a::product:1.1:sp3:x86",{
                "part": "a",
                "vendor": "",
                "product": "product",
                "version": "1.1",
                "update": "sp3",
                "edition": "x86"
            }],
            ["cpe:/a:vendor::1.1:sp3:x86",{
                "part": "a",
                "vendor": "vendor",
                "product": "",
                "version": "1.1",
                "update": "sp3",
                "edition": "x86"
            }],
            ["cpe:/a:vendor:product::sp3:x86",{
                "part": "a",
                "vendor": "vendor",
                "product": "product",
                "version": "",
                "update": "sp3",
                "edition": "x86"
            }],
            ["cpe:/a:vendor:product:1.1::x86",{
                "part": "a",
                "vendor": "vendor",
                "product": "product",
                "version": "1.1",
                "update": "",
                "edition": "x86"
            }],
            ["cpe:/a:vendor:product:1.1:sp3",{
                "part": "a",
                "vendor": "vendor",
                "product": "product",
                "version": "1.1",
                "update": "sp3",
                "edition": ""

            }],

        ]


        for test_info in tests:
            cpe_string = test_info[0]
            correct_dict = test_info[1]

            cpe = cpe_utils.CPE(cpe_string)
            assert isinstance(cpe_string, object)
            self.assertEqual(cpe.to_json(), json.dumps(correct_dict), "{!r} was not {!r} (for cpe {})".format(
                cpe.to_json(),
                correct_dict,
                cpe_string
            ))

    def test_cpe_obj_equals(self):
        orig_cpe = "cpe:/o:vendor:product:version:update:edition"
        cpe_obj1 = cpe_utils.CPE(orig_cpe)
        cpe_obj2 = cpe_utils.CPE(orig_cpe)

        false_cpes = [
            "cpe:/a:vendor:product:version:update:edition",
            "cpe:/o:vendor1:product:version:update:edition",
            "cpe:/o:vendor:product1:version:update:edition",
            "cpe:/o:vendor:product:version1:update:edition",
            "cpe:/o:vendor:product:version:update1:edition",
            "cpe:/o:vendor:product:version:update:edition1",
        ]

        for false_cpe in false_cpes:
            false_cpe_obj = cpe_utils.CPE(false_cpe)
            self.assertFalse(cpe_obj1 == false_cpe_obj, "{} is not equal to {}".format(
                false_cpe,
                orig_cpe
            ))

    def test_has_wildcards(self):
        cpe_tests = [
            "cpe:/*:vendor:product:version:update:edition",
            "cpe:/?:vendor:product:version:update:edition",
            "cpe:/o:v*ndor:product:version:update:edition",
            "cpe:/o:v?ndor:product:version:update:edition",
            "cpe:/o:vendor:pr*duct:version:update:edition",
            "cpe:/o:vendor:pr?duct:version:update:edition",
            "cpe:/o:vendor:product:vers*on:update:edition",
            "cpe:/o:vendor:product:vers?on:update:edition",
            "cpe:/o:vendor:product:version:upda*e:edition",
            "cpe:/o:vendor:product:version:upda?e:edition",
            "cpe:/o:vendor:product:version:update:ed*tion",
            "cpe:/o:vendor:product:version:update:ed?tion",
        ]

        for cpe_str in cpe_tests:
            cpe_obj = cpe_utils.CPE(cpe_str)
            self.assertTrue(cpe_obj.has_wildcards())

        no_wildcards = cpe_utils.CPE("cpe:/o:vendor:product:version:update:edition")
        self.assertFalse(no_wildcards.has_wildcards())


if __name__ == "__main__":
    unittest.main()
