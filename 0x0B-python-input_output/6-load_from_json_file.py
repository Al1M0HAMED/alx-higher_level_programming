#!/usr/bin/python3
"""
Author: Ali Mohamed
Date: 16/11/2025
"""
import json


def load_from_json_file(filename):
    """Writes a Python object to a text file using JSON representation."""
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
