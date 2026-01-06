#
# Copyright 2024 Frank Stutz.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import subprocess
from typing import Optional
from .mlog import mlog


def rcmd(command: str | list[str], use_shell: bool = True) -> Optional[str]:
    """
    Run a shell command and return the output.

    Warning: Uses shell=True by default which can be a security risk with user input.
    Set use_shell=False for untrusted input (requires command as list).

    Args:
        command: Shell command to execute (string if use_shell=True, list if use_shell=False)
        use_shell: If True, use shell=True (default). Set to False for security with untrusted input.

    Returns:
        Command output as string, or None if command fails

    Raises:
        SystemExit: If command fails (exit code 1)
    """
    try:
        result = subprocess.check_output(command, shell=use_shell, text=True)
        return result
    except subprocess.CalledProcessError as e:
        mlog("ERROR", f"Error executing command: {e}", 1)
