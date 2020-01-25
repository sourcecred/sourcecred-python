"""

SourceCred Python is dual-licensed under the MIT License and the Apache-2
License. See LICENSE-MIT and LICENSE-APACHE provided with the code
for the terms of these licenses.

"""

__version__ = "0.0.0"
AUTHOR = "Vanessa Sochat"
AUTHOR_EMAIL = "vsochat@stanford.edu"
NAME = "sourcecred"
PACKAGE_URL = "http://www.github.com/sourcecred/sourcecred-python"
KEYWORDS = "cred, grain, open-source, contributions, graph"
DESCRIPTION = "Python implementation of sourcecred"
LICENSE = "LICENSE"

################################################################################
# Requirements

INSTALL_REQUIRES = (("numpy", {"min_version": "1.16.2"}),)
TESTS_REQUIRES = (("pytest", {"min_version": "4.6.2"}),)

INSTALL_REQUIRES_ALL = INSTALL_REQUIRES
