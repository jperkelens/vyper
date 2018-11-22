import etcd
from vyper import v

client = etcd.Client(port=2379)

v.set_config_type("toml")
v.add_remote_provider("etcd", client, "/config.toml")
v.read_remote_config()

print("Hello " + v.get("hello"))
