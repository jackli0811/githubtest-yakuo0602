class FastqFiles(object):
    """ Sorts compressed FastQ files provided to us from the Illumina sequencer. """
    def __init__(self, filenames):
        self._filenames = list(self._filter_names(filenames))

    def __iter__(self):
        for f in self._filenames:
            yield f

    def __len__(self):
        return len(self._filenames)

    @property
    def alignment_length(self):
        paired_length = len([(f1, f2) for f1, f2 in self.paired])
        single_length = len([f for f in self.single])
        return paired_length + single_length

    @property
    def paired(self):
        for f1, f2 in self._sort_filenames(paired=True):
            yield f1, f2

    @property
    def single(self):
        for f in self._sort_filenames(paired=False):
            yield f

    def _filter_names(self, data):
        # eliminate filenames that can't possibly be fastq files of interest
        for filename in reversed(data):
            if not filename.endswith('fastq.gz'):
                continue
            if '_I1_' in filename or '_I2_' in filename or '_I1.' in filename or '_I2.' in filename:
                continue
            yield filename

    def _sort_filenames(self, paired=True):
        # yield filenames that are the given type (single or paired)
        for filename in self._filenames:
            if '_R1_' in filename or '_R1.' in filename:
                pair = filename.replace('_R1_', '_R2_').replace('_R1.', '_R2.')
                if paired and pair in self._filenames:
                    yield filename, pair
                elif not paired and pair not in self._filenames:
                    yield filename
