# SSH CLIENT PYTHON PARAMIKO FOR EC2 AWS

* Important: Create file config.py in root with data config:

    ```shell
        HOST = <config_host>
        USER = <config_user>
        KEY_FILE = <config_key_file_location>
        PASSWORD = <config_password>
    ```

* Don't forget run commands:

    ```shell
        python -m venv env
        ./env/Scripts/activate
        pip install -r requirements.txt
    ```