#!/usr/bin/env python3
"""this module handles logging for debugging"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    this function returns the log message obfuscated:


    :param: fields: a list of strings representing all fields to obfuscate
    :param: redaction: a string representing by what the field will be obfuscated
    :param: message: a string representing the log line
    :param: separator: a string representing by which character is separating all fields in the log line (message)
    :return: log message obfuscated
    """
    pattern = f"({'|'.join([f'{field}=[^\\{separator}]*' for field in fields])})"
    return re.sub(pattern, lambda x: f"{x.group().split('=')[0]}={redaction}", message)
