import os
import json
import datetime

import click

WATSON_FILE = os.path.join(os.path.expanduser('~'), '.watson')


def get_watson():
    try:
        with open(WATSON_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except ValueError:
        return {}


def save_watson(content):
    with open(WATSON_FILE, 'w+') as f:
        return json.dump(content, f, indent=2)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('project')
def start(project):
    watson = get_watson()
    start_time = datetime.datetime.now()

    if watson.get('current') is not None:
        project = watson['current'].get('project', "?")
        click.echo(
            ("Project {} is already started"
             .format(project, start_time)),
            err=True
        )
        return

    click.echo("Starting {} at {:%H:%M:%S}".format(project, start_time))

    watson['current'] = {
        'project': project,
        'start': start_time.isoformat()
    }

    save_watson(watson)


@cli.command()
@click.option('-m', '--message', default=None,
              help="Add a message to this frame")
def stop(message):
    watson = get_watson()
    stop_time = datetime.datetime.now()
    current = watson.get('current')

    if not current or not current.get('project'):
        click.echo("No project started", err=True)
        return

    click.echo("Stopping {}.".format(current['project']))

    if not watson.get('projects'):
        watson['projects'] = {}

    project = watson['projects'].get(current['project'])

    if not project:
        project = {'frames': []}
        watson['projects'][current['project']] = project

    frame = {
        'start': current['start'],
        'stop': stop_time.isoformat()
    }

    if message:
        frame['message'] = message

    project['frames'].append(frame)
    del watson['current']
    save_watson(watson)

if __name__ == '__main__':
    cli()