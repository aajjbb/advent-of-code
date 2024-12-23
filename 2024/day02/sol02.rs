use std::io::{self, BufRead};

fn is_valid(numbers: Vec<i32>) -> bool {
    let mut valid = true;

    for i in 1..numbers.len() {
        let diff = (numbers[i - 1] - numbers[i]).abs();

        if diff < 1 || diff > 3 {
            valid = false;
        }

        if i > 1 {
            let diff_a = numbers[i - 2] - numbers[i - 1];
            let diff_b = numbers[i - 1] - numbers[i];

            if (diff_a > 0 && diff_b < 0) || (diff_a < 0 && diff_b > 0) {
                valid = false;
            }
        }
    }

    return valid;
}

fn main() {
    let mut lines = io::stdin().lock().lines();
    let mut count_safe = 0;

    while let Some(line) = lines.next() {
	let curr_line = line.unwrap();

	if curr_line.len() == 0 {
	    break;
	}

        let numbers: Vec<i32> = curr_line
            .split_whitespace()
            .filter_map(|num_str|
               num_str.parse::<i32>().ok()
            )
            .collect();

	for i in 0..numbers.len() {
            let mut spliced_vec = numbers.clone();
            spliced_vec.splice(i..i + 1, std::iter::empty());

            if is_valid(spliced_vec) {
                count_safe += 1;
                break;
            }
        }
    }

    println!("{}", count_safe);
}
