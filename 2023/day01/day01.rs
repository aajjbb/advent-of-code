use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let mut lines = io::stdin().lock().lines();
    let mut sum = 0;

    while let Some(line) = lines.next() {
	let curr_line = line.unwrap();

	if curr_line.len() == 0 {
	    break;
	}

	let mut digits: Vec<i32> = Vec::new();

	for ch in curr_line.chars() {
	    if ch.is_ascii_digit() {
		digits.push(ch as i32 - '0' as i32);
	    }
	}

	let first_digit = digits.first().unwrap();
	let last_digit = digits.last().unwrap();

	sum += first_digit * 10 + last_digit;

	//println!("{} {} {} - {}", curr_line, first_digit, last_digit, first_digit * 10 + last_digit)
    }

    println!("{}", sum);

    Ok(())
}
