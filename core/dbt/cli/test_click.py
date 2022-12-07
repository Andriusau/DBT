import click
import os
import sys
from typing import Optional

from dbt.cli.main import cli as dbt, deps
from dbt.cli.flags import Flags

from dbt.adapters.factory import adapter_management
from dbt.profiler import profiler
from dbt.config.runtime import load_project, load_profile
from dbt.tracking import initialize_from_flags



def make_context(args, command=dbt) -> Optional[click.Context]:
    try:
        ctx = command.make_context(command.name, args)
    except click.exceptions.Exit:
        return None
    # ctx.invoked_subcommand = ctx.protected_args[0] if ctx.protected_args else None
    # ctx.obj = {}
    # ideas option3
    # create_dbt_ctx(ctx)
    return ctx

def convert_to_args(dict):
    args = []
    for k, v in dict.items():
        args.append(f"--{k}")
        args.append(v)
    return args

cli_args = ['--printer-width', '100', 'run', '--project-dir', '/Users/chenyuli/git/python-models-test-project-small']
command = 'run'




ctx = make_context(cli_args)
# ctx command.make_context(command.name, args)
dbt.forward('run', ctx)

# cli_args = ['--project-dir', '/Users/chenyuli/git/python-models-test-project-small']
# ctx_flag = make_context(cli_args, dbt.commands[command])

# ctx_flag = make_context([command] + cli_args)
# flags = Flags(ctx=ctx_flag, args=[command] + cli_args)
# breakpoint()

# initialize_from_flags(flags.ANONYMOUS_USAGE_STATS, flags.PROFILES_DIR)
# # Profile
# profile = load_profile(
#     flags.PROJECT_DIR, flags.VARS, flags.PROFILE, flags.TARGET, flags.THREADS
# )

# # Project
# project = load_project(flags.PROJECT_DIR, flags.VERSION_CHECK, profile, flags.VARS)
# try:
#     # this function actually will modify cli_args
#     ctx = make_context(cli_args, command=dbt.commands[command])
# except click.exceptions.UsageError as input_error:
#     raise ValueError('Invalid input: {}'.format(input_error))
# ctx.obj = {}
# ctx.obj["flags"] = flags
# ctx.obj["profile"] = profile
# ctx.obj["project"] = project

# dbt.commands[command].invoke(ctx)
