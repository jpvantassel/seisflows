
WORKFLOW='inversion'    # inversion, migration
SOLVER='specfem2d'      # specfem2d, specfem3d
SYSTEM='multicore'      # serial, pbs, slurm
OPTIMIZE='LBFGS'        # base, newton
PREPROCESS='base'       # base
POSTPROCESS='base'      # base

MISFIT='Waveform'
MATERIALS='LegacyAcoustic'
DENSITY='Constant'


# WORKFLOW
BEGIN=1                 # first iteration
END=5                   # last iteration
NREC=132                # number of receivers
NSRC=25                 # number of sources
SAVEGRADIENT=1          # save gradient how often


# PREPROCESSING
FORMAT='su'             # data file format
CHANNELS='y'            # data channels
DTYPE='d'               # data type 'd'=displacement
NORMALIZE=0             # normalize
BANDPASS=0              # bandpass
FREQLO=0.               # low frequency corner
FREQHI=0.               # high frequency corner


# POSTPROCESSING
SMOOTH=20.              # smoothing radius
SCALE=6.0e6             # scaling factor


# OPTIMIZATION
PRECOND=None            # preconditioner type
STEPMAX=10              # maximum trial steps
STEPTHRESH=0.1          # step length safeguard


# SOLVER
NT=4800                 # number of time steps
DT=0.06                 # time step
F0=0.084                # dominant frequency


# SYSTEM
NTASK=25                # must satisfy 1 <= NTASK <= NSRC
NPROC=1                 # processors per task

