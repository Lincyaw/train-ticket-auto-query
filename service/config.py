# URL配置
# kubectl get service -n ts
# ts-ui-dashboard                NodePort    10.110.153.240   <none>        8080:32010/TCP   12h
BASE_URL = "http://10.10.10.220:30193"

# 日志配置
LOG_LEVEL = "DEBUG"
LOG_FILE = "app.log"