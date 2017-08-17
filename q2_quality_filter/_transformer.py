# ----------------------------------------------------------------------------
# Copyright (c) 2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import pandas as pd

from .plugin_setup import plugin
from ._format import QualityFilterStatsFmt


@plugin.register_transformer
def _1(data: pd.DataFrame) -> QualityFilterStatsFmt:
    ff = QualityFilterStatsFmt()
    data.to_csv(str(ff))
    return ff


@plugin.register_transformer
def _2(ff: QualityFilterStatsFmt) -> pd.DataFrame:
    return pd.read_csv(str(ff), index_col='sample-id')
