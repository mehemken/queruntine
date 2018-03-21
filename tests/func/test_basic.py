########################################
# Basic func tests
########################################


def test_official_example(Runner):
    runner = Runner()

    conn_str = 'mongodb://localhost:27017'
    queries = ['rust_basics.guesses.find({})']

    runner.connection_string = conn_str
    runner.queries = queries

    runner.run()


def test_runner_passes_payload_from_preproc_to_client(Runner, Client, Preprocessor):
    a, b = 'connection_string', ['query1', 'query2']
    runner = Runner(a, b)
    payload_r = runner._payload

    pre = Preprocessor(a, b)
    pre = pre.get_payload()
    client = Client(pre)
    payload_c = client._payload

    assert payload_r == payload_c


def test_runner_payload_is_output_of_preproc(Runner, Preprocessor):
    a, b = 'connection_string', ['query1', 'query2']

    runner = Runner(a, b)
    preproc = Preprocessor(a, b)

    payload_r = runner._payload
    payload_p = preproc.get_payload()

    assert payload_r == payload_p
