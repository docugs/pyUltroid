# Ultroid - UserBot
# Copyright (C) 2021-2022 Dr. ugs lab.
#
# This file is a part of < https://github.com/docugs/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/docugs/pyUltroid/blob/main/LICENSE>.

from .. import udB


def get_logger():
    return udB.get_key("LOGUSERS") or []


def is_logger(id_):
    return id_ in get_logger()


def log_user(id_):
    pmperm = get_logger()
    pmperm.append(id_)
    return udB.set_key("LOGUSERS", pmperm)


def nolog_user(id_):
    pmperm = get_logger()
    pmperm.remove(id_)
    return udB.set_key("LOGUSERS", pmperm)
