# ------------------------------------------------------------
# Copyright (c) 2017-present, SeetaTech, Co.,Ltd.
#
# Licensed under the BSD 2-Clause License.
# You should have received a copy of the BSD 2-Clause License
# along with the software. If not, See,
#
#      <https://opensource.org/licenses/BSD-2-Clause>
#
# ------------------------------------------------------------

"""We move the Module & Parameter to ``torch`` instead of ``torch.nn``,
as it will be reused by the ``torch.ops``.

"""

from dragon.vm.torch.module import Module
from dragon.vm.torch.tensor import Parameter
from .modules.conv import Conv2d
from .modules.pooling import MaxPool2d, AvgPool2d
from .modules.activation import ReLU
from .modules.linear import Linear
from .modules.loss import CrossEntropyLoss
from .modules.batchnorm import BatchNorm1d, BatchNorm2d, BatchNorm3d
from . import init