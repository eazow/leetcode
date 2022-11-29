import importlib


def import_class(file_name, class_name):
    return getattr(importlib.import_module(file_name), class_name)
