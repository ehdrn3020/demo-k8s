# Install Minikube

### guide
```
https://minikube.sigs.k8s.io/docs/start/
```

### path
```/opt/homebrew/bin/minikube```

### dash board
minikube dashboard



# Basic Kubernetes 

### context change
user와 cluster를 매칭한 것이 context이며, 이를 변경하여 다른 환경의 k8s를 활용할 수 있다.
context 는 kubectl 을 깔면 생성되는 파일인 ~/.kube/config 파일에서 설정한다.

```
kubectl config get-users
```
```
kubectl config use-context minikube
```
```
kubectl config use-context kubernetes-admin@kubernetes
```

### .kube/config 파일
크게 clusters, users, context로 나뉘어져있으며
kubectl config use-context {context.name} 값을 통해 클러스터 접근 정보를 스위치 할 수 있다.

* clusters : 쿠버네티스 클러스터 정보
* users : 클러스터에 접근할 유저 정보
* context : cluster와 user값을 조합으로 하나의 set으로 만들어 k8s에 접근
* current-context : 현재 사용하는 context 지정
```
kubectl config view
```


### namespace
```
kubectl create namespace myNameSpace
```
```
kubectl get namespace
```


### create pod
```
kubectl create -f tutorial/hellow.yml
```

### check created pod
```
kubectl get pod
```

### check detail
```
kubectl describe pod hellow.com
```

### create service of two method

### 1) port forwarding
```
kubectl port-forward hellow.com 8090:3000
```
### 2) create service
```
kubectl expose pod hellow.com --type=NodePort --name node-hellow
```
```
kubectl get service
```
```
minikube service node-hellow
```

### delete pod
```
kubectl delete pod hello.com
```

### useful command with namespace
```
kubectl attach hellow.com -n dgk 
```
```
kubectl exec hellow.com -n dgk -- ls /app
```


# More Kubernetes


## Replication Controller 

### create replication controller 
```
kubectl create -f replication-controller/repl_controller_hellow.yml
```

### scale up running pod
```
kubectl scale --replicas=3 -f replication-controller/repl_controller_hellow.yml
```

### delete replication controller
```
kubectl delete -f replication-controller/repl_controller_hellow.yml
```


## Deployments

### create deployment
```
kubectl create -f deployment/dp_hellow.yml --record
```

### get deployments
```
kubectl get deployments
```

### get information of replica set
```
kubectl get rs
```

### check pods
```
kubectl get pods --show-labels
```

### get deployment status
```
kubectl rollout status deployment/dp-hellow
```

### start dp-hellow service
```
kubectl expose deployment dp-hellow --type=NodePort --name node-hellow
```
```
minikube service node-hellow --url
```

### run image label version2
```
kubectl set image deployment/dp-hellow k8s-demo=wardviaene/k8s-demo:2
```

### check changed version 
```
kubectl rollout status deployment/dp-hellow
```

### old one is temineted and new one is running
```
kubectl get pods --show-labels
```

### get the rollout history ( need --record when act deployment)
```
kubectl rollout history deployment/dp-hellow
```

### get deployment history details
```
kubectl describe deployment dp-hellow
```

### rollback to choosed previous version
```
kubectl rollout undo deployment/dp-hellow --to-revision=n
```

### edit the deployment object
```
kubectl edit deployment/dp_hellow
```


## Service

### start service
```
kubectl create -f service/svc_nodeport.yml
```

### check url
```
minikube service service-hellow --url
```


## Health check

### start liveness deployment for healthcheck
```
kubectl create -f healthcheck/hc_liveness_cmd.yml && watch -n1 kubectl get pods
```

### start readiness deployment for healthcheck
```
kubectl create -f healthcheck/hc_readiness_cmd.yml && watch -n1 kubectl get pods
```

### check defined liveness information in pod
```
kubectl describe pods hellow-liveness-13241234
```

### edit deployment information
```
kubectl edit deployment/hellow-liveness
```

### raise error
```
kubectl exec hellow-liveness-68659b8789-rq9wv -- rm -rf /tmp
kubectl exec hellow-readiness-5b7bd74dd8-4zs7d -- rm -rf /tmp
```

### Check the difference between 'liveness' and 'readiness'
```
kubectl get pods
```

### Reference
https://bcho.tistory.com/1264

https://velog.io/@hoonki/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-Probe


## Pod State

### pod status
* running
* pending
* succeeded
* failed
* unknow : ex. network error

### container state
container state is from docker cotainer
* running
* terminated
* waiting


# Pod Lifecycle

diagram


<img width="731" alt="스크린샷 2023-05-28 오후 9 04 32" src="https://github.com/ehdrn3020/demo-k8s/assets/20849970/c011f919-1a15-42b9-957e-862db471f793">

### Monitoring Pods
```
watch -n1 kubectl get pods
```

### start deployment
```
kubectl create -f pod-lifecycle/lifecycle.yml
```

### check log
```
kubectl get pods
kubectl exec -it lifecycle-57bd4568f5-57ctd -- cat /timing 
```


# DNS Service Discovery

### start relative secret, deployment, service
```
kubectl create -f dns-service/secrets.yaml
kubectl create -f dns-service/database.yaml
kubectl create -f dns-service/service-db.yaml
kubectl create -f dns-service/deployment.yaml
kubectl create -f dns-service/service-node.yaml
```

### start service
```
minikube service service-db-hellow --url
```


# Configmap

### create configmap
```
kubectl create configmap nginx-config --from-file=configmap/reverseproxy.conf
```

### check configmap
```commandline
kubectl get configmap
kubectl get configmap nginx-config -o yaml
```

### create service appied configmap
```commandline
kubectl create -f configmap/nginx.yaml
kubectl create -f configmap/nginx-service.yaml
```

### start service 
```commandline
minikube service helloworld-nginx-service --urlÏ
```

### check service details
```commandline
curl http://127.0.0.1:54757 -vvvv
```

### find out configmap appied in containers
```commandline
kubectl exec -i -t helloworld-nginx -c nginx -- bash
cat /etc/nginx/conf.d/reverseproxy.conf
```


minikube addons enable ingress
kubectl get svc -n ingress-nginx


# Deep Kubernetes
