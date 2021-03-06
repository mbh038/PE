///
/// @file   primesieve.hpp
/// @brief  primesieve C++ API. primesieve is a library for fast prime
///         number generation, in case an error occurs a
///         primesieve::primesieve_error exception (derived form
///         std::runtime_error) will be thrown.
///
/// Copyright (C) 2017 Kim Walisch, <kim.walisch@gmail.com>
///
/// This file is distributed under the BSD License.
///

#ifndef PRIMESIEVE_HPP
#define PRIMESIEVE_HPP

#define PRIMESIEVE_VERSION "6.0"
#define PRIMESIEVE_VERSION_MAJOR 6
#define PRIMESIEVE_VERSION_MINOR 0

#include "primesieve/PrimeSieve.hpp"
#include "primesieve/primesieve_error.hpp"
#include "primesieve/iterator.hpp"
#include "primesieve/StorePrimes.hpp"

#include <stdint.h>
#include <vector>
#include <string>

/// Contains primesieve's C++ functions and classes.
namespace primesieve {

/// Store the primes <= stop in the primes vector.
template <typename T>
inline void generate_primes(uint64_t stop, std::vector<T>* primes)
{
  if (primes)
  {
    StorePrimes<std::vector<T> > sp(*primes);
    sp.storePrimes(0, stop);
  }
}

/// Store the primes within the interval [start, stop]
/// in the primes vector.
///
template <typename T>
inline void generate_primes(uint64_t start, uint64_t stop, std::vector<T>* primes)
{
  if (primes)
  {
    StorePrimes<std::vector<T> > sp(*primes);
    sp.storePrimes(start, stop);
  }
}

/// Store the first n primes in the primes vector.
template <typename T>
inline void generate_n_primes(uint64_t n, std::vector<T>* primes)
{
  if (primes)
  {
    Store_N_Primes<std::vector<T> > sp(*primes);
    sp.storePrimes(n, 0);
  }
}

/// Store the first n primes >= start in the primes vector.
template <typename T>
inline void generate_n_primes(uint64_t n, uint64_t start, std::vector<T>* primes)
{
  if (primes)
  {
    Store_N_Primes<std::vector<T> > sp(*primes);
    sp.storePrimes(n, start);
  }
}

/// Find the nth prime.
/// By default all CPU cores are used, use
/// primesieve::set_num_threads(int threads) to change the
/// number of threads.
/// @param n  if n = 0 finds the 1st prime >= start, <br/>
///           if n > 0 finds the nth prime > start, <br/>
///           if n < 0 finds the nth prime < start (backwards).
///
uint64_t nth_prime(int64_t n, uint64_t start = 0);

/// Count the primes within the interval [start, stop].
/// By default all CPU cores are used, use
/// primesieve::set_num_threads(int threads) to change the
/// number of threads.
///
uint64_t count_primes(uint64_t start, uint64_t stop);

/// Count the twin primes within the interval [start, stop].
/// By default all CPU cores are used, use
/// primesieve::set_num_threads(int threads) to change the
/// number of threads.
///
uint64_t count_twins(uint64_t start, uint64_t stop);

/// Count the prime triplets within the interval [start, stop].
/// By default all CPU cores are used, use
/// primesieve::set_num_threads(int threads) to change the
/// number of threads.
///
uint64_t count_triplets(uint64_t start, uint64_t stop);

/// Count the prime quadruplets within the interval [start, stop].
/// By default all CPU cores are used, use
/// primesieve::set_num_threads(int threads) to change the
/// number of threads.
///
uint64_t count_quadruplets(uint64_t start, uint64_t stop);

/// Count the prime quintuplets within the interval [start, stop].
/// By default all CPU cores are used, use
/// primesieve::set_num_threads(int threads) to change the
/// number of threads.
///
uint64_t count_quintuplets(uint64_t start, uint64_t stop);

/// Count the prime sextuplets within the interval [start, stop].
/// By default all CPU cores are used, use
/// primesieve::set_num_threads(int threads) to change the
/// number of threads.
///
uint64_t count_sextuplets(uint64_t start, uint64_t stop);

/// Print the primes within the interval [start, stop]
/// to the standard output.
///
void print_primes(uint64_t start, uint64_t stop);

/// Print the twin primes within the interval [start, stop]
/// to the standard output.
///
void print_twins(uint64_t start, uint64_t stop);

/// Print the prime triplets within the interval [start, stop]
/// to the standard output.
///
void print_triplets(uint64_t start, uint64_t stop);

/// Print the prime quadruplets within the interval [start, stop]
/// to the standard output.
///
void print_quadruplets(uint64_t start, uint64_t stop);

/// Print the prime quintuplets within the interval [start, stop]
/// to the standard output.
///
void print_quintuplets(uint64_t start, uint64_t stop);

/// Print the prime sextuplets within the interval [start, stop]
/// to the standard output.
///
void print_sextuplets(uint64_t start, uint64_t stop);

/// Returns the largest valid stop number for primesieve.
/// @return 2^64-1 (UINT64_MAX).
///
uint64_t get_max_stop();

/// Get the current set sieve size in kilobytes.
int get_sieve_size();

/// Get the current set number of threads.
int get_num_threads();

/// Set the sieve size in kilobytes.
/// The best sieving performance is achieved with a sieve size of
/// your CPU's L1 data cache size (per core). For sieving >= 10^17 a
/// sieve size of your CPU's L2 cache size sometimes performs
/// better.
/// @param sieve_size Sieve size in kilobytes.
/// @pre   sieve_size >= 1 && sieve_size <= 2048.
///
void set_sieve_size(int sieve_size);

/// Set the number of threads for use in
/// primesieve::count_*() and primesieve::nth_prime().
/// By default all CPU cores are used.
///
void set_num_threads(int num_threads);

/// Get the primesieve version number, in the form “i.j”.
std::string primesieve_version();

}

#endif
