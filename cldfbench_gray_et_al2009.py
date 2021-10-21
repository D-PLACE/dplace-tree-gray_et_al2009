import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "gray_et_al2009"

    def cmd_makecldf(self, args):
        """
summary.trees: original/a400-m1pcv-time.mcct.trees.gz
	nexus trees -c -t $< -o $@

posterior.trees: original/a400-m1pcv-time.trees.gz
	# remove 1000 (10%), sample 1000
	nexus trees -c -d 1-1000 $< -o tmp
	nexus trees -n 1000 tmp -o $@
	rm tmp

data.nex:
	cp original/a400.nex $@
        """
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
