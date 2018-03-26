/*########################################
This is the test suite for the Multi Tread Engine

For practicality purposes, I'm treating compiler
errors, messages and warnings as test results.
########################################*/
use super::exec_queries;
use std::ffi::CString;


#[test]
fn it_works() {
    let answer = 2 + 2;
    assert_eq!(answer, 4)
}
