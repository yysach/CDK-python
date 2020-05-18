from aws_cdk import (
    aws_sagemaker as sagemaker,
    core
)


class HelloPythonStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # enter your code here
        instance = sagemaker.CfnNotebookInstance(
            scope=self,
            id="My instance",
            instance_type="ml.t2.medium",
            role_arn=self.node.try_get_context("role-arn"),
	        default_code_repository="https://git-codecommit.us-east-1.amazonaws.com/v1/repos/AmazonSageMaker-LinearClassificationRepo",
        )