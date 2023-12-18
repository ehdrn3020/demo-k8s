# Setting Redis Using Configmap
- Redis 설정값으로 컨피그맵을 생성한다.
- 생성된 컨피그맵을 마운트하고 사용하는 Redis 파드를 생성한다.
- 설정이 잘 적용되었는지 확인한다.


# create config map
```
cat <<EOF >./example-redis-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: example-redis-config
data:
  redis-config: ""
EOF
```

위에서 생성한 컨피그맵을 Redis 파드 매니페스트와 함께 적용한다.
```
kubectl apply -f redis-config.yaml -n test
kubectl apply -f redis-pod.yaml -n test
```

생성확인 
```commandline
kubectl get pod/redis configmap/redis-config -n test 
```

# customizing

컨피그맵의 redis-config 키가 비어있는 것을 확인한다.
```commandline
kubectl describe configmap/redis-config -n test
```

kubectl exec 를 사용하여 파드에 접속하고, 현재 설정 확인을 위해서 redis-cli 도구를 실행한다.
```commandline
kubectl --namespace test exec -it redis -- redis-cli
```

maxmemory 를 확인한다.
```commandline
127.0.0.1:6379> CONFIG GET maxmemory
1) "maxmemory"
2) "0"
```

redis-config 컨피그맵에 몇 가지 설정값을 추가해 본다.
```commandline
redis-config: |
    maxmemory 2mb
    maxmemory-policy allkeys-lru    
```

갱신된 컨피그맵을 적용한다.
```commandline
kubectl apply -f redis-config.yaml -n test
```

파드는 연관된 configmap에서 갱신된 값을 인지하기 위해 재시작이 필요한다.
```commandline
kubectl delete pod redis -n test
kubectl apply -f redis-pod.yaml -n test
```

방금 추가한 설정값을 확인할 수 있을 것이다.
```commandline
kubectl describe configmap/redis-config -n test
```

redis에서 설정 값 갱신을 확인한다.
```commandline
kubectl --namespace test exec -it redis -- redis-cli

127.0.0.1:6379> CONFIG GET maxmemory
1) "maxmemory"
2) "2097152"
```

# Delete

```commandline
kubectl delete pod/redis configmap/redis-config -n test
```