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
