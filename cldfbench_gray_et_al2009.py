import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "gray_et_al2009"

    def cmd_makecldf(self, args):
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                self.sample(
                    self.read_gzipped_text(self.raw_dir / 'a400-m1pcv-time.mcct.trees.gz'),
                    detranslate=True,
                    n=1,
                    as_nexus=True,
                ),
                nex,
                'summary',
            )
        posterior = self.sample(
            self.remove_burnin(
                self.read_gzipped_text(self.raw_dir / 'a400-m1pcv-time.trees.gz'), 1000),
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, self.raw_dir / 'a400.nex')
