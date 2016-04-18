import os
import re
import logging
from exceptions import ExtensionError

class Base(object):

    """Base Class"""
    pass


class WithExtensionUnderGivenDirectory(Base):
    """
    List all files under the given directory 
    which have the given extension
    """
    def __init__(self, extension, dir):
        self.extension = extension
        self.dir = dir

    def withExtension(self):
        try:
            if self.extension.startswith('.'):
                for file in os.listdir(self.dir):
                    if file.endswith(self.extension):
                        print(file)
                    else:
                        pass
            else:
                raise ExtensionError('Invalid Extension, Enter correct extension')
        except ExtensionError as err:
            logging.exception(err.message)


class WithFileNameUnderGivenDirectory(Base):
    """
    List all files under the given directory 
    which have the given filename
    """
    def __init__(self, filename, dir):
        self.filename = filename
        self.dir = dir

    def withFilename(self):
        for file in os.listdir(self.dir):
            if self.filename == file:
                print(file)

class WithPatterUnderGivenDirectory(Base):
    """
    List all the files under the given directory
    which match the given pattern
    """
    def __init__(self, pattern, dir):
        self.pattern = pattern
        self.dir = dir

    def withPattern(self):
       for file in os.listdir(self.dir):
           if re.search(self.pattern, file):
               print(file)
