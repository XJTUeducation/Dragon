#include "operators/misc/python_op.h"

#ifdef WITH_PYTHON

#ifdef WITH_PYTHON3
#define PyBytes_FromStringAndSize \
    PyUnicode_FromStringAndSize
#endif

#define Bytes(str) \
    PyBytes_FromStringAndSize(str, string(str).size())

#define CS2Bytes(cstr) Bytes(cstr.c_str())

namespace dragon {

template <class Context>
RunOp<Context>::RunOp(const OperatorDef& def, Workspace* ws)
    : Operator<Context>(def, ws),
      module(OperatorBase::Arg<string>("module", "")),
      op(OperatorBase::Arg<string>("op", "")),
      param_str((OperatorBase::Arg<string>("param_str", ""))) {
    //  optimization for all python ops
    if (!AllowRun()) return; this->do_sync_ = false;

    //  init interpreter & load module
    Py_Initialize();
    PyObject* py_module = PyImport_ImportModule(module.c_str());
    CHECK(py_module) << "\nFail to import py module: " << module;
    PyObject* py_dict = PyModule_GetDict(py_module);
    PyObject* py_op = PyDict_GetItemString(py_dict, op.c_str());
    CHECK(py_op) << "\nFail not import operator: " << op
                 << " from module: " << module;
    self = PyObject_CallObject(py_op, NULL);

    //  wrap inputs and outputs
    inputs = PyList_New(InputSize());
    for (int i = 0; i < InputSize(); i++)
        PyList_SetItem(inputs, i, CS2Bytes(Input(i).name()));
    outputs = PyList_New(OutputSize());
    for (int i = 0; i < OutputSize(); i++)
        PyList_SetItem(outputs, i, CS2Bytes(Output(i)->name()));

    //  backward compatibility: param_str
    PyObject_SetAttr(self, Bytes("param_str"), CS2Bytes(param_str));
    PyObject_SetAttr(self, Bytes("param_str_"), CS2Bytes(param_str));

    //  backward compatibility: self.setup(inputs, outputs)
    if (PyObject_HasAttr(self, Bytes("setup"))) {
        PyObject_CallMethod(self, "setup", "OO", inputs, outputs);
    }
}

template <class Context>
void RunOp<Context>::RunOnDevice() {
    //  reset phase
    PyObject_SetAttr(self, Bytes("phase"), CS2Bytes(phase()));

    //  backward compatibility: reshape(inputs, outputs)
    if (PyObject_HasAttr(self, Bytes("reshape"))) {
        PyObject_CallMethod(self, "reshape", "OO", inputs, outputs);
    }

    //  overloaded run inferfaces
    if (PyObject_HasAttr(self, Bytes("forward"))) {
        PyObject_CallMethod(self, "forward", "OO", inputs, outputs);
    } else if (PyObject_HasAttr(self, Bytes("run"))) {
        PyObject_CallMethod(self, "run", "OO", inputs, outputs);
    }
}

DEPLOY_CPU(Run);
#ifdef WITH_CUDA
DEPLOY_CUDA(Run);
#endif
OPERATOR_SCHEMA(Run);

NO_GRADIENT(Run);

template <class Context>
void TemplateGradientOp<Context>::RunOnDevice() {
    //  reset phase
    PyObject_SetAttr(this->self,
        Bytes("phase"), CS2Bytes(phase()));

    //  backward compatibility: reshape(inputs, outputs)
    if (PyObject_HasAttr(this->self, Bytes("reshape"))) {
        PyObject_CallMethod(this->self, "reshape",
            "OO", this->inputs, this->outputs);
    }

    //  overloaded run inferfaces
    if (PyObject_HasAttr(this->self, Bytes("backward"))) {
        PyObject_CallMethod(this->self, "forward",
            "OO", this->inputs, this->outputs);
    } else if (PyObject_HasAttr(this->self, Bytes("grad"))) {
        PyObject_CallMethod(this->self, "grad",
            "OO", this->inputs, this->outputs);
    }
}

DEPLOY_CPU(Template);
#ifdef WITH_CUDA
DEPLOY_CUDA(Template);
#endif
OPERATOR_SCHEMA(Template);

DEPLOY_CPU(TemplateGradient);
#ifdef WITH_CUDA
DEPLOY_CUDA(TemplateGradient);
#endif
OPERATOR_SCHEMA(TemplateGradient);

class GetTemplateGradient final : public GradientMakerBase {
 public:
    GRADIENT_MAKER_CTOR(GetTemplateGradient);
    vector<OperatorDef> MakeDefs() override {
        vector<string> inputs, outputs;
        for (auto input : def.input()) inputs.push_back(input);
        for (int i = 0; i < def.output_size(); i++) inputs.push_back(GO(i));
        for (int i = 0; i < def.input_size(); i++) outputs.push_back(GI(i));
        return SingleDef(def.type() + "Gradient", "", inputs, outputs);
    }
};
REGISTER_GRADIENT(Template, GetTemplateGradient);

}    // namespace dragon

#endif    // WITH_PYTHON