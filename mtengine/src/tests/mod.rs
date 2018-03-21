use super::exec_queries;
use std::ffi::CString;


#[test]
fn it_works() {
    assert_eq!(2 + 2, 4);
}


#[test]
fn messenger_accepts_const_c_char() {
    let ptr = CString::new("Hello").unwrap().as_ptr();

    let _result = exec_queries(ptr);
}
