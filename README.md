
- prerequisite
  - kubernetes cluster up and running
  - Connectivity to download packages
  - clone test repository : git clone https://github.com/archit1012/test


1. Instructions
	1. $ cd level1/
	2. $ python automation.py
	   - Deploys guestbook application in staging and production namespace
	   - Deploys nginx ingress controller and creates routes

    3. configure /etc/host file add below entry
       - IP guestbook.testweb.io
       - IP staging-guestbook.testweb.io

    4. Testing Autoscaller
       - $ sh load_generator.sh
       - It sends get request in infinite loop and after couple of minutes one can see new pod getting created

	5. Refer: level1/Test_documentation.pdf
	   - file contains executed steps and evidence for each step given in assignment	
	
2. Instructions 
	1. $ cd level2/
	2. $ python automation2.py
		- Deploys Helm, guestbook application, promethues, grafana and EFK stack
	3. Exposing NodePort
	   - Get all running services
	     - $ kubectl get svc --all-namespaces | grep -i nodeport
	   - Create rule in firewall for google cloud
	     - $ gcloud compute firewall-rules create <name Of service> --allow tcp:<NodePort of Service>

	4. Accessing grafana and Kiabana
	   - IP of Master Node:NodePort

	5. Creating visualization for grafana
	   - Add datasource for grafana : http://prometheus-service.monitoring:8080/
	   - Create visualizing by adding json file "level2/yaml_files/grafana/grafana_dashboard_json_model_k8s_pod_matrics.json" 
    
    6. Creating visualization for Kiabana
       - Create index "logstash*" and add @timestamp as filter
	7. Refer: level2/Level2-Test_documentation.pdf
	   - file contains executed steps and evidence for each step given in assignment	
