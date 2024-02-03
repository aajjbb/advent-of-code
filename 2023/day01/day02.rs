use std::collections::HashMap;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let mut lines = io::stdin().lock().lines();
    let mut sum = 0;

    let mut digit_map = HashMap::new();

    digit_map.insert("1",     1);
    digit_map.insert("one",   1);
    digit_map.insert("2",     2);
    digit_map.insert("two",   2);
    digit_map.insert("3",     3);
    digit_map.insert("three", 3);
    digit_map.insert("4",     4);
    digit_map.insert("four",  4);
    digit_map.insert("5",     5);
    digit_map.insert("five",  5);
    digit_map.insert("6",     6);
    digit_map.insert("six",   6);
    digit_map.insert("7",     7);
    digit_map.insert("seven", 7);
    digit_map.insert("8",     8);
    digit_map.insert("eight", 8);
    digit_map.insert("9",     9);
    digit_map.insert("nine",  9);

    while let Some(line) = lines.next() {
	let curr_line = line.unwrap();

	if curr_line.len() == 0 {
	    break;
	}

	let mut digits: Vec<i32> = Vec::new();

	for (i, _) in curr_line.chars().enumerate() {
	    for (key, value) in &digit_map {
		if i + key.len() > curr_line.len() {
		    continue;
		}
		let substr = &curr_line[i..(i + key.len())];

		if !key.eq(&substr) {
		    continue
		}

		digits.push(*value);
		//println!("{}", &substr);
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
