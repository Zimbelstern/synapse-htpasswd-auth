# synapse-htpasswd-auth
Password auth provider module for matrix synapse

## Installation
In your synapse environment, install with pip:

```pip install synapse-htpasswd-auth/```

Add the following to your homeserver.yaml:

```
modules:
  - module: synapse_htpasswd_auth.HtpasswdAuthProvider
    config:
      htpasswd_path: /path/to/.htpasswd
```
