# Install Minikube

### guide
https://minikube.sigs.k8s.io/docs/start/

### path
/opt/homebrew/bin/minikube 


# Basic Kubernetes 

### namespace
kubectl create namespace dgk

kubectl get namespace


### create pod
kubectl create -f tutorial/hellow.yml


### check created pod
kubectl get pod


### check detail
kubectl describe pod hellow.com


### create service of two method

### 1) port forwarding
kubectl port-forward hellow.com 8090:3000

### 2) create service
kubectl expose pod hellow.com --type=NodePort --name node-hellow

kubectl get service

minikube service node-hellow


### delete pod
kubectl delete pod hello.com


### useful command with namespace
kubectl attach hellow.com -n dgk 

kubectl exec hellow.com -n dgk -- ls /app


### context change
user와 cluster를 매칭한 것이 context이며, 이를 변경하여 다른 환경의 k8s를 활용할 수 있다.

kubectl config get-users

kubectl config use-context minikube

kubectl config use-context kubernetes-admin@kubernetes


# More Kubernetes

## Replication Controller 

### create replication controller 
kubectl create -f replication-controller/repl_controller_hellow.yml

### scale up running pod
kubectl scale --replicas=3 -f replication-controller/repl_controller_hellow.yml

### delete replication controller
kubectl delete -f replication-controller/repl_controller_hellow.yml




# Deep Kubernetes