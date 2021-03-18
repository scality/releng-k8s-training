# Kubernetes Deployment

During the previous exercise we learned to create a Pod object. After playing with it
we can see where there's a lack of feature in the Pod object if we want to actually deploy
an application in production.

That's where the Deployment object comes up handy. We are going to leave the handling of the Pod object to the Deployment. Controlling the pods through Deployment.

## Creating a deployment

Familiarize yourself with the documentation of [Kubernetes deployments]

rename the file `manifest/pod.yaml` you previously created to `manifest/deployment.yaml` and translate the content of it, in a `Deployment`.

The deployment will contain the following specification:
* It will be named `k8s-intro`
* It will contain the label `app: k8s-intro`
* It will contain all the specs from the previously created Pod
* It will contain 3 replicas

```shell
# From the root of the repository
$ kubectl apply -f manifest
# check that your pods are running
# And that you have 3 of them up
$ kubectl get pods -l app=k8s-intro
# Ensure that the label selector is working
# this command should show you your k8s-intro deployment
$ kubectl get deployment -l app=k8s-intro
# Delete all pods and check if they're all re created
$ kubectl delete pod -l app=k8s-intro
```


[Kubernetes deployments]: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

