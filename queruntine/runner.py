class Runner:
    connection_string = ''
    queries = []

    def run(self):
        print('Connection string:', self.connection_string)
        print('Queries:')
        for i in self.queries:
            print(i)
