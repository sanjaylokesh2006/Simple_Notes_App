# Runtime Validation Report

Generated: 2026-07-12 13:26:18.026993

## generated_at

2026-07-12T07:55:42.436688Z

## project_path

generated\Simple_Notes_App

## dependencies

- **requirements_exists** : True
- **requirements_valid** : True
- **requirements_count** : 15
- **duplicate_requirements** : []
- **invalid_requirement_lines** : []
- **package_json_exists** : True
- **package_json_valid** : True
- **package_name** : simple-notes-app
- **package_version** : 1.0.0
- **package_dependency_count** : 3
- **recommendations** : []
- **status** : success
- **execution_time_seconds** : 0.0

## docker_build

- **status** : success
- **dockerfile_exists** : True
- **docker_available** : True
- **build_success** : True
- **error_type** : None
- **stdout** : 
- **stderr** : #0 building with "desktop-linux" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 826B 0.0s done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/python:3.11-slim
#2 DONE 7.6s

#3 [internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [1/8] FROM docker.io/library/python:3.11-slim@sha256:e031123e3d85762b141ad1cbc56452ba69c6e722ebf2f042cc0dc86c47c0d8b3
#4 resolve docker.io/library/python:3.11-slim@sha256:e031123e3d85762b141ad1cbc56452ba69c6e722ebf2f042cc0dc86c47c0d8b3 0.0s done
#4 DONE 0.0s

#5 [internal] load build context
#5 transferring context: 403B done
#5 DONE 0.0s

#6 [3/8] RUN apt-get update && apt-get install -y --no-install-recommends     curl     && rm -rf /var/lib/apt/lists/*
#6 CACHED

#7 [5/8] RUN pip install --upgrade pip &&     pip install --no-cache-dir -r requirements.txt
#7 CACHED

#8 [6/8] COPY backend/ ./backend/
#8 CACHED

#9 [7/8] RUN touch backend/__init__.py
#9 CACHED

#10 [2/8] WORKDIR /app
#10 CACHED

#11 [4/8] COPY requirements.txt .
#11 CACHED

#12 [8/8] RUN useradd -m appuser &&     chown -R appuser:appuser /app
#12 CACHED

#13 exporting to image
#13 exporting layers done
#13 exporting manifest sha256:401263612bd5c5bff7ea970b391eeafd2c0956f733edd1d1889ee706438937b8 done
#13 exporting config sha256:7e7df623c4c7c47c95c97c97c24ea41de025b90cc297ef12f003ece843d0660d done
#13 exporting attestation manifest sha256:daf1f2d72e320e4f42a3501ca457feb57c45d5fe42a67afc92601ecceec7fe3e
#13 exporting attestation manifest sha256:daf1f2d72e320e4f42a3501ca457feb57c45d5fe42a67afc92601ecceec7fe3e 0.0s done
#13 exporting manifest list sha256:6ecab613def615892e699374dd3805e553f24fa5626358720e2667c8d17d92e0 0.0s done
#13 naming to docker.io/library/ai_platform_runtime_test:latest done
#13 unpacking to docker.io/library/ai_platform_runtime_test:latest 0.0s done
#13 DONE 0.1s

- **execution_time_seconds** : 9.13

## docker_runtime

- **dockerfile_exists** : True
- **docker_compose_exists** : True
- **build** : {'status': 'success', 'dockerfile_exists': True, 'docker_available': True, 'build_success': True, 'error_type': None, 'stdout': '', 'stderr': '#0 building with "desktop-linux" instance using docker driver\n\n#1 [internal] load build definition from Dockerfile\n#1 transferring dockerfile: 826B done\n#1 DONE 0.0s\n\n#2 [internal] load metadata for docker.io/library/python:3.11-slim\n#2 DONE 0.7s\n\n#3 [internal] load .dockerignore\n#3 transferring context: 2B done\n#3 DONE 0.0s\n\n#4 [1/8] FROM docker.io/library/python:3.11-slim@sha256:e031123e3d85762b141ad1cbc56452ba69c6e722ebf2f042cc0dc86c47c0d8b3\n#4 resolve docker.io/library/python:3.11-slim@sha256:e031123e3d85762b141ad1cbc56452ba69c6e722ebf2f042cc0dc86c47c0d8b3 0.1s done\n#4 DONE 0.1s\n\n#5 [internal] load build context\n#5 transferring context: 403B done\n#5 DONE 0.0s\n\n#6 [2/8] WORKDIR /app\n#6 CACHED\n\n#7 [4/8] COPY requirements.txt .\n#7 CACHED\n\n#8 [5/8] RUN pip install --upgrade pip &&     pip install --no-cache-dir -r requirements.txt\n#8 CACHED\n\n#9 [6/8] COPY backend/ ./backend/\n#9 CACHED\n\n#10 [7/8] RUN touch backend/__init__.py\n#10 CACHED\n\n#11 [3/8] RUN apt-get update && apt-get install -y --no-install-recommends     curl     && rm -rf /var/lib/apt/lists/*\n#11 CACHED\n\n#12 [8/8] RUN useradd -m appuser &&     chown -R appuser:appuser /app\n#12 CACHED\n\n#13 exporting to image\n#13 exporting layers done\n#13 exporting manifest sha256:401263612bd5c5bff7ea970b391eeafd2c0956f733edd1d1889ee706438937b8 done\n#13 exporting config sha256:7e7df623c4c7c47c95c97c97c24ea41de025b90cc297ef12f003ece843d0660d done\n#13 exporting attestation manifest sha256:720c29ab3620b8c1da452a7bcdfd369c7e5cc725770f86ca7e23d7916536b4bd 0.0s done\n#13 exporting manifest list sha256:7adcd62c061f839b97e35a2ac24c08364a2938a2d148877a49b404ac8d60466d 0.0s done\n#13 naming to docker.io/library/ai_platform_runtime_test:latest done\n#13 unpacking to docker.io/library/ai_platform_runtime_test:latest 0.0s done\n#13 DONE 0.1s\n'}
- **startup** : {'container_started': False, 'logs': '', 'errors': '/usr/local/lib/python3.11/site-packages/pydantic/_internal/_config.py:386: UserWarning: Valid config keys have changed in V2:\n* \'orm_mode\' has been renamed to \'from_attributes\'\n  warnings.warn(message, UserWarning)\nTraceback (most recent call last):\n  File "<frozen runpy>", line 198, in _run_module_as_main\n  File "<frozen runpy>", line 88, in _run_code\n  File "/usr/local/lib/python3.11/site-packages/uvicorn/__main__.py", line 4, in <module>\n    uvicorn.main()\n  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1569, in __call__\n    return self.main(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1490, in main\n    rv = self.invoke(ctx)\n         ^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1353, in invoke\n    return ctx.invoke(self.callback, **ctx.params)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 907, in invoke\n    return callback(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 440, in main\n    run(\n  File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 609, in run\n    config.load_app()\n  File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 427, in load_app\n    return import_from_string(self.app)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 22, in import_from_string\n    raise exc from None\n  File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string\n    module = importlib.import_module(module_str)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module\n    return _bootstrap._gcd_import(name[level:], package, level)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import\n  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load\n  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked\n  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked\n  File "<frozen importlib._bootstrap_external>", line 940, in exec_module\n  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed\n  File "/app/backend/main.py", line 4, in <module>\n    from .api import router\n  File "/app/backend/api.py", line 6, in <module>\n    from .crud import create_note, get_note, update_note, delete_note\n  File "/app/backend/crud.py", line 4, in <module>\n    from .database import get_db\n  File "/app/backend/database.py", line 5, in <module>\n    from .config import settings\nModuleNotFoundError: No module named \'backend.config\'\n'}
- **status** : failed
- **reason** : Container failed to start
- **execution_time_seconds** : 13.43

## container_startup

- **container_started** : False
- **logs** : 
- **errors** : /usr/local/lib/python3.11/site-packages/pydantic/_internal/_config.py:386: UserWarning: Valid config keys have changed in V2:
* 'orm_mode' has been renamed to 'from_attributes'
  warnings.warn(message, UserWarning)
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/local/lib/python3.11/site-packages/uvicorn/__main__.py", line 4, in <module>
    uvicorn.main()
  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1569, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1490, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1353, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 907, in invoke
    return callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 440, in main
    run(
  File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 609, in run
    config.load_app()
  File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 427, in load_app
    return import_from_string(self.app)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/backend/main.py", line 4, in <module>
    from .api import router
  File "/app/backend/api.py", line 6, in <module>
    from .crud import create_note, get_note, update_note, delete_note
  File "/app/backend/crud.py", line 4, in <module>
    from .database import get_db
  File "/app/backend/database.py", line 5, in <module>
    from .config import settings
ModuleNotFoundError: No module named 'backend.config'

- **execution_time_seconds** : 11.0

## healthcheck

- **healthcheck_exists** : True
- **http_accessible** : True
- **status_code** : 200
- **response_time_ms** : 2030.51
- **status** : success
- **execution_time_seconds** : 2.03

## ports

- **dockerfile_exists** : True
- **compose_exists** : True
- **dockerfile_ports** : ['8000']
- **compose_ports** : [('8000', '8000')]
- **valid** : True
- **recommendations** : []
- **matching_ports** : ['8000']
- **missing_mappings** : []
- **status** : success
- **execution_time_seconds** : 0.0

## score

- **earned_weight** : 60
- **total_weight** : 100
- **percentage** : 60.0
- **grade** : D
- **passed** : False
- **passed_checks** : ['dockerfile_exists', 'docker_compose_exists', 'requirements_exists', 'package_json_exists', 'package_json_valid', 'docker_build', 'healthcheck_exists', 'ports_valid']
- **failed_checks** : ['container_startup', 'runtime_success']
- **recommendations** : ['Generated application should start successfully inside Docker.']
- **summary** : {'total_checks': 10, 'passed_checks': 8, 'failed_checks': 2}

## status

failed

## pipeline_execution_seconds

35.59

## summary

- **build_success** : True
- **container_started** : False
- **runtime_status** : failed

