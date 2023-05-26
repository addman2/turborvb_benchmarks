# TurboRVB Benchmarks

This repository contains the benchmarks for the Quantum Monte Carlo code TurboRVB. The benchmarks are used to measure the performance of TurboRVB on various workloads.

It is better not to clone the whole repository if not necessary:

```
git clone --depth 1 https://github.com/addman2/turborvb_benchmarks.git
```

## Workloads

The workloads used in the benchmarks are stored in the Workloads directory. Each workload is a tar.gz archive. The workloads are used to test the performance of TurboRVB on different types of calculations.

## Benchmarks

The benchmarks are stored in the Benchmarks directory. Each benchmark is a json (??). The benchmarks measure the performance of TurboRVB on a specific workload. Each benchmark file contains the time taken to run TurboRVB on the corresponding workload.

## Usage

To run the benchmarks, clone the repository and run TurboRVB on each workload file in the Workloads directory. Record the time taken to run TurboRVB on each workload and store it in a new benchmark file in the Benchmarks directory. The filename of the benchmark file should be the same as the corresponding workload file, but with the extension .benchmark.

```
python3 show.py

  gitrev  time                 workload               user      computer    software stack          walkers    mpi    omp        vmc          fn    vmc_forces    fn_forces
--------  -------------------  ---------------------  --------  ----------  --------------------  ---------  -----  -----  ---------  ----------  ------------  -----------
 5558682  18:47:01_24-05-2023  H-1024el-nopseudo-pbc  okohulak  Bobor       GNU_13_1-mkl-openmpi          1      1      1  1891.52    3848.2         1091.81       5178.69
 5558682  10:12:26_25-05-2023  P-1280el-pseudo-pbc    okohulak  Bobor       GNU_13_1-mkl-openmpi          1      1      1   513.743    139.469
 5558682  18:45:51_24-05-2023  H-300el-nopseudo-pbc   okohulak  Bobor       GNU_13_1-mkl-openmpi          1      1      1    30.2578   134.455         84.1208      481.091
 5558682  18:46:56_24-05-2023  H-686el-nopseudo-pbc   okohulak  Bobor       GNU_13_1-mkl-openmpi          1      1      1   740.842   1197.09         520.046      3420.13
 5558682  10:46:17_25-05-2023  CuO-26el-pseudo-open   okohulak  Bobor       GNU_13_1-mkl-openmpi          1      1      1     3.24       3.36877
```

