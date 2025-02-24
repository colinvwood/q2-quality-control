# ----------------------------------------------------------------------------
# Copyright (c) 2016-2025, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import SemanticType, model
from q2_types.feature_data import FeatureData


# defines types for DecontamScore
DecontamScore = SemanticType('DecontamScore',
                             variant_of=FeatureData.field['type'])


class DecontamScoreFormat(model.TextFileFormat):
    def _validate_(self, level='max'):
        pass


DecontamScoreDirFmt = model.SingleFileDirectoryFormat(
    'DecontamScoreDirFmt', 'stats.tsv', DecontamScoreFormat)
