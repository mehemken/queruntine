use std::ffi::CStr;
use std::os::raw::c_char;

#[no_mangle]
pub extern fn exec_queries() -> String {
    // The main function
    // This is where it starts
    // and also where it ends
    // It should take an arg
    // and return something
    println!("Hello world!");
    String::from("some bytes")
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
