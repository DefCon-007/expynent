# RegEx pattern for matching zip code.
ZIP_CODE = {
    "US": r"\d{5}([ \-]\d{4})?",
    "DE": r"\d{5}",
    "JP": r"\d{3}-\d{4}",
    "FR": r"\d{2}[ ]?\d{3}",
    "AU": r"\d{4}",
    "IT": r"\d{5}",
    "CH": r"\d{4}",
    "AT": r"\d{4}",
    "ES": r"\d{5}",
    "NL": r"\d{4}[ ]?[A-Z]{2}",
    "BE": r"\d{4}",
    "DK": r"\d{4}",
    "SE": r"\d{3}[ ]?\d{2}",
    "NO": r"\d{4}",
    "BR": r"\d{5}[\-]?\d{3}",
    "PT": r"\d{4}([\-]\d{3})?",
    "FI": r"\d{5}",
    "AX": r"22\d{3}",
    "KR": r"\d{3}[\-]\d{3}",
    "CN": r"\d{6}",
    "TW": r"\d{3}(\d{2})?",
    "SG": r"\d{6}",
    "DZ": r"\d{5}",
    "AD": r"AD\d{3}",
    "AR": r"([A-HJ-NP-Z])?\d{4}([A-Z]{3})?",
    "AM": r"(37)?\d{4}",
    "AZ": r"\d{4}",
    "BH": r"((1[0-2]|[2-9])\d{2})?",
    "BD": r"\d{4}",
    "BB": r"(BB\d{5})?",
    "BY": r"\d{6}",
    "BM": r"[A-Z]{2}[ ]?[A-Z0-9]{2}",
    "BA": r"\d{5}",
    "IO": r"BBND 1ZZ",
    "BN": r"[A-Z]{2}[ ]?\d{4}",
    "BG": r"\d{4}",
    "KH": r"\d{5}",
    "CV": r"\d{4}",
    "CL": r"\d{7}",
    "CR": r"\d{4,5}|\d{3}-\d{4}",
    "HR": r"\d{5}",
    "CY": r"\d{4}",
    "CZ": r"\d{3}[ ]?\d{2}",
    "DO": r"\d{5}",
    "EC": r"([A-Z]\d{4}[A-Z]|(?:[A-Z]{2})?\d{6})?",
    "EG": r"\d{5}",
    "EE": r"\d{5}",
    "FO": r"\d{3}",
    "GE": r"\d{4}",
    "GR": r"\d{3}[ ]?\d{2}",
    "GL": r"39\d{2}",
    "GT": r"\d{5}",
    "HT": r"\d{4}",
    "HN": r"(?:\d{5})?",
    "HU": r"\d{4}",
    "IS": r"\d{3}",
    "IN": r"\d{6}",
    "ID": r"\d{5}",
    "IL": r"\d{5}",
    "JO": r"\d{5}",
    "KZ": r"\d{6}",
    "KE": r"\d{5}",
    "KW": r"\d{5}",
    "LA": r"\d{5}",
    "LV": r"\d{4}",
    "LT": r"\d{5}",
    "LU": r"\d{4}",
    "MK": r"\d{4}",
    "MY": r"\d{5}",
    "MV": r"\d{5}",
    "MT": r"[A-Z]{3}[ ]?\d{2,4}",
    "MU": r"(\d{3}[A-Z]{2}\d{3})?",
    "MX": r"\d{5}",
    "MD": r"\d{4}",
    "MC": r"980\d{2}",
    "MA": r"\d{5}",
    "NP": r"\d{5}",
    "NZ": r"\d{4}",
    "NI": r"((\d{4}-)?\d{3}-\d{3}(-\d{1})?)?",
    "NG": r"(\d{6})?",
    "OM": r"(PC )?\d{3}",
    "PK": r"\d{5}",
    "PY": r"\d{4}",
    "PH": r"\d{4}",
    "PL": r"\d{2}-\d{3}",
    "PR": r"00[679]\d{2}([ \-]\d{4})?",
    "RO": r"\d{6}",
    "RU": r"\d{6}",
    "SM": r"4789\d",
    "SA": r"\d{5}",
    "SN": r"\d{5}",
    "SK": r"\d{3}[ ]?\d{2}",
    "SI": r"\d{4}",
    "ZA": r"\d{4}",
    "LK": r"\d{5}",
    "TJ": r"\d{6}",
    "TH": r"\d{5}",
    "TN": r"\d{4}",
    "TR": r"\d{5}",
    "TM": r"\d{6}",
    "UA": r"\d{5}",
    "UY": r"\d{5}",
    "UZ": r"\d{6}",
    "VA": r"00120",
    "VE": r"\d{4}",
    "ZM": r"\d{5}",
    "AS": r"96799",
    "CC": r"6799",
    "CK": r"\d{4}",
    "RS": r"\d{6}",
    "ME": r"8\d{4}",
    "CS": r"\d{5}",
    "YU": r"\d{5}",
    "CX": r"6798",
    "ET": r"\d{4}",
    "NF": r"2899",
    "GF": r"9[78]3\d{2}",
    "GN": r"\d{3}",
    "GP": r"9[78][01]\d{2}",
    "GS": r"SIQQ 1ZZ",
    "GW": r"\d{4}",
    "HM": r"\d{4}",
    "IQ": r"\d{5}",
    "KG": r"\d{6}",
    "LR": r"\d{4}",
    "LS": r"\d{3}",
    "MG": r"\d{3}",
    "MN": r"\d{6}",
    "MQ": r"9[78]2\d{2}",
    "NC": r"988\d{2}",
    "NE": r"\d{4}",
    "PF": r"987\d{2}",
    "PG": r"\d{3}",
    "PM": r"9[78]5\d{2}",
    "PN": r"PCRN 1ZZ",
    "PW": r"96940",
    "RE": r"9[78]4\d{2}",
    "SH": r"(ASCN|STHL) 1ZZ",
    "SJ": r"\d{4}",
    "SO": r"\d{5}",
    "SZ": r"[HLMS]\d{3}",
    "TC": r"TKCA 1ZZ",
    "WF": r"986\d{2}",
    "XK": r"\d{5}",
    "YT": r"976\d{2}"
}

# RegEx pattern for matching email.
EMAIL = r'([\w\.-]+)@([\w\.-]+)'

# RegEx pattern for matching URL.
URL = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|' \
      r'[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

# RegEx pattern for matching credit card.
CREDIT_CARD = '[\d]+((-|\s)?[\d]+)+'

# RegEx pattern for matching IPv4 and IPv6 addresses.
IP_V4 = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
IP_V6 = r"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:| \
([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}| \
([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}| \
([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}| \
([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}| \
([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}| \
[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})| \
:((:[0-9a-fA-F]{1,4}){1,7}|:)| \
fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}| \
::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]| \
1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]| \
1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]| \
1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"

# RegEx pattern for matching MAC-address.
MAC_ADDRESS = r'^([0-9A-Fa-f]{2}[:-]){5}' \
              r'([0-9A-Fa-f]{2})$'

# RegEx pattern for matching username.
USERNAME = r'^[a-zA-Z0-9_.-]+$'

# RegEx pattern for matching uppercase letters.
UPPERCASE = r'[A-Z]+$'


def file_extension(ext=''):
    """
    Return the regex pattern for file extension.

    :param ext: Extension of the file.
    :return: Regex pattern.
    """
    pattern = r'([-\w]+\.(?:%s))' % ext
    return pattern


def password(mi=6, mx=18):
    """
    Return the regex pattern for password

    :param mi: Minimal length of password.
    :param mx: Maximum length of password.
    :return:
    """
    pattern = r'/^[a-z0-9_-]{%s,%s}$/' % (mi, mx)
    return pattern
