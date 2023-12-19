# Setting Redis Using Configmap
- Hello World 애플리케이션을 다섯 개의 인스턴스로 실행한다.
- 외부 IP 주소를 노출하는 서비스를 생성한다.
- 실행 중인 애플리케이션에 접근하기 위해 서비스 오브젝트를 사용한다.



# Deployments
디플로이먼트로 5개 파드 생성한다.
```
kubectl apply -f service-load-balancer.yaml -n test
```

디플로이먼트에 대한 정보를 확인한다.
```commandline
kubectl get deployments hello-world -n test
kubectl describe deployments hello-world -n test
```


# Service
디플로이먼트를 외부로 노출시키는 서비스 오브젝트를 생성한다.
```commandline
kubectl expose deployment hello-world --type=LoadBalancer --name=my-service -n test
```

서비스에 대한 정보를 확인한다.
( LoadBalancer Ingress의 IP 주소를 기억한다 )
```commandline
kubectl get services my-service -n test
kubectl describe services my-service -n test
```

서비스에 여러 엔드포인트가 파드 주소로 설정되어 있음을 알 수 있다.
```commandline
kubectl get pods --output=wide -n test
```

# Access
Hello World 애플리케이션에 접근하기 위해 외부 IP 주소 (LoadBalancer Ingress)를 사용한다.
```commandline
curl http://<external-ip>:<port>
```

성공적인 요청에 대한 응답으로 hello 메세지가 나타난다.
```commandline
Hello Kubernetes!
```

minikube를 사용하고 있다면, 아래 명령어를 통해, 자동으로 브라우저 내에서 Hello World 애플리케이션에 접근할 수 있다.
```commandline
minikube service my-service -n test
```

