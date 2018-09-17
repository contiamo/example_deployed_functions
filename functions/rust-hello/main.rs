use std::io;

fn main() -> () {
  let mut input = String::new();
  match io::stdin().read_line(&mut input) {
    Ok(_n) => {
        println!("Hi there, you said: {}", input);
    }
    Err(error) => println!("error: {}", error),
}
}