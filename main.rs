// src/main.rs

// src/main.rs

fn main(){
    println!("hello print");
    //  if want any var to mutable 
    let mut x = 5 ; 
    println!("{}",x);
    let x = 6 ; 
    println!("the updated x is {}",x);
    
    // compund types 
    // types > Tuple 
    let person:(&str , u32) = ("rohit",32);
    println!("{}",person.0); // first element 
    println!("the persons age is {}",person.1); // second element 
    
    // types > array 
    let score:[i32;3]=[90,23,120];
    println!("the first element is {}",score[0]); // first element 

    call();
    control();
    flow();
    loop_create();
    while_lop();
}

fn call(){
    call_name("Debajyoti");
    println!("sum is {}",add(20,23));
}
fn call_name(name:&str){
    println!("hello {}",name);
}

fn add(a:i32 , b:i32)->i32 {
    a+b //it a expression 
}


// control flow 
fn control(){
    let number : i32 = 6 ;
    if number % 2 == 0 {
        println!("the number is even")
    } else {
        println!("the number is odd")
    }

}

fn flow(){
    let number : i32 = 10;
    let label = if number % 2 == 0 {"even"} else {"odd"};
    println!("{}",label)
}

// loop create 
fn loop_create(){
    let mut counter = 0 ;
    let result = loop {
        counter+=1;
        if counter == 5 {
            break counter * 2 ;
        }
    };

    println!("the result of the loop is {}",result)
}

// while loop 
fn while_lop(){
    let mut n : i32 = 4 ;
    while n!=0 { 
        println!("{}",n);
        n-=1;
    
     }
 
    println!("loop off");

    //  range in loop 
    for i in 1..4{
        println!("{}",i);
    }

    // array element print in loops 
    let scopes  = [90,123,78];
    for score in scopes {
        println!("scores is : {}",score)
    }
    
}
