Error importing index.py:
Traceback (most recent call last):
File "/var/task/vc__handler__python.py", line 243, in <module>
__vc_spec.loader.exec_module(__vc_module)
File "<frozen importlib._bootstrap_external>", line 999, in exec_module
File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
File "/var/task/index.py", line 1, in <module>
from sgd import app
File "/var/task/sgd/__init__.py", line 8, in <module>
token = json.loads(tokenFromVar)
^^^^^^^^^^^^^^^^^^^^^^^^
File "/var/lang/lib/python3.12/json/__init__.py", line 339, in loads
raise TypeError(f'the JSON object must be str, bytes or bytearray, '
TypeError: the JSON object must be str, bytes or bytearray, not NoneType
/var/task/_vendor/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.6) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
/var/task/_vendor/googleapiclient/model.py:29: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
import pkg_resources
Python process exited with exit status: 1. The logs above can help with debugging the issue.
