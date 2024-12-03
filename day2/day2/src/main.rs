use std::fs::File;
use std::io::{self, BufRead};
use std::time::Instant;

fn row_safe(vec: &Vec<i32>)->bool{
    // Create difference vector
    let mut diff_vec: Vec<i32> = vec![];
    let vsize:usize = vec.len()-1;
    let mut sig = 0;
    for i in 0..vsize{
        let v = vec[i+1]-vec[i];
        diff_vec.push(v);
        if v.abs()>3 || v == 0 {
            return false;
        }
        // If sign the signs are different it is unsafe
        if sig == 0{
            sig = v.signum()
        }
        else {
            if sig != v.signum(){
                // println!("sig was {}",sig);
                // println!("{}",v.signum());
                return false;
            }
            
        }
    }
    // println!("{:?}",vec);
    // println!("{:?}",diff_vec);
    return true;
}

fn main() {
    let start = Instant::now();
    let file = File::open("input").unwrap();
    let reader = io::BufReader::new(file);
    let mut data: Vec<Vec<i32>> = vec![];
    for line in reader.lines() {
        let line = line.unwrap();
        let parts: Vec<&str> = line.split_whitespace().collect();
        let mut vec: Vec<i32> = vec![];
        for i in 0..parts.len(){
            match parts[i].parse::<i32>(){ 
                Ok(num) => vec.push(num),
                Err(e) => println!("Failed to parse: {}", e)
            }
            
        }
        data.push(vec);   
    }
    let mut safe = 0;
    for row in data.iter(){
        if row_safe(row){
        safe += 1}
    }
    println!("{}",safe);
    let mut safewp = 0;
    for row in data.iter(){
        if row_safe(row){
        safewp += 1;
    }
        else {
            for i in 0..row.len(){
                let mut new_vec: Vec<i32> = row.clone();
                let _ = new_vec.remove(i);
                if row_safe(&new_vec){
                    safewp += 1;
                    break;
                }
            }
        }
    }
    println!("{}",safewp);
    let duration = start.elapsed();
    println!("Time taken: {:?}", duration);
}
