with open('nginx_logs.txt', 'r') as f:
    nums = f.read().splitlines()
    pars = ()
    for i in nums:
        i = i + "\n"
        remote_adr = i.split(' - - ')
        request_type_1 = remote_adr[1].split('] "')
        params = request_type_1[1].split(' ')
        request_type = params[0]
        requested_resource = params[1]
        pars = (remote_adr[0], request_type, requested_resource)
        print(pars)