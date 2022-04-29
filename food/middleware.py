def my_middleware(get_response):
    print('one time initialization')












    def my_function(request):
        print('b4 view')



        




        response = get_response(request)









        print('this is after view')
        return response
    return my_function