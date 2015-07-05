from __future__ import unicode_literals

import re


class REPLACEMENTS:
    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = '"'

    MAP = {
        SINGLE_QUOTE: {
            "\u00b4": "ACUTE ACCENT",
            "\u02b9": "MODIFIER LETTER PRIME",
            "\u02bc": "MODIFIER LETTER APOSTROPHE",
            "\u02c8": "MODIFIER LETTER VERTICAL LINE",
            "\u0301": "COMBINING ACUTE ACCENT",
            "\u2018": "LEFT SINGLE QUOTATION MARK",
            "\u2019": "RIGHT SINGLE QUOTATION MARK",
            "\u201b": "SINGLE HIGH-REVERSED-9 QUOTATION MARK",
            "\u2032": "PRIME",
        },
        DOUBLE_QUOTE: {
            "\u00ab": "LEFT-POINTING DOUBLE ANGLE QUOTATION MARK",
            "\u00bb": "RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK",
            "\u02ba": "MODIFIER LETTER DOUBLE PRIME",
            "\u030b": "COMBINING DOUBLE ACUTE ACCENT",
            "\u030e": "COMBINING DOUBLE VERTICLE LINE ABOVE",
            "\u201c": "LEFT DOUBLE QUOTATION MARK",
            "\u201d": "RIGHT DOUBLE QUOTATION MARK",
            "\u201e": "DOUBLE LOW-9 QUOTATION MARK",
            "\u201f": "DOUBLE HIGH-REVERSED-9 QUOTATION MARK",
            "\u2033": "DOUBLE PRIME",
            "\u2036": "REVERSED DOUBLE PRIME",
            "\u3003": "DITTO MARK",
            "\u301d": "REVERSED DOUBLE PRIME QUOTATION MARK",
            "\u301e": "DOUBLE PRIME QUOTATION MARK",
        }
    }

    @classmethod
    def get_replace_regex(cls, char):
        return "[%s]" % "".join(cls.MAP[char])


def normalize(s):
    for char in REPLACEMENTS.MAP:
        s = re.sub(REPLACEMENTS.get_replace_regex(char), char, s)
    return s
