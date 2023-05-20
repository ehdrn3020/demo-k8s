# Demo Kubernetes Example

### namespace
kubectl create namespace dgk
kubectl get namespace

### create pod
kubectl create -f tutorial/hellow.yml -n  dgk

### check created pod
kubectl get pod -n dgk

### check detail
kubectl describe pod hellow.com -n dgk

### create service of two method
### 1) port forwarding
kubectl port-forward hellow.com 8090:3000 -n dgk
### 2) create service
kubectl expose pod hellow.com --type=NodePort --name node-hellow -n dgk
kubectl get service -n dgk
minikube service node-hellow

### delete pod
kubectl delete pod hello.com -n dgk

### useful command
kubectl attach hellow.com -n dgk 
kubectl exec hellow.com -n dgk -- ls /app

### context change
user와 cluster를 매칭한 것이 context
context를 변경하여 다른 환경의 k8s를 활용할 수 있다.
kubectl config get-users
kubectl config use-context minikube
kubectl config use-context kubernetes-admin@kubernetes
