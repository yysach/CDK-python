#!/usr/bin/env python3

from aws_cdk import (
    core
)

from hello_python.hello_python_stack import HelloPythonStack

app = core.App()
HelloPythonStack(app, "HelloPythonStack", env=core.Environment(
    region="us-east-1",
    account="424165949979"))

# MyStack(app, "MyStack", env=core.Environment(
#        region="REGION",
#        account="ACCOUNT"))

app.synth()
