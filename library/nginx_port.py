#!/usr/bin/python3
from ansible.module_utils.basic import AnsibleModule
import subprocess
import re

CONF = "/etc/nginx/conf.d/files.conf"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            port=dict(type='int', required=True)
        )
    )

    port = module.params['port']
    changed = False

    try:
        with open(CONF, "r") as f:
            content = f.read()
    except FileNotFoundError:
        module.fail_json(msg="nginx config not found")

    new_content = re.sub(r"listen\s+\d+;", f"listen {port};", content)

    if new_content != content:
        with open(CONF, "w") as f:
            f.write(new_content)
        changed = True

        subprocess.run(["systemctl", "reload", "nginx"], check=True)

    module.exit_json(
        changed=changed,
        message=f"Nginx configured on port {port}"
    )

if __name__ == '__main__':
    main()

