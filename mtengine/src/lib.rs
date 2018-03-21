use std::ffi::CStr;
use std::os::raw::c_char;

#[no_mangle]
pub extern fn exec_queries(msg: *const c_char) -> *const c_char {
    println!("Hello world!");
    msg
}

#[cfg(test)]
pub mod tests;
