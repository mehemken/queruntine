/*########################################
This is the test suite for the Multi Tread Engine

For practicality purposes, I'm treating compiler
errors, messages and warnings as test results.
########################################*/
use super::exec_queries;
use std::ffi::CString;


#[test]
fn messenger_accepts_const_c_char() {
    /* Although, the compiler checks for this now.
    Is this necessary? */
    let ptr = CString::new("Hello").unwrap().as_ptr();

    let _result = exec_queries(ptr);
}


#[test]
fn messenger_returns_c_char() {
    let ptr = CString::new("Hello").unwrap().as_ptr();
    let result = exec_queries(ptr);
    assert_eq!(ptr, result)
}
