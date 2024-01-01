# Deploying FastAPI Applications with Redis
- Redis 리더를 실행
- 2개의 Redis 팔로워를 실행
- FastAPI 프론트엔드를 실행
- 프론트엔드 서비스를 노출하고 Redis 연결 확인



# Redis Database 실행

단일 복제본 Redis 파드를 디플로이먼트 컨트롤러로 실행하는 매니페스트 실행
```commandline
kubectl apply -f redis-leader-deployment.yaml -n test
```

Redis 파드가 실행 중인지 확인한다.
```commandline
kubectl get pods -n test
kubectl --namespace test exec -it {redis_name} -- redis-cli
```

Redis 리더 파드의 로그를 보려면 다음 명령어를 실행한다.
```commandline
kubectl logs -f deployment/redis-leader
```

프론트에서 데이터를 쓰려면 Redis와 통신해야 한다. Redis 파드로 트래픽을 프록시하려면 서비스를 생성해야 한다.
```commandline
kubectl apply -f redis-leader-service.yaml -n test
```

서비스의 목록을 질의하여 Redis 서비스가 실행 중인지 확인한다.
```commandline
kubectl get service -n test
```



# Redis 팔로워 구성
Redis 리더는 단일 파드이지만, 몇 개의 Redis 팔로워 또는 복제본을 추가하여 가용성을 높이고 트래픽 요구를 충족할 수 있다.


매니페스트 파일을 이용하여 Redis 디플로먼트 컨트롤러를 실행한다.
```commandline
kubectl apply -f redis-follower-deployment.yaml -n test
```

Redis 팔로워를 발견 가능(discoverable)하게 만드려면, 새로운 서비스를 구성해야 한다.
```commandline
kubectl apply -f redis-follower-service.yaml -n test
```

이전에 정의된 레이블과 일치하는 레이블 집합을 가진 redis-follower라는 서비스를 생성하므로, 서비스는 네트워크 트래픽을 Redis 파드로 라우팅한다.



# FAST API

도커파일로 fastapi 이미지 빌드
```commandline
docker build -t test/fastapi-app:1.0.0 .
```

로컬 이미지 minikube에 인식가능하도록 upload
```commandline
minikube image load test/fastapi-app:1.0.0
minikube image ls
```

매니페스트 파일을 이용하여 프론트엔드 디플로이먼트를 생성한다.
```commandline
kubectl apply -f fastapi-deployment.yaml -n test
```

서비스 생성
```commandline
kubectl apply -f fastapi-service.yaml -n test
```

minikube 일 경우 service를 따로 실행
```commandline
minikube service fastapi-app -n test
```
