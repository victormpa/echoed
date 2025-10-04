import click


@click.group()
@click.option("--verbose", is_flag=True, help="Enable verbose output")
@click.pass_context
def main(ctx, verbose):
    """
    Welcome to Echoed.
    """
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose
