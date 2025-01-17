# Ultroid - UserBot
# Copyright (C) 2021-2022 Dr. ugs lab.
#
# This file is a part of < https://github.com/docugs/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/docugs/pyUltroid/blob/main/LICENSE>.

"""
Exceptions which can be raised by py-Ultroid Itself.
"""


class pyUltroidError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyUltroidError):
    ...
