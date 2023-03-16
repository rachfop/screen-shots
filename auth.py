import click


@click.command()
@click.argument("url")
@click.argument("context_file", type=click.File("w"))
def auth(url, context_file):
    """
    Open browser so user can manually authenticate with the specified site,
    then save the resulting authentication context to a file.

    Usage:

        shot-scraper auth https://github.com/ auth.json
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        click.echo("Hit <enter> after you have signed in:")
        input()
        storage = context.storage_state()
        context_file.write(storage)
        click.echo("Authentication context saved to {}.".format(context_file.name))


if __name__ == "__main__":
    auth()
