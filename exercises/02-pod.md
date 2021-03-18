# Creating your first Kubernetes Object

In this exercise we will learn how to translate a `docker run` command into the K8s world.

## Creating your first Pod

Pod is the smallest resource available in Kubernetes. It's easy to translate it as a `docker run` but it does much more than just a docker run. Please read [the documentation about pods] to have the official explanation. 

In this exercise you will create `manifest/pod.yaml` file that will run the flask app.
You can check the [pod] object specification to help you towards your task.

The pod will have the following specification:
* It will be named `k8s-intro`
* It will contain the label `app: k8s-intro`
* It will contain one container named `k8s-intro` and run the image we just built.
* The container `k8s-intro` will have a port spec named `http` that targets the port `5000` over `TCP`.


The pod will be created like the following:

```shell
# From the root of the repository
$ kubectl apply -f manifest
# check that your pod is running
$ kubectl get pods
# Ensure that the label selector is working
# this command should show you your k8s-intro
$ kubectl get pods -l app=k8s-intro
# Forward the connection to the pod in your computer to speak to it
$ kubectl port-forward k8s-intro 5000:5000
# In another shell the following command output must be the same as shown
$ curl localhost:5000
Hello, World!
# Delete your pod
$ kubectl delete -f manifest
```


[the documentation about pods]: https://kubernetes.io/docs/concepts/workloads/pods/
[pod]: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#pod-v1-core
