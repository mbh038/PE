extern crate num;

const NUM_BINS : usize = 32;
const NUM_DIGITS : usize = 12;

fn cdf(n : usize) -> f64 {
    let two_to_the_n = num::pow(2.0, n);
    let nr = two_to_the_n - 1.0;
    let p = nr / two_to_the_n;
    num::pow(p, NUM_BINS)
}

fn expectation() -> f64 {
    let tolerance = 1.0 / num::pow(10.0, NUM_DIGITS);
    let mut p_prev = cdf(0);
    let mut p_curr = cdf(1);
    let mut p = p_curr - p_prev;
    let mut i = 1;
    let mut e_i = p;
    let mut e = e_i; 
    while e_i > tolerance {
        p_prev = p_curr;
        i = i + 1;
        p_curr = cdf(i);
        p = p_curr - p_prev;
        e_i = p * (i as f64);
        e = e + e_i;
    }
    e
}

fn main() {
    println!("{}", expectation());
}


