use std::fs::File;
use std::io::{self, BufRead};
use std::time::Instant;

fn main() -> io::Result<()> {
    let start = Instant::now();
    let file = File::open("../input")?;
    let reader = io::BufReader::new(file);
    
    let mut lhs: Vec<i32> = vec![];
    let mut rhs: Vec<i32> = vec![];
    for line in reader.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split_whitespace().collect();
        match parts[0].parse::<i32>(){ 
            Ok(num) => lhs.push(num),
            Err(e) => println!("Failed to parse: {}", e)
        }
        match parts[1].parse::<i32>(){ 
            Ok(num) => rhs.push(num),
            Err(e) => println!("Failed to parse: {}", e)
        }
    
    }
    lhs.sort();
    rhs.sort();

    let mut sum_of_differences: i32 = 0;
    let mut similarity: i32 = 0;
    for i in 0..lhs.len(){
        let difference = lhs[i]-rhs[i];
        sum_of_differences += difference.abs();
        if lhs.contains(&rhs[i]){
            similarity += &rhs[i]
        }
    }
    println!("Part1: {}", sum_of_differences);
    println!("Part2: {}", similarity);
    let duration = start.elapsed();
    println!("Time taken: {:?}", duration);
    Ok(())
}
