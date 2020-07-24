fn main() {
    let n: f64 = 132.00;
    let ans = collatz(n);
}

fn collatz(n: f64) -> f64 {
    println!("{}", n);
    return if n == 1.00 {
        n
    } else if n % 2.00 == 0.00 {
        return collatz(n / 2.00)
    } else {
        return collatz((n * 3.00) + 1.00)
    }
}
