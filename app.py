#!/usr/bin/env python3

from aws_cdk import core

from hello_python.hello_python_stack import HelloPythonStack


app = core.App()
HelloPythonStack(app, "hello-python")

app.synth()
