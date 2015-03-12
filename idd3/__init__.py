# -*- coding: utf-8 -*-
# IDD3 - Propositional Idea Density from Dependency Trees
# Copyright (C) 2014-2015  Andre Luiz Verucci da Cunha
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

from idd3.base import *


config = Config()
all_transformations = []
all_rulesets = []


def use_language(module):
    """Configure idd3's global variables (config, all_transformations,
        and all_rulesets) using those from module.
    """
    global config, all_transformations, all_rulesets

    for key, value in module.config.items():
        config[key] = value

    while len(all_transformations):
        del all_transformations[0]
    all_transformations.extend(module.all_transformations)

    while len(all_rulesets):
        del all_rulesets[0]
    all_rulesets.extend(module.all_rulesets)


from idd3 import rules
from idd3 import transform
