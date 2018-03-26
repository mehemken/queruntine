########################################
# Basic func tests
########################################


def test_official_example(Runner, test_params_tuple_mongo):
    conn_str, queries = test_params_tuple_mongo

    runner = Runner(conn_str, queries)

    runner.run()


def test_runner_passes_payload_from_preproc_to_client(Runner, Client, Preprocessor, test_params_tuple_mongo):
    a, b = test_params_tuple_mongo
    preproc = Preprocessor(a, b)
    pre = preproc.get_payload()

    client = Client()
    got_response = client.get_response(pre)

    assert got_response


def test_runner_payload_is_output_of_preproc(Runner, Preprocessor):
    a, b = 'connection_string', ['query1', 'query2']

    runner = Runner(a, b)
    preproc = Preprocessor(a, b)

    payload_r = runner._payload
    payload_p = preproc.get_payload()

    assert payload_r == payload_p
