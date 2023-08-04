try:
    from kubernetes import client, config

    # Try loading the in-cluster configuration for Kubernetes
    config.load_incluster_config()

    v1 = client.CoreV1Api()

    namespace = "vti"
    name = "hello-python-config"

    # Get the ConfigMap data
    config_map = v1.read_namespaced_config_map(name=name, namespace=namespace)
    config_data = config_map.data

    # Now, you can access the data in the ConfigMap
    env_dev_properties = config_data.get("env-dev.properties")
    if env_dev_properties is not None:
        env_dev_properties_str = config_data.get("env-dev.properties", "")
        env_dev_properties = {}
        for line in env_dev_properties_str.splitlines():
            key, value = line.split("=")
            env_dev_properties[key.strip()] = value.strip()
    else:
        print("Failed to retrieve env-dev.properties from ConfigMap.")
        env_dev_properties = {
            "author": "default_author",
            "difficulty": "default_value",
        }

except Exception as e:
    print(e)
    # If the 'kubernetes' package is not available, use default values
    env_dev_properties = {
        "author": "default_author",
        "difficulty": "default_value",
    }

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    print("okie")
    return f'Hello {env_dev_properties["author"]}'
