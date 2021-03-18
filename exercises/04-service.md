# Kubernetes Services

Service are the objects in Kubernetes that will allow us to expose our pods and loadbalance the traffic inside our cluster.

Allowing other pods in the cluster to communicate with your pods.

## Creating your first Service

Familiarize yourself with the [service documentation]

Create a file named `manifest/service.yaml`

The service you will create will have the following spec:
* It will be named `k8s-intro`
* It will redirect the traffic on the `k8s-intro` pods
* It will target the port `5000` and listen on the port `5000`

Those command and outputs should be the same

```shell
# This command should now create the service and the deployment
$ kubectl apply -f manifest
# Forward the connection from the service to your computer
$ kubectl port-forward service/k8s-intro 5000:5000
# In another shell the following command output must be the same as shown
$ curl localhost:5000
Hello, World!
```

## Automate it!

Automate the commands above in GitHub actions

[service documentation]: https://kubernetes.io/docs/concepts/services-networking/service/
