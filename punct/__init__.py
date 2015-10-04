from __future__ import unicode_literals

import re


class REPLACEMENTS:
    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = '"'
    HYPHEN = '-'
    GRAVE = '`'
    FORWARD_SLASH = '/'
    VERTICAL_BAR = '|'
    EXCLAMATION_POINT = '!'
    CARAT = '^'
    TILDE = '~'
    UNDERSCORE = '_'
    PERCENT = '%'
    COLON = ':'

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
        },
        GRAVE: {
            "\u02cb": "MODIFIER LETTER GRAVE ACCENT",
            "\u0300": "COMBINING GRAVE ACCENT",
            "\u2035": "REVERSED PRIME",
        },
        HYPHEN: {
            "\u00ad": "SOFT HYPHEN",
            "\u2010": "HYPHEN",
            "\u2011": "NON-BREAKING HYPHEN",
            "\u2012": "FIGURE DASH",
            "\u2013": "EN DASH",
            "\u2014": "EM DASH",
            "\u2212": "MINUS SIGN",
        },
        FORWARD_SLASH: {
            "\u00f7": "DIVISION SIGN",
            "\u0338": "COMBINING LONG SOLIDUS OVERLAY",
            "\u2044": "FRACTION SLASH",
            "\u2215": "DIVISION SLASH",
        },
        VERTICAL_BAR: {
            "\u01c0": "LATIN LETTER DENTAL CLICK",
            "\u05c0": "HEBREW PUNCTUATION PASEQ",
            "\u2223": "DIVIDES",
            "\u2758": "LIGHT VERTICAL BAR",
        },
        EXCLAMATION_POINT: {
            "\u01c3": "LATIN LETTER RETROFLEX CLICK",
            "\u2762": "HEAVY EXCLAMATION MARK ORNAMENT",
        },
        CARAT: {
            "\u02c4": "MODIFIER LETTER UP ARROWHEAD",
            "\u02c6": "MODIFIER LETTER CIRCUMFLEX ACCENT",
            "\u0302": "COMBINING CIRCUMFLEX ACCENT",
            "\u2038": "CARET",
            "\u2303": "UP ARROWHEAD",
        },
        TILDE: {
            "\u02dc": "SMALL TILDE",
            "\u0303": "COMBINING TILDE",
            "\u2053": "SWUNG DASH",
            "\u223c": "TILDE OPERATOR",
            "\u301c": "WAVE DASH",
        },
        UNDERSCORE: {
            "\u02cd": "MODIFIER LETTER LOW MACRON",
            "\u0331": "COMBINING MACRON BELOW",
            "\u0332": "COMBINING LOW LINE",
            "\u2017": "DOUBLE LOW LINE",
        },
        PERCENT: {
            "\u066a": "ARABIC PERCENT SIGN",
            "\u2052": "COMMERCIAL MINUS SIGN",
        },
        COLON: {
            "\u0589": "ARMENIAN FULL STOP",
            "\u05c3": "HEBREW PUNCTUATION SOF PASUQ",
            "\u2236": "RATIO",
        }
    }

    @classmethod
    def get_replace_regex(cls, char):
        return "[%s]" % "".join(cls.MAP[char])


def normalize(s, encoding='UTF-8'):
    if not isinstance(s, unicode):
        s = unicode(s, encoding)
    for char in REPLACEMENTS.MAP:
        s = re.sub(REPLACEMENTS.get_replace_regex(char), char, s)
    return s
