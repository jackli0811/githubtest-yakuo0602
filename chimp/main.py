"""
Chip-Hybridized Interaction Mapping Platform

Usage:
  chimp map FASTQ_DIRECTORY PATHS_TO_BAMFILES ... [-v | -vv | -vvv]
  chimp align PROJECT_NAME ALIGNEMT_READ_NAME (--alignment_channel <alignment_channel> | --alignment_index <alignment_index>) [--min_hits] [--rotation_estimate] [--snr_threshold] [--tile_width_estimate] [-v | -vv | -vvv]
  chimp preprocess [-v | -vv | -vvv ]

Options:
  -h --help     Show this screen.
  --version     Show version.

Commands:
  map       maps all the reads in the fastq files, typically for separating phiX
  align     maps reads from the high-throughput sequencer to fluorescent points in microscope image data

"""
from chimp.controller import align, preprocess
from docopt import docopt
import logging
from chimp.model.clargs import CommandLineArguments
from chimp.model.constants import VERSION
import os


def main(**kwargs):
    arguments = CommandLineArguments(docopt(__doc__, version=VERSION), os.getcwd())

    log = logging.getLogger()
    log.addHandler(logging.StreamHandler())
    log.setLevel(arguments.log_level)

    # make some space to distinguish log messages from command prompt
    for _ in range(3):
        log.info('')

    commands = {'align': align.main,
                'preprocess': preprocess.fitsify}
    commands[arguments.command](arguments)


if __name__ == '__main__':
    main()
