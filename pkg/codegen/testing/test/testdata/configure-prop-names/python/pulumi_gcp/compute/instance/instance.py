# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ... import compute as _compute

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 boot_disk: pulumi.Input['_compute.instancebootdisk.InstanceBootDiskArgs']):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input['_compute.instancebootdisk.InstanceBootDiskArgs'] boot_disk: The boot disk for the instance.
               Structure is documented below.
        """
        InstanceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            boot_disk=boot_disk,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             boot_disk: Optional[pulumi.Input['_compute.instancebootdisk.InstanceBootDiskArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if boot_disk is None and 'bootDisk' in kwargs:
            boot_disk = kwargs['bootDisk']
        if boot_disk is None:
            raise TypeError("Missing 'boot_disk' argument")

        _setter("boot_disk", boot_disk)

    @property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> pulumi.Input['_compute.instancebootdisk.InstanceBootDiskArgs']:
        """
        The boot disk for the instance.
        Structure is documented below.
        """
        return pulumi.get(self, "boot_disk")

    @boot_disk.setter
    def boot_disk(self, value: pulumi.Input['_compute.instancebootdisk.InstanceBootDiskArgs']):
        pulumi.set(self, "boot_disk", value)


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *,
                 boot_disk: Optional[pulumi.Input['_compute.instancebootdisk.InstanceBootDiskArgs']] = None):
        """
        Input properties used for looking up and filtering Instance resources.
        :param pulumi.Input['_compute.instancebootdisk.InstanceBootDiskArgs'] boot_disk: The boot disk for the instance.
               Structure is documented below.
        """
        _InstanceState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            boot_disk=boot_disk,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             boot_disk: Optional[pulumi.Input['_compute.instancebootdisk.InstanceBootDiskArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if boot_disk is None and 'bootDisk' in kwargs:
            boot_disk = kwargs['bootDisk']

        if boot_disk is not None:
            _setter("boot_disk", boot_disk)

    @property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> Optional[pulumi.Input['_compute.instancebootdisk.InstanceBootDiskArgs']]:
        """
        The boot disk for the instance.
        Structure is documented below.
        """
        return pulumi.get(self, "boot_disk")

    @boot_disk.setter
    def boot_disk(self, value: Optional[pulumi.Input['_compute.instancebootdisk.InstanceBootDiskArgs']]):
        pulumi.set(self, "boot_disk", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 boot_disk: Optional[pulumi.Input[pulumi.InputType['_compute.instancebootdisk.InstanceBootDiskArgs']]] = None,
                 __props__=None):
        """
        A mock of an instance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['_compute.instancebootdisk.InstanceBootDiskArgs']] boot_disk: The boot disk for the instance.
               Structure is documented below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A mock of an instance.

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            InstanceArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 boot_disk: Optional[pulumi.Input[pulumi.InputType['_compute.instancebootdisk.InstanceBootDiskArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceArgs.__new__(InstanceArgs)

            if boot_disk is not None and not isinstance(boot_disk, _compute.instancebootdisk.InstanceBootDiskArgs):
                boot_disk = boot_disk or {}
                def _setter(key, value):
                    boot_disk[key] = value
                _compute.instancebootdisk.InstanceBootDiskArgs._configure(_setter, **boot_disk)
            if boot_disk is None and not opts.urn:
                raise TypeError("Missing required property 'boot_disk'")
            __props__.__dict__["boot_disk"] = boot_disk
        super(Instance, __self__).__init__(
            'gcp:compute/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            boot_disk: Optional[pulumi.Input[pulumi.InputType['_compute.instancebootdisk.InstanceBootDiskArgs']]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['_compute.instancebootdisk.InstanceBootDiskArgs']] boot_disk: The boot disk for the instance.
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceState.__new__(_InstanceState)

        __props__.__dict__["boot_disk"] = boot_disk
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> pulumi.Output['_compute.instancebootdisk.outputs.InstanceBootDisk']:
        """
        The boot disk for the instance.
        Structure is documented below.
        """
        return pulumi.get(self, "boot_disk")

