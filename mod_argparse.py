import argparse

basic_argparse = 0
advance_argparse = 1

# Create ArgumentParser Object
parser = argparse.ArgumentParser(description="Example to study argparse")


if basic_argparse:
    # Add argument
    parser.add_argument("pos1", help="positional argument 1")
    parser.add_argument("pos2", help="positional argument 2")
    parser.add_argument("-o", "--optional-arg", help="optional argument", dest="opt", default="default")
    parser.add_argument("n", help="repeat time", type=int)
    parser.add_argument("-u", "--user-name", dest="user_name")

    #parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_false")
    parser.add_argument("-v", "--verbose", help="increase output verbosity")


    # Parser Argument
    args = parser.parse_args()

    # Main 
    print("Positional arg1:", args.pos1)
    print("Positional arg2:", args.pos2)
    print("Optional arg:", args.opt)

    for _ in range(args.n):
        print("Hello, {}".format(args.user_name))
        
    if args.verbose:
        print("Verbosity: turned on")
    else:    
        print("Verbosity: turned off")
        

if advance_argparse:       
    # Add argument
    parser.add_argument('-s', action='store', dest='simple_value',
            help='Store a simple value')

    parser.add_argument('-c', action='store_const', dest='constant_value',
            const='value-to-store',
            help='Store a constant value')

    parser.add_argument('-t', action='store_true', default=False,
            dest='boolean_switch',
            help='Set a switch to true')
    parser.add_argument('-f', action='store_false', default=False,
            dest='boolean_switch',
            help='Set a switch to false')

    parser.add_argument('-a', action='append', dest='collection',
            default=[],
            help='Add repeated values to a list')

    parser.add_argument('-A', action='append_const', dest='const_collection',
            const='value-1-to-append',
            default=[],
            help='Add different values to list')
    parser.add_argument('-B', action='append_const', dest='const_collection',
            const='value-2-to-append',
            help='Add different values to list')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    
    # Parser Argument
    results = parser.parse_args()
    
    # Main 
    print 'simple_value     =', results.simple_value
    print 'constant_value   =', results.constant_value
    print 'boolean_switch   =', results.boolean_switch
    print 'collection       =', results.collection
    print 'const_collection =', results.const_collection   