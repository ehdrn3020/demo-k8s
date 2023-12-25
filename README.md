# 01.ready
다양한 기본 예제
- deployment
- service
- pod-lifecycle
- healthcheck
- configmap
- ingress

# 02.helm
helm을 통한 mariadb 설치 및 실행 예제

# 03.setting-redis-using-configmap
configmap을 이용한 redis 설정값 셋팅
- Redis 설정값으로 컨피그맵을 생성한다.
- 생성된 컨피그맵을 마운트하고 사용하는 Redis 파드를 생성한다.
- 설정이 잘 적용되었는지 확인한다.

# 04.access-app-by-ingress
Ingress를 통해 외부에서 Service Access 예제 
- Hello World 파드를 실행한다.
- 외부에서 접근하기 위한 서비스를 생성한다.
- 실행 중인 애플리케이션에 접근해본다.

# 05.deploy-fastapi-app-with-redis
Redis와 연결된 FastAPI 앱 배포 예제
- Redis 리더를 실행
- 2개의 Redis 팔로워를 실행
- FastAPI 프론트엔드를 실행
- 프론트엔드 서비스를 노출하고 Redis 연결 확인