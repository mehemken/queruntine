use std::ffi::CStr;
use std::os::raw::c_char;

#[no_mangle]
pub extern fn exec_queries(msg: *const c_char) -> String {
    // The main function
    // This is where it starts
    // and also where it ends
    // It should take an arg
    // and return something
    println!("Hello world!");
    String::from("some bytes")
}

#[cfg(test)]
pub mod tests;
