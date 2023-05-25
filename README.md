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
