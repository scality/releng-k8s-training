# Introduction

Kubernetes help us orchestrate containers, so before we start playing with it, we need to build one.

[Docker](https://docker.com) is going to help towards this task.

## Docker build

Create a `Dockerfile` at the root of the repository containing the required instruction to build a Docker image capable of running the flask application. 

You're free to use any OS that please you or base image that may help you in your path.

The following command must build your image successfully:

```shell
$ docker build --tag ghcr.io/scality/releng-k8s-training/k8s-intro:latest .
```

## Docker run

Once we have built our image, let's ensure the Docker image is running the application.

The following commands should be successful and contain the same result:

```shell
$ docker run --rm -p 5000:5000 --name k8s-intro --detach ghcr.io/scality/releng-k8s-training/k8s-intro:latest
$ curl localhost:5000
Hello, World!
```

## Docker push

When running applications in Kubernetes, the first requirement is that our image is hosted on a container registry.

[GitHub docker registry](https://docs.github.com/en/packages/guides/configuring-docker-for-use-with-github-packages)


## Open a PR

Once you're done with all the steps above, open a PR targeting the `main` branch.
