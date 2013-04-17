# ! /user/bin/env

import os
import sys

if __name__ == "__main__":
	os.environ.getdefault("DJANGO_SETTINGS_MODULE", "pi_io.settings")

	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.arg)
