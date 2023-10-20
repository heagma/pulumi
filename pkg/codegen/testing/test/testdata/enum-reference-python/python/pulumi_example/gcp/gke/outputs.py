# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
import pulumi_google_native

__all__ = [
    'NodePoolAutoscaling',
]

@pulumi.output_type
class NodePoolAutoscaling(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "locationPolicy":
            suggest = "location_policy"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NodePoolAutoscaling. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NodePoolAutoscaling.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NodePoolAutoscaling.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 location_policy: Optional['pulumi_google_native.container.v1.NodePoolAutoscalingLocationPolicy'] = None):
        """
        :param 'pulumi_google_native.container.v1.NodePoolAutoscalingLocationPolicy' location_policy: Location policy used when scaling up a nodepool.
        """
        NodePoolAutoscaling._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            location_policy=location_policy,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             location_policy: Optional['pulumi_google_native.container.v1.NodePoolAutoscalingLocationPolicy'] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if location_policy is None and 'locationPolicy' in kwargs:
            location_policy = kwargs['locationPolicy']

        if location_policy is not None:
            _setter("location_policy", location_policy)

    @property
    @pulumi.getter(name="locationPolicy")
    def location_policy(self) -> Optional['pulumi_google_native.container.v1.NodePoolAutoscalingLocationPolicy']:
        """
        Location policy used when scaling up a nodepool.
        """
        return pulumi.get(self, "location_policy")


