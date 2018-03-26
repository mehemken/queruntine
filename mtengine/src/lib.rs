use std::ffi::CStr;
use std::os::raw::c_char;

#[no_mangle]
//pub extern fn exec_queries<'a>(msg: *const c_char) -> &'a String {
pub extern fn exec_queries<'a>(msg: *const c_char) -> &'a str {
    let my_json = unsafe { CStr::from_ptr(msg) };
    println!("My json:");
    println!("{}", my_json.to_str().unwrap());
    &my_json.to_str().unwrap()
}


#[cfg(test)]
pub mod tests;
