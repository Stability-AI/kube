#!/usr/bin/env python3

import fire

from neo_kube.cluster import ClusterCLI
from neo_kube.job import JobCLI
from neo_kube.utils import assert_binary_on_path
from neo_kube.volume import VolumeCLI


class CLI(object):
    '''
    A CLI for working with Kubernetes clusters on EKS.
    '''

    cluster = ClusterCLI()
    job = JobCLI()
    volume = VolumeCLI()


if __name__ == '__main__':
    assert_binary_on_path('eksctl', 'You must install `eksctl` to use this tool.')
    assert_binary_on_path('kubectl', 'You must install `kubectl` to use this tool.')
    assert_binary_on_path('aws', 'You must install the AWS CLI tool to use this tool.')
    fire.Fire(CLI)
