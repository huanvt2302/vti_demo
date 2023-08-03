#!/bin/sh
kubectl apply -f deployment.yaml
kubectl apply -f role.yaml
# kubectl port-forward -n vti hello-python-67f77b495b-5fvv6 5001:5001
