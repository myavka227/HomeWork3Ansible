#!/usr/bin/python3
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            port=dict(type='int', required=True)
        )
    )

    port = module.params['port']

    module.exit_json(
        changed=True,
        message=f"Nginx port set to {port}"
    )

if __name__ == '__main__':
    main()
