Experiment(description='Telescope data set',
           data_dir='../data/telescope/',
           max_depth=10, 
           random_order=False,
           k=1,
           debug=False, 
           local_computation=False, 
           n_rand=9,
           sd=2, 
           jitter_sd=0.1,
           max_jobs=300, 
           verbose=False,
           make_predictions=False,
           skip_complete=True,
           results_dir='../results/2013-12-18-telescope-add/',
           iters=250,
           base_kernels='SE,Per,Lin,Const,Noise',
           random_seed=1,
           period_heuristic=3,
           period_heuristic_type='min',
           subset=True,
           subset_size=250,
           full_iters=10,
           bundle_size=5,
           additive_form=True,
           mean='ff.MeanZero()',      # Starting mean
           kernel='ff.NoiseKernel()', # Starting kernel
           lik='ff.LikGauss(sf=-np.Inf)', # Starting likelihood 
           score='bic',
           search_operators=[('A', ('+', 'A', 'B'), {'A': 'kernel', 'B': 'base'}),
                             ('A', ('*', 'A', 'B'), {'A': 'kernel', 'B': 'base-not-const'}),
                             ('A', ('*-const', 'A', 'B'), {'A': 'kernel', 'B': 'base-not-const'}),
                             ('A', 'B', {'A': 'kernel', 'B': 'base'}),
                             ('A', ('None',), {'A': 'kernel'})])
