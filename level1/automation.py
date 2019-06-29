#!/usr/bin/python

# This script will install niginx-ingress controller and guestBook application in 2 namespaces
# It will also exposes application on 2 different hostname

import os
# Install Load balancer

# Install Kind:service name: ingress-nginx with type: LoadBalancer
os.system("kubectl apply -f yaml_files/mandatory.yaml")
os.system("kubectl apply -f yaml_files/ingress-nginx_service.yaml")

namespace_list = ["staging", "production"]
fileListToApply = ["redis-master-deployment.yaml","redis-master-service.yaml","redis-slave-deployment.yaml","redis-slave-service.yaml","frontend-deployment.yaml","frontend-service_nginx.yaml"]

# Create Namespace
for namespace in namespace_list:
    cmd= "kubectl create namespace " + namespace
    os.system(cmd)
    
for namespace in namespace_list:
    print(namespace)
    # Creating deployment and Service
    for fileName in fileListToApply:
        cmd= "kubectl create -f yaml_files/" + fileName + " -n " + namespace
        print(cmd)
        os.system(cmd)

# Expose application on desired hostname
os.system("kubectl create -f yaml_files/ingress_staging_guestbook_routing.yaml -n staging")
os.system("kubectl create -f yaml_files/ingress_production_guestbook_routing.yaml -n production")
