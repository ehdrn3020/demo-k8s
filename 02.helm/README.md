# Search

차트 리포지토리를 추가한다. 
가능한 헬름 차트 레포지토리를 위해서 
Artifact Hub를 확인한다.

https://artifacthub.io/

```
helm repo add bitnami https://charts.bitnami.com/bitnami
```

또는 여러 저장소들에 있는 헬름 차트들을 포괄하는 
헬름 허브를 검색한다.
```
helm search hub wordpress
```

# List
헬름을 사용하여 릴리스된 내용을 쉽게 확인할 수 있다.
```
helm list -n test
```

# Install

사용자가 지정한 릴리스 이름, 설치하려는 차트 이름의 2개 인수를 받는다.
```
helm install my-release oci://registry-1.docker.io/bitnamicharts/mariadb -n test
```

파일을 통한 설치 명령어
```
helm install <릴리즈명> -f <values 파일명> <chart 위치> -n <네임스페이스>
helm install my-release -f k8s/helm/values.yaml k8s/helm/ -n test
```


# Connect

Run a pod that you can use as a client
```commandline
kubectl run my-release-mariadb-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mariadb:11.1.3-debian-11-r0 --namespace test --command -- bash
```

To connect to primary service (read/write)
```commandline
mysql -h my-release-mariadb.test.svc.cluster.local -uroot -p my_database
```


# Uninstall
릴리스를 설치 제거하려면, helm uninstall 커맨드를 사용한다.
```
helm uninstall my-release -n test
```


# Customizing
차트에 어떤 옵션이 구성 가능한지 보려면, helm show values를 사용하자.
```
helm show values oci://registry-1.docker.io/bitnamicharts/mariadb
```

YAML 형식 파일에 있는 이러한 설정들을 오버라이드(override)하여, 설치시 파일과 함께 반영
```commandline
echo "{usernmae: user1, password: user1pw}" > config.yaml
helm install -f config.yaml oci://registry-1.docker.io/bitnamicharts/mariadb --generate-name -n test
```

# Upgrade
```commandline
ROOT_PASSWORD=$(kubectl get secret --namespace test my-release-mariadb -o jsonpath="{.data.mariadb-root-password}" | base64 -d)
helm upgrade --namespace test my-release oci://registry-1.docker.io/bitnamicharts/mariadb --set auth.rootPassword=$ROOT_PASSWORD
```

새로운 설정이 적용되었는지 확인
```commandline
helm get values my-release -n test
```

특정 릴리스의 리비전 번호를 확인
```commandline
helm history my-release -n test
```


# Rollback
```commandline
helm rollback my-release 1 -n test
```