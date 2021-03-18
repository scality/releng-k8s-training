# Setting up a local K8s cluster

Kubernetes itself is a complicated tool to install and there are hundreds of way of doing it. Even here at Scality we have developed our own Kubernetes distribution, which is called [metalk8s](https://github.com/scality/metalk8s)

However those installation are made for real production environment, and even though they
may work well for a local development environment it is not the quickest/easiest way.


## Install and Configure kubectl

[`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/) is the CLI that will be used to communicate with your Kubernetes cluster.

Install `kubectl` on your computer it will be configured later on so that it can communicate with your Kubernetes cluster.

## Installing your own K8s local cluster

There are various tools that help you install a kubernetes cluster locally.
The one that will be recommended for this exersices is called [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).

Please install kind or any other k8s installation tool that please you and create your own k8s cluster.

## Is it up?

Run some kubectl commands like the following to ensure that your cluster is up and running and that kubectl is configured properly:

```shell
$ kubectl get pods --all-namespaces
$ kubectl get deployment --all-namespaces
$ kubectl get service --all-namespaces
```

We'll see what does command mean afterwards.
