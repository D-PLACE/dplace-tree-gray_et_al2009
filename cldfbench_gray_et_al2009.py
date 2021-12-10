import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "gray_et_al2009"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree(
                'a400-m1pcv-time.mcct.trees.gz', detranslate=True),
            self.metadata,
            args.log)
        
        posterior = self.sample(
            self.remove_burnin(
                self.raw_dir.read('a400-m1pcv-time.trees.gz'), 1000),
            detranslate=True,
            as_nexus=True)
        args.writer.add_posterior(
            posterior.trees.trees, 
            self.metadata, 
            args.log)
        
        args.writer.add_data(
            self.raw_dir.read_nexus('a400.nex'),
            self.characters, 
            args.log)
