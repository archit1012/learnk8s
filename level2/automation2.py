#!/usr/bin/python

# This script will install niginx-ingress controller and guestBook application in 2 namespaces
# It will also exposes application on 2 different hostname

import os

# Helm installation
os.system("curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash")
os.system("kubectl --namespace kube-system create sa tiller")
os.system("kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller")
os.system("helm init --service-account tiller")
os.system("helm repo update")
os.system("kubectl get deploy,svc tiller-deploy -n kube-system")
 
# create development namespace for application deployment 
os.system("kubectl create namespace development")
 
# Deploy guest-bok application in development namespace
application_namespace_list = ["development"]
fileListToApply = ["redis-master-deployment.yaml","redis-master-service.yaml","redis-slave-deployment.yaml","redis-slave-service.yaml","frontend-deployment.yaml","frontend-service_nginx.yaml"]
 
for namespace in application_namespace_list:
    print(namespace)
    # Creating deployment and Service
    for fileName in fileListToApply:
        cmd= "kubectl create -f yaml_files/guestbook/" + fileName + " -n " + namespace
        print(cmd)
        os.system(cmd)
 
 
# Create monitoring namespace for monitoring tools deployment
os.system("kubectl create namespace monitoring")
  
# Deploy Prometheus
application_namespace_list = ["monitoring"]
fileListToApply = ["clusterRole.yaml","config-map.yaml","prometheus-deployment.yaml","prometheus-service.yaml"]
 
for namespace in application_namespace_list:
    print(namespace)
    # Creating deployment and Service
    for fileName in fileListToApply:
        cmd= "kubectl create -f yaml_files/prometheus/" + fileName + " -n " + namespace
        print(cmd)
        os.system(cmd)
 
# Deploy grafana
cmd = "helm install -f yaml_files/grafana/grafana_values.yaml stable/grafana -n monitoring" 
os.system(cmd)
 

# Deploy EFK
os.system("kubectl create namespace logging")

application_namespace_list = ["logging"] 
fileListToApply = ["elastic.yaml","kibana.yaml","fluentd-rbac.yaml","fluentd-daemonset.yaml","fluentd-service.yaml"]
 
for namespace in application_namespace_list:
    print(namespace)
    # Creating deployment and Service
    for fileName in fileListToApply:
        cmd= "kubectl create -f yaml_files/efk-kubernetes/" + fileName + " -n " + namespace
        print(cmd)
        os.system(cmd)
 
