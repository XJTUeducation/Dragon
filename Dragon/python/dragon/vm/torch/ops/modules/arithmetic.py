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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from dragon.vm.torch.ops.modules.base import BaseModule


class Fundamental(BaseModule):
    def __init__(self, key, ctx, **kwargs):
        super(Fundamental, self).__init__(key, ctx, **kwargs)
        self.op_type = kwargs.get('op_type', 'Add')
        self.register_arguments()
        self.register_op()

    def register_arguments(self):
        """No arguments for fundamental ops."""
        pass

    def register_op(self):
        self.op_meta = {
            'op_type': self.op_type,
            'n_inputs': 2, 'n_outputs': 1,
            'arguments': {}
        }

    def forward(self, x1, x2, y):
        inputs = [x1, x2]; self.unify_devices(inputs)
        outputs = [y] if y else [self.register_output(x1.dtype)]
        return self.run(inputs, outputs)


class Maximum(BaseModule):
    def __init__(self, key, ctx, **kwargs):
        super(Maximum, self).__init__(key, ctx, **kwargs)
        self.register_arguments()
        self.register_op()

    def register_arguments(self):
        """No arguments for minimum op."""
        pass

    def register_op(self):
        self.op_meta = {
            'op_type': 'Maximum',
            'n_inputs': 2, 'n_outputs': 1,
            'arguments': {}
        }

    def forward(self, x1, x2, y, dtype):
        inputs = [x1, x2]; self.unify_devices(inputs)
        outputs = [y] if y else [self.register_output(dtype)]
        return self.run(inputs, outputs)


class Minimum(BaseModule):
    def __init__(self, key, ctx, **kwargs):
        super(Minimum, self).__init__(key, ctx, **kwargs)
        self.register_arguments()
        self.register_op()

    def register_arguments(self):
        """No arguments for minimum op."""
        pass

    def register_op(self):
        self.op_meta = {
            'op_type': 'Minimum',
            'n_inputs': 2, 'n_outputs': 1,
            'arguments': {}
        }

    def forward(self, x1, x2, y, dtype):
        inputs = [x1, x2]; self.unify_devices(inputs)
        outputs = [y] if y else [self.register_output(dtype)]
        return self.run(inputs, outputs)


class Clamp(BaseModule):
    def __init__(self, key, ctx, **kwargs):
        super(Clamp, self).__init__(key, ctx, **kwargs)
        self.min = kwargs.get('min', None)
        self.max = kwargs.get('max', None)
        if self.min is not None: self.min = float(self.min)
        if self.max is not None: self.max = float(self.max)
        self.register_arguments()
        self.register_op()

    def register_arguments(self):
        """No arguments clamp op."""
        pass

    def register_op(self):
        self.op_meta = {
            'op_type': 'Clip',
            'n_inputs': 1, 'n_outputs': 1,
            'arguments': {
                'low': self.min,
                'high': self.max,
            }
        }

    def forward(self, x, y):
        inputs = [x]; self.unify_devices(inputs)
        outputs = [y] if y else [self.register_output(x.dtype)]
        return self.run(inputs, outputs)


class Log(BaseModule):
    def __init__(self, key, ctx, **kwargs):
        super(Log, self).__init__(key, ctx, **kwargs)
        self.register_arguments()
        self.register_op()

    def register_arguments(self):
        """No arguments for Log op."""
        pass

    def register_op(self):
        self.op_meta = {
            'op_type': 'Log',
            'n_inputs': 1, 'n_outputs': 1,
            'arguments': {}
        }

    def forward(self, x, y):
        inputs = [x]; self.unify_devices(inputs)
        outputs = [y] if y else [self.register_output(x.dtype)]
        return self.run(inputs, outputs)


class Exp(BaseModule):
    def __init__(self, key, ctx, **kwargs):
        super(Exp, self).__init__(key, ctx, **kwargs)
        self.register_arguments()
        self.register_op()

    def register_arguments(self):
        """No arguments for Log op."""
        pass

    def register_op(self):
        self.op_meta = {
            'op_type': 'Exp',
            'n_inputs': 1, 'n_outputs': 1,
            'arguments': {}
        }

    def forward(self, x, y):
        inputs = [x]; self.unify_devices(inputs)
        outputs = [y] if y else [self.register_output(x.dtype)]
        return self.run(inputs, outputs)