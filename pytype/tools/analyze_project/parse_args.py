"""Argument parsing for analyze_project."""

import argparse


def parse_or_die(argv):
  """Parse command line args."""

  parser = argparse.ArgumentParser()
  parser.add_argument(
      'filenames', metavar='filename', type=str, nargs='*',
      help='input file(s)')
  parser.add_argument(
      '--tree', dest='tree', action='store_true', default=False,
      help='Display import tree.')
  parser.add_argument(
      '--unresolved', dest='unresolved', action='store_true', default=False,
      help='Display unresolved dependencies.')
  parser.add_argument(
      '-v', '--verbosity', dest='verbosity', type=int, action='store',
      default=1,
      help='Set logging level: 0=ERROR, 1 =WARNING (default), 2=INFO.')
  parser.add_argument(
      '--config', dest='config', type=str, action='store', default='',
      help='Configuration file.')
  parser.add_argument(
      '--generate-config', dest='generate_config', type=str, action='store',
      default='',
      help='Write out a dummy configuration file.')
  return parser.parse_args(argv)
